# If you need to import additional packages or classes, please import here.

def func():
    num = int(input())
    str_test = []
    for i in range(num):
        str_test.append(list(map(str, input().split())))
    str_test = sorted(str_test, key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3]), x[0]))
    for i in str_test:
        print(' '.join(i))


if __name__ == "__main__":
    func()
