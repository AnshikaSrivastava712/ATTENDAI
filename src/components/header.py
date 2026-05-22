import streamlit as st
import base64
from pathlib import Path

def get_base64_of_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def header_home():
    img_base64 = get_base64_of_image("logo.jpg")
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='data:image/jpeg;base64,{img_base64}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>ATTENDAI</h1>
        </div>   
    """, unsafe_allow_html=True)

def header_dashboard():
    img_base64 = get_base64_of_image("logo.jpg")
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='data:image/jpeg;base64,{img_base64}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>ATTENDAI</h2>
        </div>   
    """, unsafe_allow_html=True)