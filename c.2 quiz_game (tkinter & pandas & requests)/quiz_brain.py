import random


class QuizBrain:
    def __init__(self, q_list):
        self.score = 0
        self.user_answer = ""
        self.question_list = q_list
        self.question_number = 1
        self.question = random.choice(self.question_list)
        self.answer_ = self.question.answer
        self.text_ = self.question.text

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def check_answer(self):
        if self.user_answer == self.answer_:
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print("That's wrong.")
            print(f"Your current score is: {self.score}/{self.question_number}")
        print("")
        self.question_number += 1
        self.question = self.question = random.choice(self.question_list)
        self.answer_ = self.question.answer
        self.text_ = self.question.text
