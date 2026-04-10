# 1. On utilise la version complète (comme pour le backend)
FROM python:3.11

# 2. On définit un dossier de travail différent pour ne pas confondre
WORKDIR /frontend_serveur

# 3. Mise à jour de l'outil d'installation
RUN pip install --upgrade pip

# 4. Installation des outils pour le site web
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. On copie tout le code (app.py, etc.)
COPY . .

# 6. Streamlit utilise par défaut le port 8501
EXPOSE 8501

# 7. La commande pour lancer le site
CMD ["streamlit", "run", "App.py", "--server.port=8501", "--server.address=0.0.0.0"]