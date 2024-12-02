from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def detect_credit_card_info(card_url):
    try:
        credential = AzureKeyCredential("SUBSCRIPTION_KEY")
        document_intelligence_client = DocumentIntelligenceClient("ENDPOINT", credential)
        
        card_info = document_intelligence_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
        result = card_info.result()
    except Exception as ex:
        return None
    
    for document in result.documents:
        fields = document.get("fields", {})

        return{
            "card_name": fields.get('CardHolderName', {}).get('content'),
            "card_number": fields.get('CardNumber', {}).get('content'),
            "expiry_date": fields.get('ExpirationDate', {}).get('content'),
            "bank_name": fields.get('IssuingBank', {}).get('content')
        }
    