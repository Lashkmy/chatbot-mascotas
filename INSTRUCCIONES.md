# Asistente de Cuidado de Mascotas — Guía rápida

## 1. Conseguir tu API key (gratis)
1. Ve a https://aistudio.google.com
2. Inicia sesión con tu cuenta de Google
3. Haz clic en "Get API key" y créala
4. Copia esa key

## 2. Configurar el proyecto en tu computador
1. Instala Python si no lo tienes: https://www.python.org/downloads/
2. Abre una terminal en esta carpeta y crea un entorno virtual:
   ```
   python -m venv venv
   ```
3. Actívalo:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Instala las librerías:
   ```
   pip install -r requirements.txt
   ```
5. Renombra `.env.example` a `.env` y pega tu API key real ahí dentro.

## 3. Probarlo en tu computador
```
streamlit run app.py
```
Se abrirá una pestaña en tu navegador con el chatbot funcionando.

## 4. Subirlo a internet (Streamlit Community Cloud, gratis)
1. Crea un repositorio en GitHub y sube estos archivos (NO subas el .env, solo el .env.example)
2. Ve a https://share.streamlit.io e inicia sesión con GitHub
3. Selecciona tu repositorio y el archivo `app.py`
4. En "Advanced settings" → "Secrets", pega:
   ```
   GOOGLE_API_KEY = "tu_api_key_real_aqui"
   ```
5. Dale a "Deploy" — en unos minutos tendrás una URL pública para tu documento y video.

## Ideas para probar el chatbot
- "¿Cada cuánto debo bañar a mi perro?"
- "¿Qué frutas puede comer un gato?"
- "Mi perro no quiere comer, ¿qué hago?"
- "¿Cómo sé si mi mascota tiene fiebre?"

## Para tu documento y reflexión
Anota qué dificultades tuviste (ej. errores al instalar, límites de la API,
ajustar el system prompt para que responda mejor) — eso es justo lo que
pide el entregable de Trello y el documento APA.
