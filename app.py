import streamlit as st
import pandas as pd
import numpy as np
import json

message = st.text_input('Entrez votre message ici')

if message:
    st.write('Vous avez écrit : ', message)


if message:
    with open(message, 'r') as f:
        data = json.load(f)
        df = pd.DataFrame(data)
        st.write(df)
