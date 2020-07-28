1. For API Testing Postman is used.

---Docker Build & Run Commands---
docker build -t score_microservice .
docker run -d -p 4000:80 score_microservice
docker container ls

---Local Test Command---
FLASK_APP=app.py flask run

---Mock JSON Server---
docker run --name mock-json-server -v \$(pwd)/db.json:/usr/src/app/data.json -p 8001:8000 ajoelpod/mock-json-server

Required

1. How to build the microservice
2. Usage examples through cURL

Architectural Diagram + Text, how it should be implemented, how user interact with the service.
