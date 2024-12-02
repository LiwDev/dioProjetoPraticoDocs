import streamlit as st
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import  DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utills.config import Config

def analize_credit_card(card_url):
    try:
         doc_intelligence_client = DocumentIntelligenceClient(
        endpoint=Config.ENDPOINT, credential=AzureKeyCredential(Config.KEY)
         )
         request_url = AnalyzeDocumentRequest(url_source=card_url)
         card_info = doc_intelligence_client.begin_analyze_document("prebuilt-creditCard",request_url)
         result= card_info.result()
         data =[]
         for document in result.documents:
           fields = document.get("fields",{})

           record = { 
             'card_name': fields.get("CardHolderName",{}).get("content"),
             'card_number': fields.get("CardNumber",{}).get("content"),
             'expiry_date': fields.get("ExpirationDate",{}).get("content"),
             'bank_name': fields.get("IssuingBank",{}).get("content")

             }
           data.append(record)
         # Convertendo os dados para um DataFrame do Pandas 
           df = pd.DataFrame(data) 
          # Exibindo a tabela no Streamlit
         
           return st.table(df)
    except Exception as ex:
        st.write(f"erro na extração de dados da imagem:{ex}")
    
        return None
