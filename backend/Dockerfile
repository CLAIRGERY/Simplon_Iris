FROM python:3.11

WORKDIR /app

# On copie tout le contenu du dossier backend dans /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# On lance : dossier.nom_du_fichier:variable_fastapi
CMD ["uvicorn", "api.Iris_Api:app", "--host", "0.0.0.0", "--port", "8000"]