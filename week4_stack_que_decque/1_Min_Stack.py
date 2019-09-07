class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._data = []
        self._min = []

    def push(self, x: int) -> None:
        if len(self._min) == 0:
            self._min.append(x)
        else:
            if x <= self._min[-1]:
                self._min.append(x)
           
        self._data.append(x)

    def pop(self) -> None:
        if len(self._data) == 0 :
            raise Empty('Stack is empty')

        if self._data[-1] == self._min[-1]:
            self._min.pop()

        return self._data.pop()

    def top(self) -> int:
        if len(self._data) == 0 :
            raise Empty('Stack is empty')

        return self._data[-1]

    def getMin(self) -> int:
        if len(self._min) == 0 :
            raise Empty('Stack is empty')

        return self._min[-1]
