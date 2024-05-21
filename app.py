import streamlit as st
import pandas as pd
import numpy as np
import json

#recuperer le tableau grace a un fichier 
#modifier a partir d'un numero de ligne (exemple ligne 159)
#modifier a partir d'un sting (exemple lio retourn lion,lionne,...)

#Simplifier la modification 
#permettre de rajouter des donnees a la fin


# Ouvrir le fichier JSON et charger les données
with open('test.json', 'r') as f:
    data = json.load(f)

# Convertir les données en DataFrame
df = pd.DataFrame(data)

st.write(df)

#normalement on touve la ligne on la modifie et on le renvoie 
