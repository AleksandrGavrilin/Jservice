import requests as r


root = 'http://127.0.0.1:8080'
root_extended = 'https://jservice.io/api/random?count=1'


# Проверка ответа на запрос:
answer = r.post(root + '/', json={'questions_num': 10})


print(answer.status_code)
print(answer.json())