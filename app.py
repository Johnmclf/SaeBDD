import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

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

# Fonction pour obtenir les dates de tirage
def get_draw_dates(start_date, end_date):
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=7)  # Ajouter une semaine entre chaque tirage
    return dates

# URL de la page des résultats
url = "https://www.lesbonsnumeros.com/loto/resultats/tirages.htm"

# Date de début (octobre 2009)
start_date = datetime(2009, 10, 1)
# Date de fin (aujourd'hui)
end_date = datetime.now()

# Obtenir les dates de tirage entre start_date et end_date
draw_dates = get_draw_dates(start_date, end_date)

# Initialiser une liste pour stocker les données de tous les tirages
all_draws_data = []

# Faire une requête pour obtenir le contenu de la page pour chaque date de tirage
for draw_date in draw_dates:
    draw_date_str = draw_date.strftime("%Y-%m-%d")
    response = requests.get(f"{url}?date={draw_date_str}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver tous les paragraphes contenant les informations de tirage
        draw_paragraphs = soup.find_all('p')

        # Parcourir chaque paragraphe
        for paragraph in draw_paragraphs:
            # Extraire le texte du paragraphe
            paragraph_text = paragraph.get_text()
            # Extraire la date du tirage (si disponible)
            if "EuroMillions - Tirage du " in paragraph_text:
                draw_numbers = extract_numbers(paragraph_text)
                draw_data = {
                    'Date': draw_date_str,
                    'Numéros': ' '.join(draw_numbers[:5]),  # Les cinq premiers sont les numéros principaux
                    'Étoiles': ' '.join(draw_numbers[5:])  # Les étoiles
                }
                all_draws_data.append(draw_data)

# Convertir la liste de données en DataFrame pandas
df = pd.DataFrame(all_draws_data)

# Afficher le DataFrame avec Streamlit
st.title("Résultats de l'EuroMillions depuis octobre 2009")
st.write("Liste des tirages de l'EuroMillions depuis octobre 2009")
st.dataframe(df)
