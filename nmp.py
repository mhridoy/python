import socket
import streamlit as st

def app():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    target = st.text_input("Enter Target IP: ")
    portNumber = st.text_input("Port Number")
    submit = st.button("Click me!")
    if submit:
       # port_range = st.slider('Set the port range', 1, 22, 100)
        def scanner(port):
            try:
                sock.connect((target, port))
                return True
            except:
                return False
        if scanner(portNumber):
            st.write('[*] Port', portNumber, '/tcp','is open')
        # for portNumber in range(1,port_range):
        #     st.write("Scanning port", portNumber)
        #     if scanner(portNumber):
        #         st.write('[*] Port', portNumber, '/tcp','is open')
