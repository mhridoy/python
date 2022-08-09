import requests as re
from sys import argv
import streamlit as st

import urllib.request
import json

def app():
    text = st.text_input("Enter your IP address" )
    if(st.button("Submit")):
        ip = IP
        st.write(IP)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("IP Details : Location")
            result = re.get('http://ip-api.com/json/',ip)
            st.write(result.json())    

        with col2:

            st.info ("IP= Residential or Hosting")
            response = urllib.request.Request("http://v2.api.iphub.info/ip/{}".format(ip))
            response.add_header("X-Key", "MTgxMzM6N2o0Y3BDSGdnRGVoRFJXazExS2RxVkZ2cXlnbFJEQnQ=")

            try:
                response = json.loads(urllib.request.urlopen(response).read().decode())
                st.write(response)
            except:
                st.write("HTTP 403")
        with col3:
            st.warning ("Port Scanning Result")
            st.text("Under construction")
	

else: 
	print("No input")
    
