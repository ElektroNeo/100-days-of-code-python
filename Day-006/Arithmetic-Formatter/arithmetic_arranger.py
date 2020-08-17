def arithmetic_arranger(problems, answer=False):
    # Initialise variables
    first = ''
    second = ''
    firstNum = ''
    secondNum = ''
    line = ''
    ans = ''
    count = len(problems)

    # If too many problems
    if count > 5:
        return "Error: Too many problems."
    
    # Go to problem by problem
    for problem in problems:
        # Split every problem
        problem = problem.split()

        # Get numbers and operator
        firstNum = problem[0]
        secondNum = problem[2]
        operand = problem[1]

        # Check for numeric
        if not firstNum.isnumeric() or not secondNum.isnumeric():
            return "Error: Numbers must only contain digits."
        
        # Check for number length
        if len(firstNum) > 4 or len(secondNum) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Check for operand
        if (operand == '+') or (operand == '-'):
            # Set maximum length
            length = max(len(firstNum), len(secondNum)) + 2

            # Add numbers and operand
            first += firstNum.rjust(length)
            second += operand + secondNum.rjust(length-1)

            # Add lines
            for i in range(length):
                line += '-'
            
            # Check for answer
            if answer == True:
                # Calculate answer and justify to right
                if operand == '+':
                    ans += str(int(firstNum) + int(secondNum)).rjust(length)
                elif operand == '-':
                    ans += str(int(firstNum) - int(secondNum)).rjust(length)
        else:
            # If operator is different than + or -
            return "Error: Operator must be '+' or '-'."

        # Check for last problem
        if count != 1:
            first += '    '
            second += '    '
            line += '    '
            ans += '    '
        # Decrement problem counter
        count -= 1

    # Check for answer
    if answer == True:
        arranged_problems = first + '\n' + second + '\n' + line + '\n' + ans
    else:
        arranged_problems = first + '\n' + second + '\n' + line

    # Return formatted string
    return arranged_problems