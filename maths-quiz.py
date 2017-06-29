import random

#Sets score to 0
score=0
#initialises dictionary
questions = {}

#Randomly generates maths questions with number between 0 and 10
#Operator is randomly picked out of (+, -, *)
for i in range(10):
    int_a = random.randint(0,10)
    int_b = random.randint(0,10)
    operators = ['+','-','*']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "
    
    #adds the question to questions dictionary
    questions.update({question:answer})

#Iterates through the questions in the dictionary and response respectively
for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("Correct!")
        score+=1
    else:
        print("You're Wrong!")
#Outputs the users score
print("You got "+str(score)+" right!")

