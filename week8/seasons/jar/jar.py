import sys

class Jar:
    def __init__(self, capacity=-1):
        if capacity < 0:
            raise ValueError("Capacity is wrong")

    def __str__(self):
        ...

    def deposit(self, n):
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n

def main():
    jar = Jar()

if __name__ == "__main__":
    main()
