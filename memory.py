# El agente necesita un system prompt inicial. Este código lee el archivo .txt, devuelve todo el contenido como texto --> para meterlo en cada conversación

from config import SYSTEM_PROMPT_PATH

def load_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()
      
# El modelo no "recuerda" nada por sí mismo, así que tenemos que ir guardando el historial de la conversación para ir pasándoselo en cada llamada. Este código crea esa memoria y la va actualizando. --> guardar lo que dice el usuario, lo que responde el agente y mantiene contexto. 

def init_memory():
    return []

def add_message(memory, role, content):
    memory.append({
        "role": role,
        "content": content
    })
    return memory