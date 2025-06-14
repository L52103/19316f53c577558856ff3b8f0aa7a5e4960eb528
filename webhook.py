from flask import Flask, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip().lower()
    from_number = request.values.get("From", "")

    if "lycoris" in incoming_msg:
        # Guarda la hora de la última respuesta válida
        with open("db.json", "w") as f:
            json.dump({"last_response": datetime.utcnow().isoformat()}, f)
        print(f"✅ Lycoris detectado de {from_number}")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
