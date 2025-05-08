import streamlit as st

def show():
    st.title("Bienvenue dans l'application de détection de fraudes")
    st.write("""
    Cette application utilise un modèle de Machine Learning pour prédire si une offre d'emploi est frauduleuse ou non.
    - Vous pouvez explorer les données utilisées pour entraîner le modèle
    - Faire une prédiction en entrant une offre d'emploi
    """)
    st.image("https://cdn.pixabay.com/photo/2021/09/04/17/42/detective-6597426_960_720.png", width=300)
