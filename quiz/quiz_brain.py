class QuizBrain:

  def __init__(self, question_list):
    self.question_number = 0
    self.score = 0
    self.question_list = question_list

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Otázka č.: {self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer, current_question.answer)
  
  def has_questions(self):
    if self.question_number < len(self.question_list):
      return True
    else:
      return False
  
  def check_answer(self, user_answer, current_question):
    if user_answer.lower() == current_question.lower():
      print("Správne")
      self.score += 1
    else:
      print("Nesprávne")
    
    print(f"Vaše skóre je: {self.score}/{self.question_number}")