import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    KEY_BLOB_STORAGE = os.getenv("")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("")
    CONTAINER_NAME = os.getenv("")
    ENDPOINT_DOCUMENT_INTELLIGENCE = os.getenv("")
    KEY_DOCUMENT_INTELLIGENCE = os.getenv("")
