# Este archivo es el núcleo del MVP. Aqui se unen las piezas que hemos ido creando: la configuración, la memoria y el cliente de OpenAI. 

""" Esta clase hace 4 cosas:
    1. crea el cliente para hablar con el modelo
    2. carga el prompt del sistema
    3. inicializa la memoria conversacional
    4. expone un método ask() para enviar preguntas y recibir respuestas
"""

from openai import OpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL
from services.memory import load_system_prompt, init_memory, add_message


class BIAgent:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)            #Crea la conexión con el modelo usando la API key.
        self.system_prompt = load_system_prompt()               # Carga el comportamiento definido en el .txt.
        self.memory = init_memory()                              # Crea el historial vacío de la conversación.
        add_message(self.memory, "system", self.system_prompt)  # Añade el prompt como primer mensaje. Esto es clave porque define el rol y las reglas del agente desde el inicio.

    def ask(self, user_message: str) -> str:                      # guarda la pregunta, envia todo el historial al modelo, recoge la respuesta (tb la guarda) y la devuelve.
        add_message(self.memory, "user", user_message)

        response = self.client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=self.memory,
            temperature=0           # Se reduce variabilidad para respuestas más consistentes, precisión y repetibilidad. 
        )

        assistant_message = response.choices[0].message.content
        add_message(self.memory, "assistant", assistant_message)

        return assistant_message