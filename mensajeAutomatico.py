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
PALABRA_CLAVE = os.environ["PALABRA_CLAVE"]

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

# Tarea que corre cada 48 horas
@tasks.loop(hours=48)
async def tarea_diaria():
    user = await bot.fetch_user(USER_ID)
    await user.send(MENSAJE_DIARIO)

    # Esperar 48 horas y verificar si hay respuesta
    await asyncio.sleep(48 * 3600)
    ultima = obtener_respuesta()
    if not ultima or datetime.now(timezone.utc) - ultima > timedelta(hours=48):
        alert_user = await bot.fetch_user(ALERT_CHANNEL_ID)
        if alert_user:
            await alert_user.send(MENSAJE_ALERTA)
        else:
            print(" No se encontró al usuario de alerta.")

        # Detener la tarea
        tarea_diaria.stop()

@bot.event
async def on_ready():
    print(f"🤖 Bot listo: {bot.user}")
    tarea_diaria.start()

@bot.event
async def on_message(message):
    if message.author.id == USER_ID and PALABRA_CLAVE.lower() in message.content.lower():
        guardar_respuesta()
        await message.channel.send(" Respuesta recibida. El tiempo ha sido reseteado.")
    await bot.process_commands(message)

# ----------------------------
# Servidor Flask para Replit
# ----------------------------
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "El bot está funcionando."

def run():
    app.run(host='0.0.0.0', port=8080)

def mantener_vivo():
    t = Thread(target=run)
    t.start()

mantener_vivo()

bot.run(TOKEN)
