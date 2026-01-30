import random

# Settings (change these in the code)
MAX_NUMBER_ADD = 20
MAX_NUMBER_SUB = 15        # Maximum number for problems
MAX_NUMBER_MUL = 10

NUM_QUESTIONS = 10      # How many questions per session


# Welcome message
print("\nWelcome to the Math Practice Program!\n") 
print("You can practice Addition (+), Subtraction (-), or Multiplication (x)\n")



try: 
    with open("scores.txt", "r") as f:
        scores = f.readlines()
        if scores: #check file is not empty
            high_score = max(int(line.split()[0]) for line in scores) #extract score
            print(f"Previous high score: {high_score}/{NUM_QUESTIONS}\n")
        else:
            high_score = 0
except FileNotFoundError:
        high_score = 0
        print("No previous score has been recorded. Let'S start fresh!\n")


while True:
    # keep looping until user gives valid input
    while True:   
        operation = input("Which operation would you like to practice?\n" # User chooses operation
                        "Press 1 for Addition\n"
                        "Press 2 for Subtraction\n"
                        "Press 3 for Multiplication\n"
        ) 
        if operation in ["1", "2", "3"]:
            break #exits loop if user enters valid input
        else:
            print("Invalid choice. Please enter either 1, 2, or 3 to begin.\n")


    score = 0

    for i in range(NUM_QUESTIONS):
        
        #defines the max numbers for each operation
        if operation == "1":    
            max_num = MAX_NUMBER_ADD #Addition
        elif operation == "2":
            max_num = MAX_NUMBER_SUB #substraction
        elif operation == "3":
            max_num = MAX_NUMBER_MUL #multiplication

        num1 = random.randint(1, max_num)
        num2 = random.randint(1, max_num)


# Handle subtraction to avoid negative answers
        if operation == "2":
            if num1 < num2:
                num1, num2 = num2, num1
            correct_answer = num1 - num2
            question = f"{num1} - {num2} = ? "
        elif operation == "1":
            correct_answer = num1 + num2
            question = f"{num1} + {num2} = ? "
        elif operation == "3":
            correct_answer = num1 * num2
            question = f"{num1} x {num2} = ? "

        while True: #keep looking till user enters a number
            try: 
                user_answer = int(input(question)) # Ask user for answer
                break
            except ValueError:
                print("Please enter numbers only. Letters are not excepted.")


        # Check answer
        if user_answer == correct_answer:
            score += 1
            print("Correct! \n")
            print(f"Your score is now: {score}\n")
            print(f"Question {i+1} of {NUM_QUESTIONS}\n")

        else:
            print(f"Oops! The correct answer was {correct_answer} \n")
            print(f"Your current score: {score}\n")

        print(f"Question {i+1} of {NUM_QUESTIONS}\n")

    # Final score
    print(f"You got {score} out of {NUM_QUESTIONS} correct! \n")
    print("Thanks for practicing!")

    if score > high_score:
        high_score = score
        print(f"New High Score: {high_score}/{NUM_QUESTIONS}!\n")
    else:
        print(f"Current High Score: {high_score}/{NUM_QUESTIONS}!\n")

    with open("scores.txt", "w") as f:  #overwrite file with latest high score
        f.write(f"{high_score} out of {NUM_QUESTIONS}\n")              


    while True:
        user_input = input("Do you want to keep practising?\n"
            "Type Yes to continue.\n" 
            "Type No to exit game.\n"
            ).upper()

        if user_input in ["YES", "Y"]:
                print("Great! Let's start a new round.\n")
                break #breaks to main loop
        elif user_input in ["NO", "N"]:
            print("Thanks for playing! See you next time!")
            print(f"Current High Score: {high_score}/{NUM_QUESTIONS}!\n")
            exit() #exits game 
        else:
            print("Please type Yes or No.\n")                        
        