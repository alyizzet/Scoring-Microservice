# Flask Scoreboard Microservice

<h3> Virtualenv Commands </h3>
-virtualenv -p /home/example_username/opt/python-3.6.2/bin/python3 venv <br>
-source venv/bin/activate

<h3> Docker Build & Run Commands </h3>
- docker build -t score_microservice . <br>
- docker run -d -p 4000:80 score_microservice  <br>
- docker container ls <br>
- docker stop $(docker ps -aq) <br>
- docker rm container

<h3> Local Test Command </h3>
- FLASK_APP=app.py flask run

<h3> Mock JSON Server </h3> 
- docker run --name mock-json-server -v \$(pwd)/db.json:/usr/src/app/data.json -p 8001:8000 ajoelpod/mock-json-server

<b> Required </b>

1. How to build the microservice
2. Usage examples through cURL(Postman API Tester)
3. Testing
4. Architectural Diagram + Text, how it should be implemented, how user interact with the service.
5. CloudCraft Diagram
