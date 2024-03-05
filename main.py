from stack import Node, Stack


def eval_postfix(expr):
    stack = Stack()

    for token in expr.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.push(float(token))
        else:
            if stack.size() < 2:
                raise SyntaxError("Invalid postfix expression")

            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                if operand2 == 0:
                    raise ValueError("Division by zero")
                result = operand1 / operand2
            else:
                raise SyntaxError("Invalid operator")

            stack.push(result)

    if stack.size() != 1:
        raise SyntaxError("Invalid postfix expression")

    return stack.top()


def in2post(expr):
    stack = Stack()
    output = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in expr:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while stack.size() > 0 and stack.top() != '(':
                output.append(stack.pop())
            if stack.size() == 0 or stack.top() != '(':
                raise SyntaxError("Mismatched parentheses")
            stack.pop()
        elif token in precedence:
            while stack.size() > 0 and stack.top() in precedence and precedence[stack.top()] >= precedence[token]:
                output.append(stack.pop())
            stack.push(token)

    while stack.size() > 0:
        if stack.top() == '(':
            raise SyntaxError("Mismatched parentheses")
        output.append(stack.pop())

    return ' '.join(output)


def main():
    with open("data.txt", "r") as file:
        for line in file:
            infix_expr = line.strip()
            print("infix:", infix_expr)

            try:
                postfix_expr = in2post(infix_expr)
                print("postfix:", postfix_expr)

                result = eval_postfix(postfix_expr)
                print("answer:", result)
                print()
            except (SyntaxError, ValueError) as e:
                print(f"Error: {e}")
                print()


if __name__ == "__main__":
    main()
