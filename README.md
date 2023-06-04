![](img_for_readme/main.jpg)
____
**<span style='color:rgb(250, 196, 0)'>This project is a web service that performs the following functions:</span>**
1. Accepts requests as input, in the form of a service question number, containing English-language questions for quizzes;
2. The information received from the service is stored in the database in the form of: question id, question text, answer text, question creation date. 
   If the database has the same question, additional requests are made to the public API with quizzes until a unique question for the quiz is obtained.
____
**<span style='color:rgb(250, 196, 0)'>Instructions for building a docker image with a service, setting it up and running it.</span>**
Данный вариант предусматривает также запуск базы данных и средства администрирования pgadmin4.
Стартовые настройки запуска контейнеров размещены в файле docker-compose.yml
В файле Dockerfile размещены инструкции по сборке образа сервиса jservice.
1. Запуск с помощью Docker-compose: docker compose up -d
2. Остановка с удалением контейнеров Docker-compose: docker compose down
3. Просмотр информации о запущенных процессах Docker-compose: docker compose ps
4. Просмотр логов в Docker-compose: docker compose logs
____
Запуск сервиса в Docker:
1. Создание образа приложения: docker build -t jservice .  
2. Создание контейнера и его запуск: docker run -d --name mycontainer -p 8080:8080 -e DB_URI=postgresql://juser:cfytr666131@localhost/jservicedb jservice
____
Запуск сервиса без контейнера:
uvicorn app.main:app --host "0.0.0.0" --port "8080"
____