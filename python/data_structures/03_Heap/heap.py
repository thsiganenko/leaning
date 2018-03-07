class MaxHeap:
    """Структура данных: Куча или двоичная куча

       Упорядочивание кучи реализовано с помощью рекурсии
       В конструктор добавлена возможность создавать кучу на основе объекта
       типа список, кортеж, множество. Если объект не передан, то будет
       создана пустая куча.

       Методы:
           add() - добавление нового элемента в кучу
           sort_heap() - упорядочивание кучи
           get_max() - извлечение максимального элемента из кучи
           export_array() - добавление массива в кучу
           __str__() - вывод кучи в виде строки
           __len__() - получение количества элементов в куче

    """

    def __init__(self, data=None):
        self.heap = []
        if data and isinstance(data, (list, tuple, set)):
            self.export_array(data)

    def add(self, element):
        """Добавляет новый элемент в кучу"""
        if not isinstance(element, (int, float, str)):
            raise ValueError('Аргумент на является скалярным значением')

        if self.heap and type(self.heap[0]) != type(element):
            msg = 'В кучу с элементами типа {0} не может быть добавлен {1}'
            raise TypeError(msg.format(type(self.heap[0]), type(element)))

        self.heap.append(element)
        child = len(self.heap) - 1
        parent = (child - 1) // 2
        while child > 0 and self.heap[child] > self.heap[parent]:
            self.heap[child], self.heap[parent] = self.heap[parent], \
                                                  self.heap[child]
            child = parent
            parent = (child - 1) // 2

    def export_array(self, iterable):
        """Добавляет элементы в кучу из итерируемого объекта"""
        for item in iterable:
            self.add(item)

    def sort_heap(self, parent):
        """Упорядочивает кучу"""
        left = parent * 2 + 1
        right = parent * 2 + 2
        lenght = len(self.heap)

        if left < lenght:
            if self.heap[left] > self.heap[parent]:
                self.heap[parent], self.heap[left] = self.heap[left], \
                                                     self.heap[parent]
                self.sort_heap(left)

        if right < lenght:
            if self.heap[right] > self.heap[parent]:
                self.heap[parent], self.heap[right] = self.heap[right], \
                                                      self.heap[parent]
                self.sort_heap(right)

    def get_max(self):
        """Возвращает максимальный элемент и удаляет его из кучи"""
        if self.heap:
            if len(self.heap) == 1:
                return self.heap.pop()

            max_element = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.sort_heap(0)

            return max_element

    def __str__(self):
        lenght = len(self.heap)
        i = 0
        k = 1
        output = []
        while i < lenght:
            while i < k and i < lenght:
                output.append(str(self.heap[i]) + ' ')
                i += 1
            k = k * 2 + 1

        return '\n'.join(output)

    def __len__(self):
        return len(self.heap)
