import streamlit as st

st.title ("Rabsa's NID ")
st.text("To Download, click on Download Button")

with open("NID_RABSA.pdf", "rb") as file:
    btn = st.download_button(
            label="Download pdf",
            data=file,
            file_name="NID.pdf",
            
          )