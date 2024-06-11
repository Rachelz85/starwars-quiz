# asking the question
# checking if the answer was correct
# checking if were the end of the quiz

#Quiz brain class
class QuizBrain:
    """
    Manages the flow of the quiz.
    Presents questions to the user.
    Receives and checks user answers.
    Keeps track of the current question.
    Updates and displays the user's score.
    Determines if there are more questions.
    """

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # Increment the question number
        input(f"Q.{self.question_number}: {current_question.text} (True/False):")