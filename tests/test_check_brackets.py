import unittest
from main import check_brackets
from parameterized import parameterized

FIXTURES = [
        ('(((([{}]))))', 'Сбалансировано'),
        ('[([])((([[[]]])))]{()}', 'Сбалансировано'),
        ('{{[()]}}', 'Сбалансировано'),
        ('}{}', 'Несбалансированно или неподдерживаемый тип скобки'),
        ('тест', 'Несбалансированно или неподдерживаемый тип скобки'),
        ('{{[(])]}}', 'Несбалансированно'),
        ('[[{())}]', 'Несбалансированно'),
    ]

class CheckBrackets(unittest.TestCase):

    @parameterized.expand(FIXTURES)
    def test_check_brackets(self, bracket_list, exp_result):
        result = check_brackets(bracket_list)
        self.assertEqual(result, exp_result)

