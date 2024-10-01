class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{question_number}: ")