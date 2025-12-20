valid = None
score = 0
def get_input(user_input):
    user_input = input("Please choose an Answer (A, B, C or D): ").upper()
    return user_input

def validate_input(user_input, valid):
    while True:
        if user_input not in {"A", "B", "C", "D"}:
            print("ERROR: Please type A, B, C or D")
            valid = False
            return valid
        else:
            valid = True
            return valid

questions = ("What is the capital of Japan?",
             "Which Planet is known as the Red Planet?",
             "Who wrote 1984?",
             "What is 9 x 7?",
             "Which language is primarily used for Data Science?")

options = (("Tokyo", "Kyoto", "Nagoya", "Osaka"),
           ("Earth", "Jupiter", "Venus", "Mars"), 
           ("George Orwell", "Aldous Huxley", "J.K. Rowling", "Ernest Hemingway"),
           ("56","72", "63", "49"),
           ("HTML", "CSS", "Bash", "Python"))

answers = ("A", "D", "A", "C", "D")

i = 0
x = 0
guesses = []
user_input = None
letters = ["A", "B", "C", "D"]

for question in questions:
    x = 0
    print()
    print(question)
    print()
    question_num = options[i]
    for num in question_num:
        print(f"{letters[x]}) {num}") 
        x += 1 
    print()
    while True:
        user_input = get_input(user_input)
        valid = validate_input(user_input, valid)
        if valid == False:
            continue
        else:
            break
    guesses.append(user_input)
    i += 1

for i in range(len(guesses)):
    if guesses[i] == answers [i]:
        score += 1

print(f"You got {score}/{len(questions)}!")
 