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
            if stack.peek().data != brackets_pair[bracket]:
                return 'Несбалансированно'
            else:
                stack.pop()
        else:
            return 'Несбалансированно или неподдерживаемый тип скобки'

    return 'Сбалансировано' if stack.size() == 0 else 'Несбалансированно'


