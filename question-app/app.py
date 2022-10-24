from Question import Question

question_prompts = [
"What colour are apples?\n(a) Red/Green (b) blue/yellow (c) black/red ",
"What colour are bananas?\n(a) black (b) red (c) yellow ",
"What colour are strawberries\n (a) Yellow (b) Red (c) Blue "
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)))


run_test(questions)
