import streamlit as st
import pandas as pd
from datetime import datetime
from euromillions_data import get_euromillions_data  # Fonction fictive pour obtenir les données

# Fonction fictive pour obtenir les données de l'EuroMillions depuis octobre 2009
def get_euromillions_data():
    # Ici tu devrais inclure la logique pour obtenir les données depuis ta source (API, fichier CSV, base de données, etc.)
    # Pour cet exemple, je vais juste simuler quelques données
    data = [
        {"date": "2024-06-10", "num_1": 3, "num_2": 7, "num_3": 12, "num_4": 21, "num_5": 36, "etoile_1": 4, "etoile_2": 8},
        {"date": "2024-06-07", "num_1": 5, "num_2": 14, "num_3": 19, "num_4": 23, "num_5": 30, "etoile_1": 3, "etoile_2": 9},
        # Ajoute d'autres données ici
    ]
    return data

# Obtiens les données de l'EuroMillions
data = get_euromillions_data()

# Création du DataFrame
df = pd.DataFrame(data)

# Convertir la colonne 'date' en format datetime
df['date'] = pd.to_datetime(df['date'])

# Affichage de l'application Streamlit
st.title("Historique des numéros de l'EuroMillions depuis octobre 2009")

# Affichage du DataFrame
st.write(df)
