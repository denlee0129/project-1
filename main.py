import os
from dotenv import load_dotenv
load_dotenv()
app_name = os.getenv("APP_NAME")
api_key = os.getenv("API_KEY")
if app_name and api_key:
    print(f"App Name: {app_name}")
    print(f"Api Key loaded: {bool(api_key)}")
else:
    print("Please check your .env file.")