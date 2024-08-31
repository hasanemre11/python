from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import requests
import pandas

question_list = []


response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

data = pandas.DataFrame(response.json()["results"])

q = data.question.to_dict()

questions = {value: data.correct_answer.to_dict()[key] for (key, value) in q.items()}
print(questions)

for key, value in questions.items():
    q = Question(key, value)
    question_list.append(q)

quiz_brain = QuizBrain(question_list)


while quiz_brain.still_has_questions:
    quiz_brain.ask_q()
    quiz_brain.check_answer()
