import discord
from discord.ext import commands, tasks
import json
from datetime import datetime, timedelta
import asyncio
import os

# Variables de entorno seguras desde Replit Secrets
TOKEN = os.environ["DISCORD_TOKEN"]
USER_ID = int(os.environ["DISCORD_USER_ID"])
ALERT_CHANNEL_ID = int(os.environ["DISCORD_ALERT_CHANNEL_ID"])
MENSAJE_DIARIO = os.environ["MENSAJE_DIARIO"]
MENSAJE_ALERTA = os.environ["MENSAJE_ALERTA"]

bot = commands.Bot(command_prefix="!")

# Base de datos simple
def guardar_respuesta():
    with open("db.json", "w") as f:
        json.dump({"last_response": datetime.utcnow().isoformat()}, f)

def obtener_respuesta():
    try:
        with open("db.json", "r") as f:
            data = json.load(f)
            return datetime.fromisoformat(data["last_response"])
    except:
        return None

# Tarea que corre cada 24h
@tasks.loop(hours=24)
async def tarea_diaria():
    user = await bot.fetch_user(USER_ID)
    await user.send(MENSAJE_DIARIO)
    
    # Esperar 48 horas y verificar si respondió
    await asyncio.sleep(300)
    ultima = obtener_respuesta()
    if not ultima or datetime.utcnow() - ultima > timedelta(hours=48):
        canal = bot.get_channel(ALERT_CHANNEL_ID)
        await canal.send(MENSAJE_ALERTA)

@bot.event
async def on_ready():
    print(f"🤖 Bot listo: {bot.user}")
    tarea_diaria.start()

@bot.event
async def on_message(message):
    if message.author.id == USER_ID and "lycoris" in message.content.lower():
        guardar_respuesta()
        await message.channel.send("✅ Respuesta registrada. Me alegra saber de ti.")
    await bot.process_commands(message)

bot.run(TOKEN)
