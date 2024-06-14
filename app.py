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

def compter_chiffres(dataframe, colonnes):
    comptages = {}
    for chiffre in range(1, 51):  # Boucle de 1 à 50
        total = 0
        for colonne in colonnes:
            total += (dataframe[colonne] == chiffre).sum()
        comptages[chiffre] = total
    return comptages

def main():
    st.title("Analyse des chiffres dans les colonnes sélectionnées")

    # Widget pour uploader le fichier CSV
    fichier = st.file_uploader("Uploader un fichier CSV", type=['csv'])

    separateur = ';'  # Séparateur par défaut

    if fichier is not None:
        separateur = st.text_input("Entrez le séparateur utilisé dans le fichier CSV (par défaut ';')", ';')

        # Lecture du fichier CSV
        dataframe = lire_csv_vers_dataframe(fichier, separateur)
        
        if dataframe is not None:
            st.success("Fichier chargé avec succès !")
            
            # Sélection des colonnes par l'utilisateur
            colonnes_selectionnees = st.multiselect("Sélectionnez les colonnes pour l'analyse", dataframe.columns)
            
            if colonnes_selectionnees:
                # Compter le nombre de chaque chiffre de 1 à 50 dans les colonnes sélectionnées
                comptages = compter_chiffres(dataframe, colonnes_selectionnees)
                
                # Création du DataFrame pour afficher les résultats
                df_resultats = pd.DataFrame(comptages.items(), columns=['Chiffre', 'Nombre de fois'])
                
                # Tri par ordre croissant du nombre de fois
                df_resultats = df_resultats.sort_values(by='Nombre de fois')
                
                # Affichage des résultats triés
                st.write("Nombre de chaque chiffre de 1 à 50 dans les colonnes sélectionnées (trié par ordre croissant) :")
                st.write(df_resultats)
            else:
                st.warning("Veuillez sélectionner au moins une colonne pour l'analyse.")

if __name__ == "__main__":
    main()
