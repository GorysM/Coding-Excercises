def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    separators = []
    answers = []

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        top_line = num1.rjust(width)
        bottom_line = operator + num2.rjust(width - 1)
        separator = "-" * width

        first_line.append(top_line)
        second_line.append(bottom_line)
        separators.append(separator)

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            elif operator == '-':
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))

    arranged_first_line = '    '.join(first_line)
    arranged_second_line = '    '.join(second_line)
    arranged_separators = '    '.join(separators)
    arranged_answers = '    '.join(answers) if show_answers else ""

    if show_answers:
        arranged_problems = f"{arranged_first_line}\n{arranged_second_line}\n{arranged_separators}\n{arranged_answers}"
    else:
        arranged_problems = f"{arranged_first_line}\n{arranged_second_line}\n{arranged_separators}"

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
