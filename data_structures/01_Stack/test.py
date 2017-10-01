import stack
import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = stack.Stack()

    def test_empty_stack_first(self):
        self.assertTrue(self.stack.isEmpty())
        self.assertEqual(len(self.stack), 0)

    def test_push_value_to_stack(self):
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 2)
        self.stack.push(3)
        self.assertEqual(len(self.stack), 3)

    def test_methon_peek(self):
        self.stack.push('a').push('b').push('c')
        self.assertEqual(self.stack.peek(), 'c')

    def test_len_stack(self):
        self.stack.push(1).push(2).push(3)
        self.assertFalse(self.stack.isEmpty())
        self.assertEqual(len(self.stack), 3)

    def test_pop_value_from_stack(self):
        self.stack.push(1).push(2).push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(len(self.stack), 0)
        self.assertTrue(self.stack.isEmpty())

    def test_exception(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

if __name__ == '__main__':
    unittest.main()
