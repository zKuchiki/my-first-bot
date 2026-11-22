import os 
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("API_KEY")

print(token[:4])
