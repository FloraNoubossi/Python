# Utiliser une image officielle de Python comme image parente
FROM python:3.9

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier le contenu du répertoire courant dans le conteneur à /app
COPY . /app

# Installer les paquets nécessaires spécifiés dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Rendre le port 80 disponible pour l'extérieur du conteneur
EXPOSE 80

# Définir une variable d'environnement
ENV NAME=Monde

# Exécuter app.py lorsque le conteneur se lance
CMD ["python", "app.py"]

