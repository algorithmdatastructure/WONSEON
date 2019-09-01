class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._data = []
        self._front = 0
        self._size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self._data[self._front]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self._size:
            return False
        else : return True
