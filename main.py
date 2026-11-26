import os
import sys
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")

if not app_name or not api_key:
    if not app_name:
        print("Error: APP_NAME is missing")
    if not api_key:
        print("Error: API_KEY is missing")
    sys.exit(1)
else:
    print(f"APP_NAME: {app_name}")
    print(f"API_KEY loaded: {bool(api_key)}")