import Stack

def eval_postfix(expr):
    stack = Stack()

    for token in expr.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            else:
                raise SyntaxError("Invalid operator")

            stack.push(result)

    return stack.pop()

def in2post(expr):
    stack = Stack()
    output = []

    operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in expr.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while stack.top() != '(':
                output.append(stack.pop())
            stack.pop()  # Discard the '('
        elif token in operators:
            while stack.size() > 0 and stack.top() in operators and operators[stack.top()] >= operators[token]:
                output.append(stack.pop())
            stack.push(token)

    while stack.size() > 0:
        output.append(stack.pop())

    return ' '.join(output)

def main():
    try:
        with open("data.txt", "r") as file:
            infix_expression = file.readline().strip()
    except FileNotFoundError:
        print("Error: File 'data.txt' not found.")
        return 1

    print("infix:", infix_expression)

    try:
        postfix_expression = in2post(infix_expression)
        print("postfix:", postfix_expression)

        result = eval_postfix(postfix_expression)
        print("answer:", result)

    except SyntaxError as e:
        print("Error:", e)
        return 1
    except ValueError as e:
        print("Error:", e)
        return 1

    return 0

if __name__ == "__main__":
    main()
