import streamlit as st
import pandas as pd
import json

# Permettre à l'utilisateur de télécharger un fichier
uploaded_file = st.file_uploader("Choisissez un fichier JSON", type="json")

if uploaded_file is not None:
    # Lire les données du fichier
    data = json.load(uploaded_file)

    # Convertir les données en DataFrame
    df = pd.DataFrame(data)

    # Afficher le DataFrame original
    st.write('DataFrame original :')
    st.write(df)

    # Boucle pour permettre à l'utilisateur de faire plusieurs modifications
    while True:
        # Demander à l'utilisateur s'il veut faire une modification
        modify = st.button('Voulez-vous faire une modification ?')

        if modify:
            # Demander à l'utilisateur d'entrer l'index de la ligne à modifier
            row_index = st.number_input('Entrez l\'index de la ligne à modifier', min_value=0, max_value=len(df)-1, step=1)

            # Demander à l'utilisateur d'entrer le nom de la colonne à modifier
            column_name = st.text_input('Entrez le nom de la colonne à modifier')

            # Demander à l'utilisateur d'entrer la nouvelle valeur
            new_value = st.text_input('Entrez la nouvelle valeur')

            if st.button('Appliquer les modifications'):
                # Modifier la valeur dans le DataFrame
                df.loc[row_index, column_name] = new_value

                # Afficher le DataFrame modifié
                st.write('DataFrame modifié :')
                st.write(df)
        else:
            break
