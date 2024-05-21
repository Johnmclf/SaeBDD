import streamlit as st
import pandas as pd
import json

uploaded_file = st.file_uploader("Choisissez un fichier JSON", type="json")

if uploaded_file is not None:
    data = json.load(uploaded_file)
    df = pd.DataFrame(data)
    st.write(df)
