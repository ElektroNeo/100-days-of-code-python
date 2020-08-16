def arithmetic_arranger(problems, answer=False):

    first = ''
    second = ''
    firstNum = ''
    secondNum = ''
    line = ''
    ans = ''

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        problem = problem.split()

        firstNum = problem[0]
        secondNum = problem[2]
        operand = problem[1]

        if operand != '+' or operand != '-':
            return "Error: Operator must be '+' or '-'."

        length = max(len(first), len(second)) + 2

        first = firstNum.rjust(length)
        second = operand + secondNum.rjust(length-1)

        for i in range(length):
            line += '-'
        
        if answer == True:
            if operand == '+':
                ans = str(int(firstNum) + int(secondNum))
            elif operand == '-':
                ans = str(int(firstNum) - int(secondNum))
            ans.rjust(length)

        first += '    '
        second += '    '
        line += '    '
        ans += '    '

    first.rstrip()
    second.rstrip()
    line.rstrip()
    ans.rstrip()

    if answer == True:
        arranged_problems = first + '\n' + second + '\n' + line + '\n' + ans
    else:
        arranged_problems = first + '\n' + second + '\n' + line

    return arranged_problems