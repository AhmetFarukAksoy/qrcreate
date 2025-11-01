import streamlit as st
import pyqrcode
data=st.text_input("QR verisini giriniz")
color=st.color_picker("renk seç")
qr=pyqrcode.create(data)
boyut=st.slider("boyut seç",1,25)
qr.svg("qr.svg",scale=boyut,module_color=color)

if qr:
    st.image("qr.svg")
#pip install streamlit
#pip install pyqrcode
#pip install pypng
#pip install pysvg