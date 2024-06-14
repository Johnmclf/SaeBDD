import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

# URL de la page des résultats
url = "https://www.lesbonsnumeros.com/loto/resultats/tirages.htm"

# Faire une requête pour obtenir le contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver tous les tableaux de résultats
results_table = soup.find('table', {'class': 'historique'})

# Initialiser une liste pour stocker les données
data = []

# Parcourir chaque ligne du tableau
for row in results_table.find_all('tr'):
    # Initialiser un dictionnaire pour stocker les informations de chaque ligne
    row_data = {}
    cells = row.find_all('td')
    if len(cells) == 9:  # Assurer que la ligne contient les bons nombres de colonnes
        # Extraire les informations de chaque colonne
        row_data['date'] = cells[0].text.strip()
        row_data['boule_1'] = cells[1].text.strip()
        row_data['boule_2'] = cells[2].text.strip()
        row_data['boule_3'] = cells[3].text.strip()
        row_data['boule_4'] = cells[4].text.strip()
        row_data['boule_5'] = cells[5].text.strip()
        row_data['chance'] = cells[6].text.strip()
        
        # Ajouter le dictionnaire à la liste de données
        data.append(row_data)

# Convertir la liste de données en DataFrame pandas
df = pd.DataFrame(data)

# Afficher le DataFrame avec Streamlit
st.title("Résultats de l'EuroMillions")
st.write("Tableau des résultats des tirages de l'EuroMillions depuis novembre 2009")
st.dataframe(df)
