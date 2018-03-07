import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.add(1).add(2).add(3)

    def test_empty_list(self):
        self.ll = LinkedList()
        self.assertTrue(self.ll.isEmpty())
        self.assertEqual(self.ll.length, 0)
    
    def test_add_items(self):
        self.ll = LinkedList()
        self.assertEqual(str(self.ll), 'None')
        self.assertEqual(self.ll.length, 0)
        self.ll.add(1)
        self.assertEqual(str(self.ll), '1 -> None')
        self.assertEqual(self.ll.length, 1)
        self.ll.add(2)
        self.assertEqual(str(self.ll), '2 -> 1 -> None')
        self.assertEqual(self.ll.length, 2)
        self.ll.add(3)
        self.assertEqual(str(self.ll), '3 -> 2 -> 1 -> None')
        self.assertEqual(self.ll.length, 3)

    def test_pop_item(self):
        self.assertEqual(self.ll.pop(), 3)
        self.assertEqual(self.ll.length, 2)
        self.assertEqual(str(self.ll), '2 -> 1 -> None')

        self.assertEqual(self.ll.pop(), 2)
        self.assertEqual(self.ll.length, 1)
        self.assertEqual(str(self.ll), '1 -> None')

        self.assertEqual(self.ll.pop(), 1)
        self.assertEqual(self.ll.length, 0)
        self.assertEqual(str(self.ll), 'None')

    def test_get_item(self):
        self.assertEqual(self.ll[0], 3)
        self.assertEqual(self.ll[1], 2)
        self.assertEqual(self.ll[2], 1)
        with self.assertRaises(IndexError):
            self.ll[3]

    def test_search_item(self):
        self.assertTrue(self.ll.search(1))
        self.assertTrue(self.ll.search(2))
        self.assertTrue(self.ll.search(3))
        self.assertFalse(self.ll.search(0))

    def test_index_item(self):
        self.assertEqual(self.ll.index(1), 2)
        self.assertEqual(self.ll.index(2), 1)
        self.assertEqual(self.ll.index(3), 0)
        self.assertEqual(self.ll.index(0), -1)

    def test_remove_exist_item(self):
        self.ll.remove(2)
        self.assertEqual(str(self.ll), '3 -> 1 -> None')
        self.ll.remove(3)
        self.assertEqual(str(self.ll), '1 -> None')
        self.ll.remove(1)
        self.assertEqual(str(self.ll), 'None')

    def test_remove_not_exist_item(self):
        self.ll.remove(0)
        self.assertEqual(str(self.ll), '3 -> 2 -> 1 -> None')
        self.ll.remove(4)
        self.assertEqual(str(self.ll), '3 -> 2 -> 1 -> None')

if __name__ == '__main__':
    unittest.main()
