import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("LLM_BASE_URL")
API_KEY = os.getenv("LLM_API_KEY", "none")
MODEL = os.getenv("LLM_MODEL", "Qwen3.8-Flash-Next")