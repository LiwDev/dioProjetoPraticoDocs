import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utills.config import Config
def blob_upload(file,fileName):
     try:
        print("Azure Blob Storage")
        st.write("Azure Blob Storage ")
        varBlobServiceClient = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        varBlobClient = varBlobServiceClient.get_blob_client(container=Config.CONTAINER_NAME,blob=fileName)
        varBlobClient.upload_blob(file,overwrite=True)
        return varBlobClient.url
   

     except Exception as ex:
        print('Exception:')
        print(ex)
        st.write("Exception: imagem não enviada para o Azure Blob Storage")
        st.write(ex)
        return None