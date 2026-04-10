# Projet de Classification d'Iris - Pipeline CI/CD

Ce projet implémente un cycle complet de Machine Learning, allant de l'entraînement d'un modèle de classification à son exposition via une interface utilisateur web. Il utilise **Scikit-Learn** pour la modélisation, **MLflow** pour le suivi des expériences, **FastAPI** pour le backend et **Streamlit** pour le frontend.

---

## Installation des dépendances

Avant de commencer, assurez-vous d'installer les bibliothèques Python nécessaires via votre terminal :

```bash
pip install pandas scikit-learn mlflow matplotlib fastapi uvicorn pydantic joblib streamlit requests
```

---

## Guide d'utilisation

Le projet s'exécute en **trois étapes distinctes**. Il est recommandé d'utiliser des **terminaux séparés** pour chaque service.

### 1. Entraînement du modèle

Exécutez le script d'entraînement pour générer le fichier de modèle et enregistrer les métriques dans MLflow.

```bash
python train.py
```

Cette commande effectue les actions suivantes :

- Chargement et préparation des données (*Iris dataset*)
- Entraînement d'un modèle `RandomForestClassifier`
- Génération d'une matrice de confusion dans le dossier de résultats
- Sauvegarde du modèle au format `model.pkl`
- Enregistrement de la session dans la base de données locale MLflow

### 2. Lancement de l'API Backend (FastAPI)

Une fois le modèle généré, lancez le serveur API pour permettre les prédictions en temps réel.

```bash
uvicorn main:app --reload
```

L'API est accessible par défaut sur : `http://127.0.0.1:8000`

La documentation interactive (Swagger) est disponible sur : `http://127.0.0.1:8000/docs`

### 3. Lancement de l'interface utilisateur (Streamlit)

Enfin, lancez le frontend pour interagir avec le modèle via votre navigateur.

```bash
streamlit run app.py
```

L'interface vous permettra de saisir les 4 caractéristiques de la fleur :

- longueur des sépales
- largeur des sépales
- longueur des pétales
- largeur des pétales

Puis d'envoyer une requête de prédiction à l'API.

---

## Suivi des expériences avec MLflow

Pour visualiser l'historique de vos entraînements, les métriques d'accuracy et les artefacts (schémas), utilisez l'interface de visualisation MLflow :

```bash
mlflow ui --backend-store-uri sqlite:///mlflow_tracking.db
```

Accédez ensuite à l'adresse `http://127.0.0.1:5000` dans votre navigateur.

---

## Structure des points de terminaison API

| Méthode | Route      | Description |
|--------|------------|-------------|
| GET    | `/`        | Vérifie si l'API est fonctionnelle (Health Check). |
| POST   | `/predict` | Reçoit les caractéristiques en JSON et renvoie la classe d'Iris prédite. |
