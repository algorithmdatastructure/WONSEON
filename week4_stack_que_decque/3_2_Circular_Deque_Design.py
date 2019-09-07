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
        if self._size == len(self._data):
            return False

        self._data.insert(0, value)
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self._size == len(self._data):
            return False

        self._data.append(value)
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self._size:
            return False

        self._front = (self._front + 1) % len(self._data)
        self._data.pop(0)
        self._size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self._size:
            return False

        self._last = self._size - 1
        self._data.pop()
        self._size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self._size :
            return -1

        return self._data[self._front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self._size:
            return -1

        return self._data[self._last]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if not self._size :
            return False
        else : return True

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self._size == len(self._data) :
            return True
        else : return False
