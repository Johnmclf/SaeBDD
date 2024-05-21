import streamlit as st
import pandas as pd
import json
import SessionState

# Permettre à l'utilisateur de télécharger un fichier
uploaded_file = st.file_uploader("Choisissez un fichier JSON", type="json")

if uploaded_file is not None:
    try:
        # Lire les données du fichier
        data = json.load(uploaded_file)

        # Convertir les données en DataFrame
        df = pd.DataFrame(data)

        # Afficher le DataFrame original
        st.write('DataFrame original :')
        st.write(df)

        # Utiliser SessionState pour conserver les entrées de l'utilisateur
        state = SessionState.get(row_index=0, column_name='', new_value='')

        # Demander à l'utilisateur d'entrer l'index de la ligne à modifier
        state.row_index = st.number_input('Entrez l\'index de la ligne à modifier', min_value=0, max_value=len(df)-1, step=1, value=state.row_index)

        # Demander à l'utilisateur d'entrer le nom de la colonne à modifier
        state.column_name = st.text_input('Entrez le nom de la colonne à modifier', value=state.column_name)

        # Demander à l'utilisateur d'entrer la nouvelle valeur
        state.new_value = st.text_input('Entrez la nouvelle valeur', value=state.new_value)

        if st.button('Appliquer les modifications'):
            # Si la colonne n'existe pas, la créer
            if state.column_name not in df.columns:
                df[state.column_name] = ''

            # Modifier la valeur dans le DataFrame
            df.loc[state.row_index, state.column_name] = state.new_value

            # Afficher le DataFrame modifié
            st.write('DataFrame modifié :')
            st.write(df)
    except Exception as e:
        st.write('Une erreur s\'est produite lors de la lecture du fichier JSON ou de la modification du DataFrame.')
        st.write('Détails de l\'erreur :', str(e))
