import streamlit as st
from streamlit_option_menu import option_menu
import os
from PIL import Image

# Import des pages existantes
from my_pages import home, eda, about, prediction

# Configuration de la page
st.set_page_config(page_title="Détection de Fraude", layout="wide")

# --- Sidebar avec logo et menu ---
with st.sidebar:
    # Logo local (remplace "logo_esprit.png" par le nom réel si besoin)
    logo_path = os.path.join(os.getcwd(), "images/logo_esprit.png")
    if os.path.exists(logo_path):
        st.image(Image.open(logo_path), width=500)

    # Titre personnalisé sous le logo
    st.markdown("<h2 style='text-align: center;'>Détection de Fraude</h2>", unsafe_allow_html=True)

    # Menu stylé
    choice = option_menu(
        menu_title=None,
        options=["Accueil", "Exploration", "Prédiction", "À propos"],
        icons=["house", "bar-chart", "shield-exclamation", "info-circle"],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#111"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "--hover-color": "#0d6efd"},
            "nav-link-selected": {"background-color": "#0d6efd"},
        }
    )

# --- Navigation vers les pages ---
if choice == "Accueil":
    home.show()
elif choice == "Exploration":
    eda.show()
elif choice == "Prédiction":
    prediction.show()
elif choice == "À propos":
    about.show()
