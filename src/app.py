import streamlit as st
import pandas as pd
from services.blobService import blob_upload
from services.cred_card_service import analize_credit_card

def configure_interface():
    st.title("Upload de Arquivo Dio - Desafio 1 - Azure - Fake Doc")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        file_Name = uploaded_file.name
        blob_url = blob_upload(file=uploaded_file,fileName=file_Name)
        if blob_url:
            st.write(f"Arquivo {file_Name} enviado com sucesso para o Azure Blob Storage")
            credit_card_info= analize_credit_card(blob_url)
            print(credit_card_info)
            show_image_and_validation(blob_url,credit_card_info)
        else:
            st.write(f"Arquivo {file_Name} \n enviado com sucesso para o Azure Blob Storage")
def show_image_and_validation(blob_url,credit_card_info):
    st.image(blob_url,use_container_width=True)
    st.markdown("<p style='color:green;'>imagem enviada</p>", unsafe_allow_html=True)
    
    if credit_card_info and isinstance(credit_card_info, list) and len(credit_card_info) > 0:
       st.write(f"informações do cartão de credito encontradas: ")
       
       st.markdown(f"<h1 style='color:green;'>Cartão Valido </h1>")
       data =[]
       for document in credit_card_info.documents:
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
           styled_df = df.style.applymap(lambda x: 'color: red;' if x is None else 'color: green;')
          # Exibindo a tabela no Streamlit
         
           st.table(styled_df)
       
       else:
            st.markdown(f"<h1 style='color:red;'>Cartão Invalido </h1>", unsafe_allow_html=True)
            st.write("este não é um cartão valido")
if __name__ == "__main__":
    configure_interface()
