import streamlit as st

# Configuración de página
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
    .capsule-card {
        background-color: #EBF3FA;
        border-left: 5px solid #005A9C;
        padding: 10px;
        margin-top: 10px;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown("""
    <div class="main-header">
        <h2>🤖 SASSUR-Bot Amanecer</h2>
        <p>Asistente Virtual 24/7 de Salud Digital | CESFAM Amanecer</p>
    </div>
""", unsafe_allow_html=True)

# Base de conocimiento (Respuestas inteligentes)
RESPUESTAS = {
    "preventivos": """📌 **¿CÓMO VERIFICAR CONTROLES PREVENTIVOS (PAP, EMPA, CRÓNICOS)?**
1. Al abrir la ficha del paciente en SASSUR, ve a la pestaña **'Historial de Prestaciones'**.
2. Revisa la fecha de emisión del último **PAP** (vigencia 3 años) o **EMPA** (vigencia 1 año).
3. Si está vencido o no figura, haz clic en **'Generar Orden de Examen / Citación'**.

🎬 **Cápsula Educativa:** [Ver Video 1: Verificación de Preventivos en SASSUR (45s)](#)""",

    "doble registro": """📌 **PASO A PASO PARA EL DOBLE REGISTRO (SASSUR + EXCEL):**
1. Guarda la atención normalmente en SASSUR.
2. Presiona el botón **'Copiar Resumen de Atención'** (al pie de la pantalla).
3. Abre la planilla *"Tarjetero Municipal Amanecer.xlsx"* y presiona **Ctrl + V**.
4. La plantilla cruzará automáticamente el RUT con los datos de FONASA sin volver a digitar antecedentes.

🎬 **Cápsula Educativa:** [Ver Video 2: Llenado de Tarjetero Excel en 60s](#)""",

    "sector": """📌 **IDENTIFICACIÓN DE SECTOR TERRITORIAL:**
1. En el encabezado de la ficha del usuario en SASSUR, ubica el campo **'Sector de Inscripción'**.
2. Verás la asignación: **Sector Rojo**, **Sector Azul**, **Sector Verde** o **CECOSF Las Quilas**.
3. Si requiere derivación interna o seguimiento por equipo de cabecera, selecciona la agenda correspondiente a su sector.

🎬 **Cápsula Educativa:** [Ver Video 3: Identificación por Sector (40s)](#)""",

    "contingencia": """📌 **PROTOCOLO DE CONTINGENCIA Y DESBLOQUEO RÁPIDO:**
1. **Si SASSUR se congela:** Presiona **F5** o **Ctrl + Shift + R** para recargar manteniendo el borrador.
2. **Si cae la red:** Utiliza el **Formulario Físico de Contingencia APS** ubicado en tu escritorio y registra en bloque al volver el sistema.
3. **Falla en Tótem de Farmacia:** Activa la entrega de números manuales codificados por color según el Sector.

🎬 **Cápsula Educativa:** [Ver Video 4: Desbloqueo F5 y Protocolo de Contingencia (30s)](#)""",

    "ciberseguridad": """🛡️ **REGLAS DE CIBERSEGURIDAD Y RESPONSABILIDAD LEGAL:**
1. **Las claves son 100% personales e indelegables:** Cada ingreso queda registrado con tu RUT e IP.
2. **Prohibición de acceso sin motivo clínico:** La ley sanciona el ingreso a fichas no autorizadas.
3. **Alumnos en práctica:** Deben usar exclusivamente sus credenciales asignadas por convenio.

🎬 **Cápsula Educativa:** [Ver Video 5: Ciberseguridad en Salud Digital (50s)](#)"""
}

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Soy **SASSUR-Bot**. Escribe tu duda o selecciona una de las opciones rápidas de abajo para ayudarte de inmediato:"}
    ]

# Mostrar historial
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Botones de acceso rápido
st.write("---")
st.write("**🔍 Accesos Rápidos Frecuentes:**")
col1, col2 = st.columns(2)

prompt_button = None
with col1:
    if st.button("🔴 Alertas Preventivas (PAP/EMPA)"):
        prompt_button = "preventivos"
    if st.button("📊 Doble Registro (SASSUR + Excel)"):
        prompt_button = "doble registro"

with col2:
    if st.button("⚡ SASSUR Congelado / Caída de Tótem"):
        prompt_button = "contingencia"
    if st.button("🛡️ Ciberseguridad y Claves"):
        prompt_button = "ciberseguridad"

# Entrada de texto del usuario
user_input = st.chat_input("Escribe tu pregunta sobre SASSUR...")

prompt = prompt_button or user_input

if prompt:
    # Registrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Lógica de respuesta inteligente
    p_lower = prompt.lower()
    respuesta = None

    for clave, contenido in RESPUESTAS.items():
        if clave in p_lower:
            respuesta = contenido
            break

    if not respuesta:
        respuesta = """🤖 No encontré una respuesta exacta para esa consulta, pero puedes probar con estas opciones frecuentes:
- Escribir **'preventivos'** para saber cómo revisar PAP o EMPA.
- Escribir **'doble registro'** para copiar datos a Excel.
- Escribir **'contingencia'** si el sistema se congeló.
- O contactar al referente informático local del CESFAM al anexo **4012**."""

    # Registrar y mostrar respuesta
    st.session_state.messages.append({"role": "assistant", "content": respuesta})
    st.chat_message("assistant").write(respuesta)
