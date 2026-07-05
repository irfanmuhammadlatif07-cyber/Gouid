import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Konfigurasi halaman (harus jadi perintah st. paling pertama)
st.set_page_config(
    page_title="GoPay Insight Dashboard",
    page_icon="📊",
    layout="wide"
)

# Menyembunyikan elemen bawaan Streamlit (menu titik tiga, footer "Made with Streamlit",
# dan toolbar/header di bagian atas) supaya tampilan bersih seperti dashboard.html aslinya
hide_streamlit_chrome = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden; height: 0; position: fixed;}
    div[data-testid="stDecoration"] {visibility: hidden; height: 0; position: fixed;}
    div[data-testid="stStatusWidget"] {visibility: hidden; height: 0; position: fixed;}
    .block-container {padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;}
    </style>
"""
st.markdown(hide_streamlit_chrome, unsafe_allow_html=True)

# Membaca file HTML dashboard yang sudah dibuat
html_path = Path(__file__).parent / "dashboard.html"
html_content = html_path.read_text(encoding="utf-8")

# Menampilkan HTML dashboard di dalam Streamlit
# height diatur cukup besar + scrolling=True karena dashboard punya banyak konten & tab
components.html(html_content, height=2400, scrolling=True)
