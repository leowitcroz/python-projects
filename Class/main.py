
from data import question_data
from quiz_brain import QuizBrain

class Question:
    def __init__(self,q_text,q_answer):
        self.q_text = q_text
        self.q_answer = q_answer


question_bank = []

for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(q_text = question_text,q_answer = question_answer)
    question_bank.append(new_question)

##print(question_bank[8].q_answer)

quiz = QuizBrain(question_bank)

print(len(question_bank))

while quiz.still_has_questions() == True:
    quiz.next_question()


print('you have completede the quiz')        
print(f'your total scores was {quiz.score}/{len(question_bank)}')
    