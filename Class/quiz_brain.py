class QuizBrain:
    def __init__ (self, q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0

    def still_has_questions(self):
        verifica = True
        if self.q_number < len(self.q_list):
            
            return True
        else:
            
            return False
        
    def next_question(self):
        currentQuestion = self.q_list[self.q_number]
        self.q_number += 1
        user_answer = input(f'Q.{self.q_number}: {currentQuestion.q_text} True/False: ').lower()
        self.checking_answer(user_answer,currentQuestion.q_answer)
        

    def checking_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print('you got it') 
        else:
            print('you missed it') 
        
        print(f'your current score is {self.score}/{self.q_number}')


    
    
        

       