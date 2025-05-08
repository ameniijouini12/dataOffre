import streamlit as st
import pandas as pd

def show():
    st.title("Faire une prédiction")

    st.write("Veuillez remplir les informations de l'offre d'emploi :")

    title = st.text_input("Titre du poste")
    company_profile = st.text_area("Profil de l'entreprise")
    description = st.text_area("Description du poste")
    requirements = st.text_area("Exigences")
    benefits = st.text_area("Avantages")

    if st.button("Prédire"):
        # 🔍 Liste de mots-clés suspects
        keywords = ["urgent", "travail à domicile", "argent facile", "pas d'expérience", "paiement immédiat"]

        # Calcul d’un score simulé basé sur la présence de ces mots-clés
        score = sum(kw in description.lower() for kw in keywords) / len(keywords)

        # Résultat basé sur le score
        if score > 0.3:
            st.error(f"⚠️ Offre potentiellement frauduleuse (score simulé : {score:.2f})")
        else:
            st.success(f"✅ Offre probablement légitime (score simulé : {score:.2f})")
