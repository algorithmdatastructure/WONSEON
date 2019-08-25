class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._data = [None] * k
        self._size = 0
        self._front = 0
        self._last = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        self._size += 1

        if self._size <= len(self._data):
            avail = (self._front + self._size - 2) % len(self._data)
            data[avail] = value
            return True
        else:
            self._size -= 1
            return False


    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        self._size += 1

        if self._size <= len(self._data):
            self._last = (self._front + self._size - 2) % len(self._data)
            data[self._last] = value
            return True
        else:
            self._size -= 1
            return False

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """


    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """


    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """


    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """


    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """


    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
