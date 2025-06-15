# Bot de Recordatorio y Verificación por Discord

Este bot envía un mensaje privado cada 48 horas a un usuario específico y espera una respuesta con una palabra clave. Si no recibe respuesta dentro del tiempo límite, se envía una alerta a otra persona. Ideal para chequeos periódicos.
---

##  ¿Qué hace este bot?

-  Envía un mensaje privado automático cada 48 horas a un usuario específico.
-  Espera una respuesta con una palabra clave (como "Lycoris").
-  Si no hay respuesta en el tiempo configurado, envía una alerta a otra persona.
-  Si se responde correctamente, se reinicia el temporizador.

> ⚠️ El bot y ambos usuarios **deben estar en el mismo servidor** para que el envío de mensajes funcione correctamente.

---

## 📦 Requisitos

- Cuenta de Discord
- Un servidor de Discord donde el bot esté invitado
- la persona que reciba el mensaje debe estar en el server tambien, de esta forma el bot lo puede encontrar
- [Replit](https://replit.com/) (o tu entorno Python preferido)

---

## 🧑‍💻 Importar el Proyecto en Replit

### 🔁 Opción Rápida: Clonar desde GitHub (o tambien puedes crear el tuyo e iniciar sesión)

1. Ve a [https://replit.com/import](https://replit.com/import)
2. Pega la URL de tu repositorio GitHub (ej. `https://github.com/usuario/bot-recordatorio-discord`)
3. Se importará automáticamente todo el código.

> Si no tienes el repo aún, puedes subir estos archivos manualmente o pedirme que te genere uno.

---

## 🔒 Configurar Variables de Entorno (Secrets en Replit)
(si no encuentra la opcion, a la izquierda hay un icono de 4 cuadrados, ahí lo buscas como secrets)
Haz clic en el ícono 🔐 de "Secrets" (Environment Variables) y agrega:

| Clave                      | Descripción                                 | Ejemplo                         |
|---------------------------|---------------------------------------------|---------------------------------|
| `DISCORD_TOKEN`           | Token del bot                               | `MzQx...`                       |
| `DISCORD_USER_ID`         | ID del usuario que debe responder           | `123456789012345678`           |
| `DISCORD_ALERT_CHANNEL_ID`| ID del usuario que recibirá la alerta       | `987654321098765432`           |
| `MENSAJE_DIARIO`          | Mensaje que se envía cada 48 horas          | `Contesta este mensaje con Lycoris.` |
| `MENSAJE_ALERTA`          | Mensaje de alerta si no hay respuesta       | `⚠️ No ha respondido en 48 horas.` |
| `PALABRA_CLAVE`           | Palabra clave que resetea el contador       | `lycoris`                       |

---

## 📥 Instalación de dependencias

en el terminal de replit colocar:
pip install -r requirements.txt

O simplemente:

pip install discord.py


## Run 

- En replit habra un .replit, dentro de este se puede cambiar el parametro de que quiere que se ejecute, el comando de ejecución es python3 "Nombre archivo".py

desde el .replit deberia quedar de la siguiente forma: 

Ej:

run = "python3 mensajeAutomatico.py"



