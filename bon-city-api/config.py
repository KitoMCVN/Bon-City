import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MINECRAFT_SERVER_IP = os.getenv('MINECRAFT_SERVER_IP')
