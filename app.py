import streamlit as st
import pandas as pd

def lire_csv_vers_dataframe(nom_fichier):
    try:
        # Lecture du fichier CSV et création du DataFrame
        dataframe = pd.read_csv(nom_fichier)
        return dataframe
    except FileNotFoundError:
        st.error("Le fichier spécifié est introuvable.")
        return None
    except Exception as e:
        st.error("Une erreur s'est produite lors de la lecture du fichier :", e)
        return None

def main():
    st.title("Chargement de fichier CSV dans DataFrame")

    # Widget pour uploader le fichier CSV
    fichier = st.file_uploader("Uploader un fichier CSV", type=['csv'])

    if fichier is not None:
        # Lecture du fichier CSV et affichage du DataFrame
        dataframe = lire_csv_vers_dataframe(fichier)
        if dataframe is not None:
            st.success("Fichier chargé avec succès ! Voici les premières lignes :")
            st.write(dataframe.head())

if __name__ == "__main__":
    main()
