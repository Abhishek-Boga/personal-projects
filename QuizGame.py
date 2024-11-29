# Author: Abhishek Boga

# Quiz Data
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["New Delhi", "Mumbai", "Kochi", "Vellore"],
        "correct_answer": 1
    },
    {
        "question": "Which planet is known as the 'Red Planet'?",
        "options": ["Saturn", "Earth", "Venus", "Mars"],
        "correct_answer": 4
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Shark", "Elephant", "Blue Whale", "Lion"],
        "correct_answer": 3
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"],
        "correct_answer": 2
    },
    {
        "question": "How many continents are there in the world?",
        "options": ["Seven", "Ten", "Two", "Six", "Three"],
        "correct_answer": 1
    }
]

def quiz_game():
    """Main function for the quiz game."""
    user_answers = []
    score = 0
    reward_per_question = 50

    print("\nWelcome to the Quiz Game!")
    
    # Main quiz loop
    for i, q in enumerate(quiz, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        
        # Display options dynamically
        for j, option in enumerate(q["options"], start=1):
            print(f"{j}. {option}")
        
        # Get user input with validation
        while True:
            try:
                answer = int(input(f"Enter your answer (1-{len(q['options'])}): "))
                if 1 <= answer <= len(q["options"]):
                    user_answers.append(answer)
                    break
                else:
                    print(f"Invalid option! Please choose between 1 and {len(q['options'])}.")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Scoring and feedback
    print("\nYour answers are:", user_answers)

    for i, (q, user_ans) in enumerate(zip(quiz, user_answers), start=1):
        if user_ans == q["correct_answer"]:
            print(f"Question {i}: Correct!")
            score += 1
        else:
            correct_option = q["options"][q["correct_answer"] - 1]
            print(f"Question {i}: Incorrect. The correct answer was '{correct_option}'.")

    # Display results
    total_reward = score * reward_per_question
    print("\nSummary:")
    print(f"Correct answers: {score}/{len(quiz)}")
    print(f"Total reward: ${total_reward}")

if __name__ == "__main__":
    quiz_game()
