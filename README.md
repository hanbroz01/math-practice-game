# 🧮 Math Practice Program

A Python program to practice basic math skills: Addition, Subtraction, and Multiplication.  
Designed to help beginners and kids practice math and track their progress with high scores.

## Features

- Practice Addition, Subtraction, and Multiplication
- Configurable number of questions and maximum numbers
- Tracks high scores automatically
- Handles invalid inputs gracefully
- Easy to use for beginners and kids

## Installation

1. Make sure you have **Python 3.x** installed.
2. Clone the repository and navigate into it:

```bash
git clone https://github.com/hanbroz01/math_practice_game.git
cd math_practice_game
python main.py
```

## Usage

<img width="640" height="239" alt="image" src="https://github.com/user-attachments/assets/211cd755-c002-4a22-9711-fcc06fc276cc" />

1. When you run the program, it will display a welcome message and your **previous high score** (if any).

2. Choose which operation to practice:
   - `1` for **Addition (+)**
   - `2` for **Subtraction (-)**
   - `3` for **Multiplication (x)**

3. Answer the questions displayed. Only **numbers** are accepted.  
   - Subtraction is handled to avoid negative results.

4. After each answer, your **current score** is shown.

5. At the end of the session, your **final score** is shown and compared to your **previous high score**.  
   - If you beat your high score, it updates automatically in `scores.txt`.

6. You can choose to **continue practicing** or **exit** the program:
   - Type `Yes` or `Y` to continue.
   - Type `No` or `N` to exit.

  
## Notes

- ➡️ The program creates a scores.txt file to store high scores.
- ➡️ Designed to be beginner-friendly and safe for kids.
- ➡️ The number of questions and maximum numbers can be adjusted in the code.
