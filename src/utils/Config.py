import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("")
    KEY = os.getenv("")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("")
    CONTAINER_NAME = os.getenv("")