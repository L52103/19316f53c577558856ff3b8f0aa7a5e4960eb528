#  Bot de Recordatorio y Verificación por Discord

Este bot envía un mensaje privado **cada 48 horas** a un usuario específico y espera una respuesta con una palabra clave.  
Si no recibe respuesta dentro del tiempo límite, **se envía una alerta a otra persona o canal**.  
Ideal para chequeos periódicos, recordatorios personales o sistemas de bienestar.

---

##  ¿Qué hace este bot?

- Envía un **mensaje privado automático** cada 48 horas a un usuario específico.
- Espera una respuesta con una palabra clave .
- Si no hay respuesta en ese plazo, **envía una alerta** a otro usuario o canal.
- Si se responde correctamente, se reinicia el temporizador.
- ⚠ **Todos los usuarios involucrados deben estar en el mismo servidor que el bot**.

---

##  Requisitos

- Cuenta en [Discord](https://discord.com/)
- Servidor de Discord donde esté el bot y los usuarios involucrados
- Cuenta en [Render](https://render.com)
- Código fuente de este repositorio (ya incluido)

---

##  Paso 1: Crear el Bot en Discord

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Haz clic en **"New Application"** y ponle un nombre.
3. En el menú lateral, selecciona **Bot** → **Add Bot**
4. Activa la opción **MESSAGE CONTENT INTENT** en *Privileged Gateway Intents*
5. Copia el **TOKEN del bot** (lo usarás luego en Render)

###  Invitar el bot a tu servidor

1. Ve a la sección **OAuth2 → URL Generator**
2. Marca los siguientes scopes:
   - `bot`
   - `applications.commands`
3. En "Bot Permissions", selecciona:
   - `Send Messages`
   - `Read Message History`
   - `View Channels`
4. Copia la URL generada, pégala en tu navegador e invita el bot a tu servidor

---

##  Paso 2: Configurar Variables de Entorno

Render permite definir variables de entorno para configurar el bot sin modificar el código.

| Clave                       | Descripción                                                | Ejemplo                              |
|----------------------------|------------------------------------------------------------|--------------------------------------|
| `DISCORD_TOKEN`            | Token del bot de Discord                                   | `MzQx...`                            |
| `DISCORD_USER_ID`          | ID del usuario que debe responder                          | `12345645678.......`                |
| `DISCORD_ALERT_CHANNEL_ID` | ID del canal o usuario que recibirá la alerta              | `98765432109.......`                |
| `MENSAJE_DIARIO`           | Mensaje que se envía cada 48 horas                         | `Contesta este mensaje con ........`|
| `MENSAJE_ALERTA`           | Mensaje enviado si no hay respuesta en 48 horas            | `⚠️ No ha respondido en 48 horas.`   |
| `PALABRA_CLAVE`            | Palabra clave que reinicia el contador                     | `palabra`                            |

> Puedes obtener IDs activando el **modo desarrollador** en Discord (Configuración → Avanzado).

---

##  Paso 3: Desplegar en Render

1. Inicia sesión en (https://render.com)
2. Haz clic en **New Web Service**
3. Selecciona **"Deploy from Git repository"** y elige este repositorio
4. Completa los siguientes campos:

###  Configuración general

- **Name**: `bot-recordatorio` (o el nombre que prefieras)
- **Environment**: `Python`
- **Build Command**:
  ```bash
  pip install -r requirements.txt

###  Variables de entorno

Agrega todas las variables mencionadas anteriormente en la sección **Environment > Environment Variables** de tu servicio en Render.

---

### Instance Type

- Puedes usar el plan **Free** si no necesitas disponibilidad 24/7.
- Para uso continuo o profesional, considera un plan de pago (**Starter** o superior).

Una vez completado todo, haz clic en **Create Web Service** y Render comenzará a construir y ejecutar el bot.

---

### Confirmar que Funciona

En los logs de Render deberías ver una línea similar a:

- El bot enviará automáticamente el mensaje de chequeo al usuario definido.
- Si el usuario responde correctamente con la palabra clave, se reinicia el temporizador.
- Si no lo hace, después de 48 horas se enviará una alerta al destinatario configurado.

---

### Extras

Puedes modificar el intervalo del temporizador en el código cambiando esta línea:

```python
@tasks.loop(hours=48)

