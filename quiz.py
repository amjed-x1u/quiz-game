# quiz game

Questions = ("what is the hottest planet in the Solar System?: ",
            "what is the largest planet in the Solar System?: ",
            "how many people are there in the world?: ",
            "who is considered the most influential scientist in the history of computer science?: ",
            "who created the binary system ?: ") 

options = (("A.VENUS","B.EARTH","C.MARS","D.MERCURY"),
          ("A.URANUS","B.SATURN","C.NEPTUNE","D.JUPITER"),
          ("A.5.5","B.6.8","C.8.3","D.10.1"),
          ("A.Alan turing","B.Ada Lovelace","C.John von Neumann","D.Dennis Ritchie"),
          ("A.Leonardo da Vinci","B.Gottfrid Wilhelm Leibniz","C.Prophet Muhammad ","D.Albert Einstein"))

answers = ("A","D","C","A","B")

guesses = []
score = 0
question_num = 0

for question in Questions :
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("ENTER (A,B,C,D):").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("COORECT (^人^)")
        score += 1
    else:
        print("INCOORECT!!!!")
        print(f"{answers[question_num]} is the coorect answer")

    question_num += 1

print("-------------------")
print("       RESULTS            ")
print("-------------------")

print("answers : ",end="")
for answer in answers :
    print(answer,end=" ")
print()

print("guesses : ",end="")
for guess in guesses :
    print(guess,end=" ")
print()

score = int(score / len(answers) * 100)
print(f"Your score is : {score}%")
