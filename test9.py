# If you need to import additional packages or classes, please import here.
def func():
    a, b = map(int, input().strip().split())
    if a < b:
        print(-1)
    elif a < b + 7:
        print(0)
    else:
        if a // 8 > b:
            print(b - 1)
        elif a // 8 < b:
            if a % 8 > b - a // 8:
                if a % 8 == 4 and b - a // 8 == 1:
                    print(b - 2)
                else:
                    print(a // 8)
            else:
                print(a // 8 - 1)
        else:
            print(a // 8)


# please define the python3 input here. For example: a,b = map(int, input().strip().split())

# please finish the function body here.

# please define the python3 output here. For example: print().

if __name__ == "__main__":
    func()
