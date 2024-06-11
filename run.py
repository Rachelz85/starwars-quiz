from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def game_instructions():
    """
    Displays the game instructions based on the user's input.
    """
    game_instructions_txt = input("Would you like to see the game instructions? Y/N: ")

    while game_instructions_txt.lower() not in ["y", "n"]:
        game_instructions_txt = input("Enter 'y' to show game instructions or 'n' to skip.\n ")

    if game_instructions_txt.lower() == "y":
        instructions_text = [
            "\nWelcome to the Star Wars Quiz!\n",
            "How to Play:",
            "- You will be asked a series of True/False questions about the Star Wars universe.",
            "- Type 'True' or 'False' to answer each question.",
            "- Your score will be updated and displayed after each question.",
            "- Try to answer all questions correctly to get the highest score!",
            "May the Force be with you!\n"
        ]
        for line in instructions_text:
            print(line)
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

# Ask user if they want to read instructions
game_instructions()

# If quiz still has questions remaining:
while quiz.still_has_questions():
    quiz.next_question()

# User's final score message:
print("The quiz is complete. May the Force will be with you, always \n")
print(f"Your final score is: {quiz.score}/{quiz.question_number} Well done, young Padawan.")
