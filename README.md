Nztung über Docker & API für Modellverprobung

Vorgehen: 
Einbindung in Web-Service 
	- Modell mit pickle gespeichert
  - Notwendige Requirements speichern
	- API erstellt: FastAPI-Endpinkt erstellt um neue Eingaben entgegen zu nehmen und Vorhersagen zu berechnen
	- Docker-Container bauen: Anwendung in Docker Container verpackt um Bereitstellung zu ermöglichen 
  - Testen über Swagger UI


# Starting Docker

Führe diese zwei Befehle aus, um einen Docker container zu erstellen:
docker build -t mle-python-app .
docker run -d --name my-fastapi-container -p 8000:8000 mle-python-app

# Nutzen Swagger UI im Browser für Verprobung

Kopiere Link in Browser: http://127.0.0.1:8000/docs 

Fülle Eingangsvariablen ein

Modell gibt Wahrscheinlichkeit aus

