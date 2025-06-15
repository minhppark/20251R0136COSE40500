def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    output = []
    stack = []
    tokens = expression.split()
    print(f"Infix expression: {expression}")
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence.get(stack[-1], 0):
                output.append(stack.pop())
            stack.append(token)
        print(f"Token: {token}, Stack: {stack}, Output: {output}")
    while stack:
        output.append(stack.pop())
    print(f"Postfix expression: {' '.join(output)}")
    return ' '.join(output)

if __name__ == "__main__":
    expr = "A * B + C * D"
    infix_to_postfix(expr)