valid = None

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
           ("Earth", "Mars", "Jupiter", "Venus"), 
           ("George Orwell", "Aldous Huxley", "J.K. Rowling", "Ernest Hemingway"),
           ("56", "63", "72", "49"),
           ("Python", "HTML", "CSS", "Bash"))

answers = ("Tokyo", "Mars", "George Orwell", "63", "Python")

i = 0
guesses = []
user_input = None

for question in questions:
    print()
    print(question)
    print()
    print(options[i])
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

print(guesses)

score = 0
question_num = 0