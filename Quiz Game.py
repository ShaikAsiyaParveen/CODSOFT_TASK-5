#Ask Username
name=input("Enter your user name:\n")
#welcome wishes!
print("Hello!",name,",","Welcome to the Quiz :) !\n")
print("By attending the quiz you may know that how much do yo know about python \n")
print("here the rules to folow in the quiz\n")
print("make sure to follow all rlues as mentioned \n")
print("\n")
print("there 3 MCQ questions in this quiz\n")
print("for every correct answer you score 20 marks \n")
print("Total marks is '60'\n")
print("Above 25 marks you won the quiz  and  below 20 marks you loos the quiz \n")      
#Creating  5 multiline strings(q1,q2,q3,q4,q5) in python by using triple quotes("""")
q1=""" 1)Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted
"""
q2="""2)All keywords in Python are in _________
a) Capitalized
b) lower case
c) UPPER CASE
d) None of the mentioned
"""
q3=""" Which of the following is used to define a block of code in Python language?
a) Indentation
b) Key
c) Brackets
d) All of the mentioned
"""

#creating dictionary named as questions
questions={q1:"a",q2:"d",q3:"a" }
#intializing score value as 0
score=0;
#By using for loop to print quiz questions
for i in  questions:
    print(i)
    #By using input function to take answer as input from the user
    ans=(input( "Enter the choice[a/b/c/d]:"))
    #By using if loop to compare user answer with actual answer
    if(ans==questions[i]):
        #if its correct print below statement
        print(ans,"  congratulation you enterd  Correct answer!")
        score+=20
        #prints current score
        print("current score :",score)
    else:
        print("wrong answer!Correct answer is",questions[i])
print("quiz completed")
#By using if loop to check whether the player is pass or fail
if(score<=20):
    print("-------------------------------------")
    print(name,"!your entered choice is incorrect so your loose the quiz\n")
    print("no worries,try next time")
else:
    print("-------------------------------------")
    print(name,"!congratulations you won the quiz")
    print("well played")
#prints final score
print("Your Final Score is",score,"/60")