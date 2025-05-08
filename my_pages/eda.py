import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show():
    st.title("Exploration des données (exemple)")

    # Données fictives pour tester
    data = pd.DataFrame({
        "title": ["Engineer", "Designer", "Manager", "Sales Rep"],
        "industry": ["Tech", "Design", "Management", "Sales"],
        "fraudulent": [0, 1, 0, 1]
    })

    st.write("Aperçu des données simulées :")
    st.dataframe(data)

    st.write("Distribution des offres frauduleuses :")
    fig, ax = plt.subplots()
    sns.countplot(x="fraudulent", data=data, ax=ax)
    st.pyplot(fig)

    st.write("Répartition par secteur :")
    fig2, ax2 = plt.subplots()
    data["industry"].value_counts().plot(kind='barh', ax=ax2)
    st.pyplot(fig2)
