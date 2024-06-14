import streamlit as st
import pandas as pd

def lire_csv_vers_dataframe(nom_fichier, separateur=';'):
    try:
        # Lecture du fichier CSV et création du DataFrame
        dataframe = pd.read_csv(nom_fichier, sep=separateur)
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

    separateur = ';'  # Séparateur par défaut

    if fichier is not None:
        separateur = st.text_input("Entrez le séparateur utilisé dans le fichier CSV (par défaut ';')", ';')

        # Lecture du fichier CSV et affichage du DataFrame
        dataframe = lire_csv_vers_dataframe(fichier, separateur)
        if dataframe is not None:
            st.success("Fichier chargé avec succès ! Voici les données :")
            st.write(dataframe)

if __name__ == "__main__":
    main()
