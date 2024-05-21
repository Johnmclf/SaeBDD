import streamlit as st
import pandas as pd
import numpy as np
import json

# Demander à l'utilisateur d'entrer un message
message = st.text_input('Entrez votre message ici')

# Afficher le message
st.write('Vous avez écrit : ', message)

# Ouvrir le fichier JSON et charger les données
with open(message, 'r') as f:
    data = json.load(f)

# Convertir les données en DataFrame
df = pd.DataFrame(data)

st.write(df)
