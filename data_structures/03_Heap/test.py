#!/usr/bin/env python
from random import randint
from unittest import main
from unittest import TestCase
from heap import MaxHeap


class TestMaxHeap(TestCase):
    """Тест для структуры данных: Куча"""
    def test_base_case(self):
        """Простой тест кучи"""
        heap = MaxHeap()
        self.assertEqual(len(heap), 0)
        heap.add(1)
        self.assertEqual(len(heap), 1)
        heap.add(2)
        self.assertEqual(len(heap), 2)
        heap.add(3)
        self.assertEqual(len(heap), 3)
        self.assertEqual(heap.get_max(), 3)
        heap.add(7)
        heap.add(5)
        self.assertEqual(heap.get_max(), 7)
        self.assertEqual(heap.get_max(), 5)
        self.assertEqual(len(heap), 2)
        self.assertEqual(heap.get_max(), 2)
        self.assertEqual(heap.get_max(), 1)
        self.assertEqual(len(heap), 0)

    def test_exception(self):
        """Тест проверки возбуждения исключений"""
        heap = MaxHeap()
        with self.assertRaises(ValueError):
            heap.add([1, 2, 3])

        heap.add(1)
        with self.assertRaises(TypeError):
            heap.add('a')

    def test_initialization_with_iterable(self):
        """Тест проверки инициализации кучи с помощью последовательности"""
        data = ([1, 2, 3, 4, 5],
                (1, 2, 3, 4, 5),
                set((1, 2, 3, 4, 5)))
        for data_set in data:
            with self.subTest(data_set=data_set):
                heap = MaxHeap(data_set)
                self.assertEqual(len(heap), 5)
                for i in range(len(heap), 0, -1):
                    self.assertEqual(heap.get_max(), i)
                self.assertEqual(len(heap), 0)


if __name__ == '__main__':
    main()
