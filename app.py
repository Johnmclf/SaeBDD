import streamlit as st
import pandas as pd
import json

uploaded_file = st.file_uploader("Choisissez un fichier JSON", type="json")
if uploaded_file is not None:
    data = json.load(uploaded_file)
    df = pd.DataFrame(data)
    st.write('DataFrame original :')
    st.write(df)
    while True:
        modify = st.checkbox('Voulez-vous faire une modification ?')
        if modify:
            row_index = st.number_input('Entrez l\'index de la ligne à modifier', min_value=0, max_value=len(df)-1, step=1)
            column_name = st.text_input('Entrez le nom de la colonne à modifier')
            new_value = st.text_input('Entrez la nouvelle valeur')

            if st.button('Appliquer les modifications'):
                df.loc[row_index, column_name] = new_value
                st.write('DataFrame modifié :')
                st.write(df)
        else:
            break
