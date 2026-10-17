import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="SASSUR-Bot Amanecer",
    page_icon="🤖",
    layout="centered"
)

# Estilos visuales institucionales
st.markdown("""
    <style>
    .main-header {
        background-color: #005A9C;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown("""
    <div class="main-header">
        <h2>🤖 SASSUR-Bot Amanecer</h2>
        <p>Asistente Virtual 24/7 de Salud Digital | CESFAM Amanecer</p>
    </div>
""", unsafe_allow_html=True)

# Base de conocimiento con videos enlazados
RESPUESTAS = {
    "preventivos": {
        "texto": """📌 **¿CÓMO VERIFICAR CONTROLES PREVENTIVOS (PAP, EMPA)?**
1. Al abrir la ficha del paciente en SASSUR, ve a la pestaña **'Historial de Prestaciones'**.
2. Revisa la fecha del último **PAP** (vigencia 3 años) o **EMPA** (vigencia 1 año).
3. Si está vencido o no figura, haz clic en **'Generar Orden de Examen / Citación'**.

🎬 **Cápsula Educativa en Video:**""",
        "video": "https://www.youtube.com/watch?v=8EbCVH21ch0"
    },

    "doble registro": {
        "texto": """📌 **PASO A PASO PARA EL DOBLE REGISTRO (SASSUR + EXCEL):**
1. Guarda la atención normalmente en SASSUR.
2. Presiona el botón **'Copiar Resumen de Atención'** al pie de la pantalla.
3. Abre la planilla *\"Tarjetero Municipal Amanecer.xlsx\"* y presiona **Ctrl + V**.
4. La planilla vinculará automáticamente el RUT con los datos de FONASA.

🎬 **Cápsula Educativa en Video:**""",
        "video": "https://www.youtube.com/watch?v=8EbCVH21ch0"
    },

    "contingencia": {
        "texto": """📌 **PROTOCOLO DE CONTINGENCIA Y DESBLOQUEO RÁPIDO:**
1. **Si SASSUR se congela:** Presiona **F5** o la combinación **Ctrl + Shift + R** para recargar la pantalla.
2. **Si cae la red:** Utiliza el **Formulario Físico de Contingencia APS** ubicado en tu escritorio.
3. **Falla en Tótem de Farmacia:** Entrega de números manuales codificados por color según el Sector.

🎬 **Cápsula Educativa en Video:**""",
        "video": "https://www.youtube.com/watch?v=8EbCVH21ch0"
    },

    "ciberseguridad": {
        "texto": """🛡️ **REGLAS DE CIBERSEGURIDAD Y RESPONSABILIDAD LEGAL:**
1. **Las claves son 100% personales e indelegables:** Cada ingreso queda registrado con tu RUT e IP.
2. **Prohibición de acceso no autorizado:** La ley sanciona el ingreso a fichas sin motivo clínico.
3. **Alumnos en práctica:** Deben usar exclusivamente sus credenciales asignadas.

🎬 **Cápsula Educativa en Video:**""",
        "video": "https://www.youtube.com/watch?v=8EbCVH21ch0"
    }
}

# Etiquetas bonitas para mostrar cuando el usuario pulsa botones
BUTTON_LABELS = {
    "preventivos": "🔴 Alertas Preventivas (PAP/EMPA)",
    "doble registro": "📊 Doble Registro (SASSUR + Excel)",
    "contingencia": "⚡ SASSUR Congelado / Desbloqueo",
    "ciberseguridad": "🛡️ Ciberseguridad y Claves"
}

# Historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy **SASSUR-Bot**. Escribe tu duda o selecciona una de las opciones rápidas de abajo para ver la solución y la cápsula en video:"}
    ]

# Mostrar historial de mensajes (incluye video si el mensaje tiene clave 'video')
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        # Si el mensaje incluye un video (key 'video'), mostrarlo
        if msg.get("video"):
            st.video(msg["video"])

# Botones de acceso rápido
st.write("---")
st.write("**🔍 Accesos Rápidos con Video:**")
col1, col2 = st.columns(2)

prompt_button = None
with col1:
    if st.button(BUTTON_LABELS["preventivos"]):
        prompt_button = "preventivos"
    if st.button(BUTTON_LABELS["doble registro"]):
        prompt_button = "doble registro"

with col2:
    if st.button(BUTTON_LABELS["contingencia"]):
        prompt_button = "contingencia"
    if st.button(BUTTON_LABELS["ciberseguridad"]):
        prompt_button = "ciberseguridad"

# Entrada de texto del usuario
user_input = st.chat_input("Escribe tu pregunta sobre SASSUR...")
prompt = prompt_button or user_input

if prompt:
    # Cuando el trigger viene de un botón, mostrar la etiqueta bonita al historial de usuario
    user_display = BUTTON_LABELS.get(prompt, prompt)
    st.session_state.messages.append({"role": "user", "content": user_display})
    with st.chat_message("user"):
        st.write(user_display)

    p_lower = prompt.lower()
    respuesta_data = None

    for clave, data in RESPUESTAS.items():
        if clave in p_lower:
            respuesta_data = data
            break

    if respuesta_data:
        # Guardar respuesta con la misma clave 'video'
        msg_dict = {
            "role": "assistant",
            "content": respuesta_data["texto"],
            "video": respuesta_data.get("video")
        }
        st.session_state.messages.append(msg_dict)

        with st.chat_message("assistant"):
            st.write(respuesta_data["texto"])
            if respuesta_data.get("video"):
                st.video(respuesta_data["video"])
    else:
        respuesta_gen = """🤖 No encontré una respuesta exacta para esa consulta. Puedes probar con:
- Escribir **'preventivos'** para ver el video sobre PAP y EMPA.
- Escribir **'doble registro'** para la guía de Excel.
- O contactar al referente informático local al anexo **4012**."""
        st.session_state.messages.append({"role": "assistant", "content": respuesta_gen})
        with st.chat_message("assistant"):
            st.write(respuesta_gen)
