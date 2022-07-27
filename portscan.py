import streamlit as st
import menu
import nmp
st.set_page_config(layout="wide")
#executed the menubar and hide other functionality
menu.hide()
# NMAP
#st.title("NMAP Scanner")
nmp.app()

