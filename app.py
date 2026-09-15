import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted, GoogleAPICallError

# 1) Cargar la API key desde el archivo .env (nunca la escribas directamente en el código)
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# 2) Configurar la conexión con la API de Gemini usando tu key
genai.configure(api_key=API_KEY)

# 3) System prompt: aquí le decimos al chatbot su personalidad, su tema y sus reglas
SYSTEM_PROMPT = """
Eres un asistente experto en cuidado de mascotas (perros y gatos).
Tu trabajo es responder preguntas sobre alimentación, salud básica,
comportamiento, higiene y bienestar general de mascotas.

Reglas:
- Responde siempre en español, de forma clara, breve y amable.
- Si la pregunta es sobre un problema de salud grave o urgente,
  recomienda SIEMPRE acudir a un veterinario. No des diagnósticos médicos.
- Si no sabes algo con certeza, dilo honestamente en vez de inventar.
- Usa un tono cercano, como un amigo con experiencia en mascotas.
"""

# 4) Crear el modelo de IA, indicándole el system prompt de arriba
model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=SYSTEM_PROMPT
)

# ---------------- INTERFAZ WEB (Streamlit) ----------------

st.set_page_config(page_title="Asistente de Mascotas", page_icon="🐾")
st.title("🐾 Asistente de Cuidado de Mascotas")
st.write("Pregúntame lo que quieras sobre el cuidado de tu perro o gato.")

# 5) Streamlit "olvida" todo cada vez que la página se recarga, por eso guardamos
#    el chat y los mensajes en "session_state" (memoria de la sesión actual)
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

# 6) Volver a mostrar en pantalla los mensajes de conversaciones anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 7) Campo de texto donde el usuario escribe su pregunta
user_input = st.chat_input("Escribe tu pregunta aquí...")

if user_input:
    # Mostrar el mensaje del usuario en pantalla y guardarlo en el historial
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 8) Enviar el mensaje a Gemini y mostrar la respuesta
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = st.session_state.chat.send_message(user_input)
                answer = response.text
            except ResourceExhausted:
                # Se agotó el límite gratuito de solicitudes por minuto/día
                answer = (
                    "🐾 En este momento he recibido demasiadas preguntas seguidas "
                    "y alcancé el límite gratuito de uso. Por favor espera un "
                    "minuto y vuelve a intentarlo."
                )
            except GoogleAPICallError:
                # Cualquier otro error de la API (conexión, servidor, etc.)
                answer = (
                    "🐾 Tuve un problema para conectarme con el servicio de IA. "
                    "Intenta de nuevo en unos segundos."
                )
            st.markdown(answer)

    # Guardar la respuesta del asistente en el historial
    st.session_state.messages.append({"role": "assistant", "content": answer})
