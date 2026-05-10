import random

def generate_question():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    return max(number_one, number_two), min(number_one, number_two)

def ask_question(number_one, number_two):
    correct_answer = number_one - number_two
    for attempt in range(2):
        answer = int(input(f"What is {number_one} - {number_two}? = "))
        if answer == correct_answer:
            print("That is correct, Keep going!!")
            return True
        else:
            print("Wrong answer, Try again!!")
    return False

def run_questions():
    score = 0
    for _ in range(10):
        number_one, number_two = generate_question()
        if ask_question(number_one, number_two):
            score += 1
    print(f"Final Score: {score}/10")
    return score
    

