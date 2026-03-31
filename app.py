# versión mínima del chat para poder probar el agente de extremo a extremo.

import streamlit as st
from services.agent import BIAgent

st.set_page_config(page_title="BI Agent MVP", page_icon="📊", layout="wide")      # onfigura la página de Streamlit

st.title("📊 BI Agent MVP")
st.write("Haz una pregunta de negocio sobre tu modelo de Power BI.")

if "agent" not in st.session_state:                               # guarda una instancia del agente dentro de la sesión del usuario.
    st.session_state.agent = BIAgent()

if "chat_history" not in st.session_state:                        # Guarda el historial visible del chat.
    st.session_state.chat_history = []

user_input = st.chat_input("Escribe tu pregunta aquí...")          # cuadro donde el usuario escribe su pregunta.

if user_input:                                                            # al escribir, se guarda el mensaje, se llama al agente, se guarda la respuesta y se muestra el historial en pantalla
    st.session_state.chat_history.append(("user", user_input))

    response = st.session_state.agent.ask(user_input)

    st.session_state.chat_history.append(("assistant", response))

for role, message in st.session_state.chat_history:                         # Recorre el historial y pinta cada mensaje con formato de chat.
    with st.chat_message(role):
        st.markdown(message)