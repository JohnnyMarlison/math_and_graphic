class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def __eq__(self, item):
        return self.items == item

    def __it__(self, item):
        return self.items < item

    def __gt__(self, item):
        return item > self.items

    def __ge__(self, item):
        return self.items >= item

    def __le__(self, item):
        return self.items <= item

def main():
    d1 = Deque()
    d2 = Deque()
    print(d1.isEmpty())
    d1.addRear(4)
    d1.addRear('dog')
    d1.addFront('cat')
    d1.addFront(True)
    print("equivalence -", d1 == d2)
    print("larger d1 -", d1 > d2)
    print("less d1 -", d1 < d2)
    print("ge -", d1 >= d2)
    print("le -", d1 <= d2)
    print(len(d1))
    print(d1.isEmpty())
    d1.addRear(8.4)
    print(d1.removeRear())
    print(d1.removeFront())


if __name__ == "__main__":
    main()
