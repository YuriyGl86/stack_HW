from stack import Stack, Element


brackets_pair = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


def check_brackets(brackets):
    stack = Stack()
    for bracket in brackets:
        if bracket in '({[<':
            stack.push(Element(bracket))
        elif bracket in ')}]>' and stack.size() > 0:
            if stack.peek() != brackets_pair[bracket]:
                return 'Несбалансированно'


