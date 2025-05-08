import streamlit as st

def show():
    st.title("À propos du projet")
    st.markdown("""
    - Données : Kaggle Fake Job Postings  
    - Étapes : Nettoyage des données, EDA, modélisation, déploiement  
    - Outils : Python, Pandas, Scikit-Learn, Streamlit
    """)
