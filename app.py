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
        column_name = st.text_input('Entrez le nom de la colonne à modifier')
        new_value = st.text_input('Entrez la nouvelle valeur')
        add_modification = st.form_submit_button('Ajouter la modification')
    
    # Ajouter la modification à la liste
    if add_modification:
        st.session_state.modifications.append((row_index, column_name, new_value))

    # Afficher la liste des modifications en attente
    st.write('Modifications en attente :')
    for mod in st.session_state.modifications:
        st.write(f"Ligne {mod[0]}, Colonne '{mod[1]}', Nouvelle valeur : {mod[2]}")

    # Bouton pour appliquer les modifications
    if st.button('Appliquer toutes les modifications'):
        for mod in st.session_state.modifications:
            row_index, column_name, new_value = mod
            df.loc[row_index, column_name] = new_value
        st.write('DataFrame modifié :')
        st.write(df)
        
        # Réinitialiser la liste des modifications
        st.session_state.modifications = []
