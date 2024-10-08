#! /usr/bin/env python3

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[1].text)
# print(question_bank[1].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've Completed the Quiz, that's it all done")
print(f"Your final score was {quiz.score} / {len(question_bank)} ")