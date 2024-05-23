import streamlit as st
import pandas as pd
import json

# Téléchargement du fichier JSON
uploaded_file = st.file_uploader("Choisissez un fichier JSON", type="json")

if uploaded_file is not None:
    data = json.load(uploaded_file)
    df = pd.DataFrame(data)
    st.write('DataFrame original :')
    st.write(df)

    # Initialisation de la liste des modifications
    if 'modifications' not in st.session_state:
        st.session_state.modifications = []

    # Saisie de la modification
    with st.form(key='modification_form'):
        row_index = st.number_input('Entrez l\'index de la ligne à modifier', min_value=0, max_value=len(df)-1, step=1)
        column_name = st.selectbox('Choisissez le nom de la colonne à modifier', df.columns)
        new_value = st.text_input('Entrez la nouvelle valeur')
        add_modification = st.form_submit_button('Ajouter la modification')
    
    # Ajouter la modification à la liste
    if add_modification:
        st.session_state.modifications.append((row_index, column_name, new_value))

    # Afficher la liste des modifications en attente avec des boutons pour les supprimer
    st.write('Modifications en attente :')
    for i, mod in enumerate(st.session_state.modifications):
        row_index, column_name, new_value = mod
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"Ligne {row_index}, Colonne '{column_name}', Nouvelle valeur : {new_value}")
        with col2:
            if st.button('Supprimer', key=f'delete_{i}'):
                st.session_state.modifications.pop(i)
                st.experimental_rerun()

    # Bouton pour appliquer les modifications
    if st.button('Appliquer toutes les modifications'):
        for mod in st.session_state.modifications:
            row_index, column_name, new_value = mod
            df.loc[row_index, column_name] = new_value
        st.write('DataFrame modifié :')
        st.write(df)
        
        # Réinitialiser la liste des modifications
        st.session_state.modifications = []
        
        # Conversion du DataFrame modifié en JSON
        modified_json = df.to_json(orient='records', indent=2)
        
        # Bouton pour télécharger le fichier JSON modifié
        st.download_button(
            label="Télécharger les modifications en JSON",
            data=modified_json,
            file_name="modified_data.json",
            mime="application/json"
        )

