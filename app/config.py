import os

from dotenv import load_dotenv

load_dotenv()


OR_API_KEY = os.getenv("OR_API_KEY")
MODEL = os.getenv("MODEL", "openai/gpt-oss-20b:free")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")