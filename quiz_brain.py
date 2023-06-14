class quiz_brain():

    def __init__(self, question_list) -> None:
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
