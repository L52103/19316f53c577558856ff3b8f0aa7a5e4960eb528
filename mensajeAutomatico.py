import json
from datetime import datetime, timedelta
from twilio.rest import Client
import os

# Carga credenciales desde variables de entorno
TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_FROM = "whatsapp:+14155238886"
DESTINO = "whatsapp:+56990907349"

client = Client(TWILIO_SID, TWILIO_AUTH)

# Mensajes personalizados
MENSAJE_ADVERTENCIA = "Contesta este mensaje con Lycoris"
MENSAJE_FINAL = "No se recibió respuesta. Esto es una alerta automatizada."

# Leer última respuesta
try:
    with open("db.json", "r") as f:
        data = json.load(f)
        ultima_respuesta = datetime.fromisoformat(data["last_response"]) if data["last_response"] else None
except:
    ultima_respuesta = None

# Verificar si han pasado más de 48 horas
ahora = datetime.utcnow()
tiempo_limite = timedelta(hours=48)

if not ultima_respuesta or (ahora - ultima_respuesta) > tiempo_limite:
    print("🚨 No hubo respuesta en 48 horas. Enviando alerta.")
    client.messages.create(
        body=MENSAJE_FINAL,
        from_=TWILIO_FROM,
        to=DESTINO
    )
else:
    print("✅ Ya se recibió respuesta dentro del plazo. No se envía alerta.")

# Siempre se envía advertencia diaria
client.messages.create(
    body=MENSAJE_ADVERTENCIA,
    from_=TWILIO_FROM,
    to=DESTINO
)
print("📤 Mensaje de advertencia enviado.")
