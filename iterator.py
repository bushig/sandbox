class Reverse:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        self.index = len(self.data)
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]


def main():
    reverse=Reverse('Abcdefg')
    print(reverse.index)
    for item in reverse:
        print(item)

    print(reverse.index)

    for item in reverse:
        print(item)

if __name__ == '__main__':
    main()