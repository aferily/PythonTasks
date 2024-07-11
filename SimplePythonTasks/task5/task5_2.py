questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
    ]

answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
    ]

answers_rigth_order = [answers[1], answers[2], answers[0]]
for i in range(0, len(questions)):
    print(f"Q: {questions[i]}\nA: {answers_rigth_order[i]}")
