import streamlit as st


def configure_interface():
    st.title("Upload de Arquivo Dio - Desafio 1 - Azure - Fake Doc")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = ""
        
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info= ""
            show_image_and_validation(blob_url,credit_card_info)
        else:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
def show_image_and_validation(blob_url,credit_card_info):
    st.image(blob_url,caption="imagem enviada",use_column_width=True)
    
    st.write(f"informações do cartão de credito encontradas: ")
    if credit_card_info and credit_card_info["card_name"]:
       st.markdown(f"<h1 style='color:green;'>Cartão Valido <h1>")
       st.write(f"nome do titular:{credit_card_info['card_name']}")
       st.write(f"nome do titular:{credit_card_info['bank_name']}")
       st.write(f"nome do titular:{credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color:green;'>Cartão Invalido <h1>")
        st.write("este não é um cartão valido")
if __name__ == "__main__":
    configure_interface()
