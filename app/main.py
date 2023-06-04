import datetime

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.DBmodels import *
from dataclasses import dataclass
import requests as r


@dataclass
class QuestionItem:
    questions_num: int


# README КАК ЗАПУСКАТЬ ДОКЕР КОМПОСЕ, БЫЛ СОЗДАН ОТДЕЛЬНЫЙ КОНТЕЙНЕР

app = FastAPI()
root_extended = 'https://jservice.io/api/random?count=1'


@app.post("/")
def question(questions_item: QuestionItem):
    if questions_item:
        n = questions_item.questions_num
        i = 0
        while i < n:
            answer = r.get(root_extended)
            if answer.ok:
                answer_json = answer.json()[0]
                id = answer_json['id']
                answer = answer_json.get('answer', '')
                question = answer_json.get('question', '')
                created_at = answer_json.get('created_at', None)
                if created_at:
                    created_at_date = datetime.datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
                else:
                    created_at_date = datetime.datetime.now().date()
                if db.query(Questions).filter(Questions.id == id).first():
                    continue
                else:
                    db.add(Questions(id=id, question=question, answer=answer, date_of_question=created_at_date))
                    db.commit()
                    i += 1
            else:
                JSONResponse(content={}, status_code=answer.status_code)
                break
        last_record = db.query(Questions).all()[-1]
        return JSONResponse(content={'id': last_record.id, 'question': last_record.question,
                                     'answer': last_record.answer,
                                     'created_at': last_record.date_of_question.strftime('%Y-%m-%d')}, status_code=200)
    else:
        return JSONResponse(content={}, status_code=400)




