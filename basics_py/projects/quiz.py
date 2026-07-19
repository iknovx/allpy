def quiz():
    quiz = [
        {
            "question": "What is the capital of France?",
            "options": ("A. Paris", "B. London", "C. Berlin", "D. Rome"),
            "answer": "A",
        },
        {
            "question": "What is 2 + 2?",
            "options": ("A. 3", "B. 4", "C. 5", "D. 6"),
            "answer": "B",
        },
        {
            "question": "What is the capital of Spain?",
            "options": ("A. Madrid", "B. Barcelona", "C. Valencia", "D. Seville"),
            "answer": "A",
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
            "answer": "D",
        },
    ]

    guesses = []
    score = 0

    for item in quiz:
        print(item["question"])
        for option in item["options"]:
            print(option)

        while True:
            answer = input("Your answer: ").strip().upper()
            if answer in ("A", "B", "C", "D"):
                break
            print("Пожалуйста, введите A, B, C или D.")

        guesses.append(answer)
        if answer == item["answer"]:
            score += 1
        print()  # пустая строка между вопросами

    print(f"Score: {score}/{len(quiz)}")

    print("Your answers:")
    for i, guess in enumerate(guesses):
        print(f"Question {i + 1}: {guess}")
quiz()