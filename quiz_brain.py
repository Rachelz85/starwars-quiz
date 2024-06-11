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
        # Will add score atribute here 
        self.question_list = q_list

    # Still had questions method, 
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # Increment the question number
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    # method to check if the answer matches the correct current answer 
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct you are, young Padawan. The Force is strong with you!")
        else:
            print("Incorrect, young Padawan. Much to learn, you still have")
        print(f"The correct answer was: {correct_answer}.")