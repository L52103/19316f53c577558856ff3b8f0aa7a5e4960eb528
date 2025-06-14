import discord
from discord.ext import commands, tasks
import json
from datetime import datetime, timedelta, timezone
import asyncio
import os

# Variables de entorno seguras desde Replit Secrets
TOKEN = os.environ["DISCORD_TOKEN"]
USER_ID = int(os.environ["DISCORD_USER_ID"])
ALERT_CHANNEL_ID = int(os.environ["DISCORD_ALERT_CHANNEL_ID"])
MENSAJE_DIARIO = os.environ["MENSAJE_DIARIO"]
MENSAJE_ALERTA = os.environ["MENSAJE_ALERTA"]

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Necesario para leer el contenido de los mensajes

bot = commands.Bot(command_prefix="!", intents=intents)

# Base de datos simple
def guardar_respuesta():
    with open("db.json", "w") as f:
        json.dump({"last_response": datetime.now(timezone.utc).isoformat()}, f)

def obtener_respuesta():
    try:
        with open("db.json", "r") as f:
            data = json.load(f)
            return datetime.fromisoformat(data["last_response"]).astimezone(timezone.utc)
    except:
        return None

# Tarea que corre cada 24h
@tasks.loop(hours=48)
async def tarea_diaria():
    user = await bot.fetch_user(USER_ID)
    await user.send(MENSAJE_DIARIO)

    # Esperar 48 horas y verificar si respondió
    await asyncio.sleep(48 * 3600)  # 48 horas reales
    ultima = obtener_respuesta()
    if not ultima or datetime.now(timezone.utc) - ultima > timedelta(hours=48):
        canal = bot.get_channel(ALERT_CHANNEL_ID)
        await canal.send(MENSAJE_ALERTA)

        # Detener la tarea diaria
        tarea_diaria.stop()


@bot.event
async def on_ready():
    print(f"🤖 Bot listo: {bot.user}")
    tarea_diaria.start()

@bot.event
async def on_message(message):
    if message.author.id == USER_ID and "lycoris" in message.content.lower():
        guardar_respuesta()
        await message.channel.send("✅ Respuesta registrada. El tiempo ha sido reseteado.")
    await bot.process_commands(message)

bot.run(TOKEN)
