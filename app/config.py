import os
from dotenv import load_dotenv

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
HINDSIGHT_PROJECT_ID = os.getenv("HINDSIGHT_PROJECT_ID")