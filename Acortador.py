import pyshorteners as pys
import streamlit as st

#Funcion acortadora de links
def shorten_url(url):
    s = pys.Shortener()
    shorten_url = s.tinyurl.short(url)
    return shorten_url

#Pagina web con streamlit
st.set_page_config(page_title="URL Shortener", layout="centered")
st.title("URL Shortener")
url = st.text_input("Enter the url: ")
if st.button("Generate new URL"):
    st.write("Url shortened: ", shorten_url(url))