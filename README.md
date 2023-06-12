![](img_for_readme/main.jpg)
____
**<span style='color:rgb(250, 196, 0)'>This project is a web service that performs the following functions:</span>**
+ Accepts requests as input, in the form of a service question number, containing English-language questions for quizzes; 
+ The information received from the service is stored in the database in the form of: question id, question text, answer text, question creation date. 
   If the database has the same question, additional requests are made to the public API with quizzes until a unique question for the quiz is obtained.
____
**<span style='color:rgb(250, 196, 0)'>Instructions for building a docker image with a service, setting it up and running it.</span>**
+ This option also starts the database and the pgadmin4 administration tool.
+ The start settings for running containers are located in the docker-compose.yml file
+ The Dockerfile contains instructions for building the jservice service image.
1. Run with docker-compose: docker compose up -d
2. Stop and remove Docker-compose containers: docker compose down
3. View information about running Docker-compose processes: docker compose ps
4. View logs in Docker-compose: docker compose logs
____
**<span style='color:rgb(250, 196, 0)'>Starting the service in Docker:</span>**
1. Building the application image: docker build -t jservice .
2. Create a container and run it: docker run -d --name mycontainer -p 8080:8080 -e DB_URI=postgresql://juser:cfytr666131@localhost/jservicedb jservice
____
**<span style='color:rgb(250, 196, 0)'>Starting a service without a container:</span>**
uvicorn app.main:app --host "0.0.0.0" --port "8080"
____
**You can check the performance of the service by going to the file: testapi.py** 
