from question import Question
from quiz_brain import QuizBrain
from data import question_data

question_list = []

for one_question in question_data:
  text = one_question["question"]
  answer = one_question["correct_answer"]
  new_question = Question(text, answer)
  question_list.append(new_question)

quiz = QuizBrain(question_list)

while quiz.has_questions():
  quiz.next_question()
print("Dokončili ste kvíz.")
print(f"Celkové skóre z kvízu: {quiz.score}/{quiz.question_number}")