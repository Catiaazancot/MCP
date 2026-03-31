"""En este paso centralizamos la configuración del proyecto en un solo archivo. Así separamos parámetros técnicos y credenciales del resto del código, facilitando el mantenimiento, la seguridad y los cambios futuros. """

from pathlib import Path
from dotenv import load_dotenv
import os

#localiza la carpeta raíz del proyecto 
BASE_DIR = Path(__file__).resolve().parent  

# carga las variables del archivo .env
load_dotenv(BASE_DIR / ".env")

# apunta al archivo system_prompt.txt 
SYSTEM_PROMPT_PATH = BASE_DIR / "prompts" / "system_prompt.txt"

# Variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # lee la clave desde .env
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1") # modelo por defecto, pero se puede cambiar en .env sin tocar el código