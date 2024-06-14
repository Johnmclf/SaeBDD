import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def extract_numbers(text):
    """
    Fonction pour extraire les numéros de l'EuroMillions à partir du texte.
    """
    # Séparer le texte en lignes
    lines = text.split('\n')
    numbers = []
    for line in lines:
        # Rechercher les lignes contenant les numéros de l'EuroMillions
        if "EuroMillions - Tirage" in line:
            numbers_line = line.split(":")[-1].strip()
            numbers.extend(numbers_line.split(" "))
    return numbers

# URL de la page des résultats
url = "https://www.lesbonsnumeros.com/loto/resultats/tirages.htm"

# Faire une requête pour obtenir le contenu de la page
response = requests.get(url)
if response.status_code != 200:
    st.error("Impossible de récupérer les données du site.")
else:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Trouver tous les paragraphes contenant les informations de tirage
    draw_paragraphs = soup.find_all('p')

    # Initialiser une liste pour stocker les données de tous les tirages
    all_draws_data = []

    # Parcourir chaque paragraphe
    for paragraph in draw_paragraphs:
        # Extraire le texte du paragraphe
        paragraph_text = paragraph.get_text()
        # Extraire la date du tirage (si disponible)
        if "EuroMillions - Tirage du " in paragraph_text:
            draw_date = paragraph_text.split(" - ")[1].split(":")[0]
            draw_numbers = extract_numbers(paragraph_text)
            draw_data = {
                'Date': draw_date,
                'Numéros': ' '.join(draw_numbers[:5]),  # Les cinq premiers sont les numéros principaux
                'Étoiles': ' '.join(draw_numbers[5:])  # Les étoiles
            }
            all_draws_data.append(draw_data)

    # Convertir la liste de données en DataFrame pandas
    df = pd.DataFrame(all_draws_data)

    # Afficher le DataFrame avec Streamlit
    st.title("Résultats de l'EuroMillions")
    st.write("Liste des tirages de l'EuroMillions depuis novembre 2009")
    st.dataframe(df)
