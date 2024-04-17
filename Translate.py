import streamlit as st
from googletrans import Translator

st.header("Machine Translator Assignment")

text=st.text_area("Enter the text",value="")
select=st.selectbox("Which language do you wish to translate this text to",('Malayalam','Hindi','Tamil','French'))

if st.button('Translate'):
    translator=Translator()
    translation=translator.translate(text,dest=select.lower())
    st.write(translation.text)