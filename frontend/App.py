import streamlit as st
import requests

# --- Configuration de la page (Thème Floral) ---
st.set_page_config(page_title="Prédiction d'Iris", page_icon="🌸", layout="centered")

# Un peu de CSS pour colorer les boutons en rose pastel
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ffb7b2;
        color: #000000;
        border: none;
        border-radius: 8px;
    }
    div.stButton > button:hover {
        background-color: #ff9eaa;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌺 Intelligence Artificielle Botanique")
st.write("Entrez les dimensions des pétales et sépales pour identifier l'espèce d'Iris.")

# --- Variables Globales ---
# URL de l'API FastAPI (par défaut en local sur le port 8000)
API_URL = "http://api-service:8000/predict"

# --- Saisie des 4 attributs ---
st.subheader("🌿 Caractéristiques de la fleur")

col1, col2 = st.columns(2)
with col1:
    sepal_length = st.number_input("Longueur du sépale (cm)", min_value=0.0, max_value=10.0, value=5.1)
    sepal_width = st.number_input("Largeur du sépale (cm)", min_value=0.0, max_value=10.0, value=3.5)
with col2:
    petal_length = st.number_input("Longueur du pétale (cm)", min_value=0.0, max_value=10.0, value=1.4)
    petal_width = st.number_input("Largeur du pétale (cm)", min_value=0.0, max_value=10.0, value=0.2)

st.markdown("---")

# --- Boutons de communication avec l'API ---
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    # Bouton pour la route POST /predict
    if st.button("🔮 Prédire l'espèce"):
        # Les données formatées exactement comme attendu par votre classe Pydantic "Data"
        payload = {"features": [sepal_length, sepal_width, petal_length, petal_width]}
        
        try:
            response = requests.post(f"{API_URL}/predict", json=payload)
            if response.status_code == 200:
                resultat = response.json()
                # On récupère le premier élément de la liste retournée
                espece_predite = resultat["prediction"][0] 
                st.success(f"🌷 Résultat : Il s'agit d'un **{espece_predite}** !")
            else:
                st.error(f"Erreur de l'API : {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("🥀 Impossible de contacter l'API. Vérifiez que FastAPI est bien lancé.")

with col_btn2:
    # Bouton pour la route GET / (Santé de l'API)
    if st.button("⚙️ Option (Test API)"):
        try:
            response = requests.get(f"{API_URL}/")
            if response.status_code == 200:
                st.info(f"✅ L'API est en ligne : {response.json()}")
            else:
                st.warning(f"L'API a répondu avec un code {response.status_code}")
        except requests.exceptions.ConnectionError:
            st.error("🥀 Impossible de contacter l'API. Vérifiez que FastAPI est bien lancé.")