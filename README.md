Nztung über Docker & API für Modellverprobung

# Starting Docker

Führe diese zwei Befehle aus, um einen Docker container zu erstellen:
docker build -t mle-python-app .
docker run -d --name my-fastapi-container -p 8000:8000 mle-python-app

# Nutzen Swagger UI im Browser für Verprobung

Kopiere Link in Browser: http://127.0.0.1:8000/docs 

Fülle Eingangsvariablen ein

Modell gibt Wahrscheinlichkeit aus

