class Stack:

    def __init__(self):
        self.top_element = None
        self.len_list = 0

    def isEmpty(self):
        return True if self.top_element is None else False

    def push(self, new_element):
        if not self.top_element:
            self.top_element = new_element
        else:
            new_element.prev = self.top_element
            self.top_element = new_element
        self.len_list += 1

    def pop(self):
        if self.top_element:
            pop_element = self.top_element
            self.top_element = pop_element.prev
            self.len_list -= 1
            return pop_element

    def peek(self):
        return self.top_element

    def size(self):
        return self.len_list


class Element:

    def __init__(self, data):
        self.data = data
        self.prev = None
