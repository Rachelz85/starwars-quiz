from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Empty list to store the questions:
question_bank = []
# Loop through each question in the question_data:
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Quiz brain object: 
quiz = QuizBrain(question_bank)
quiz.next_question()
