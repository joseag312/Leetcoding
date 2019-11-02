def testing():
    s = r'([)]'
    my_stack = []

    for i, c in enumerate(s):
        my_stack += ']' if c == '[' else ''
        my_stack += '}' if c == '{' else ''
        my_stack += ')' if c == '(' else ''

        if c  == ']' or c == ')' or c == '}':
            if my_stack[-1] == c:
                my_stack.pop()
            else:
                return (False)
    else:
        return(True)

print (testing())