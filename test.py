# Importer les bibliothèques nécessaires
import streamlit as st
import pickle

def charger_modele():
    # Charger le modèle à partir du fichier Pickle
    with open('modele.pkl', 'rb') as fichier_modele:
        modele = pickle.load(fichier_modele)
    return modele

# Interface utilisateur Streamlit
st.title("Application de Classification des Fleurs")

# Ajouter les widgets pour l'entrée des caractéristiques
caracteristique1 = st.slider("Caractéristique 1", 0.0, 7.9, 4.0)
caracteristique2 = st.slider("Caractéristique 2", 0.0, 7.9, 4.0)
caracteristique3 = st.slider("Caractéristique 3", 0.0, 7.9, 4.0)
caracteristique4 = st.slider("Caractéristique 4", 0.0, 7.9, 4.0)

# Prétraitement des caractéristiques avec StandardScaler
caracteristiques = [[caracteristique1, caracteristique2, caracteristique3, caracteristique4]]

# Prévoir la classe avec le modèle
modele = charger_modele()
prediction = modele.predict(caracteristiques)

# Afficher la prédiction
st.markdown(f"<p style='font-size:24px; font-weight:bold;'>La fleur est de la classe : {prediction[0]}</p>", unsafe_allow_html=True)
