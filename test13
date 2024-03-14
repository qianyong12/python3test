def func(matric: list, word: str, posx, posy):
    if posx is None:
        ans = False
        for x, m in enumerate(matric):
            for y,i in enumerate(m):
                if i == word[0]:
                    if len(word) == 1:
                        return True
                    matric[x][y] = '#'
                    ans = func(matric, word[1:], x + 1, y) | \
                          func(matric, word[1:], x - 1, y) | \
                          func(matric, word[1:], x, y + 1) | \
                          func(matric, word[1:], x, y - 1) | ans
                    matric[x][y] = word[0]
        return ans
    else:
        if posx >= len(matric) or posx < 0 or posy >= len(matric[0]) or posy < 0:
            return False
        if matric[posx][posy] == word[0]:
            if len(word) == 1:
                return True
            matric[posx][posy] = '#'
            ans = func(matric, word[1:], posx + 1, posy) | \
                func(matric, word[1:], posx - 1, posy) | \
                func(matric, word[1:], posx, posy + 1) | \
                func(matric, word[1:], posx, posy - 1)
            matric[posx][posy] = word[0]
            return ans
        else:
            return False

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    word = input()
    matric = []
    for _ in range(n):
        l = []
        for a in input():
            l.append(a)
        matric.append(l)
    if func(matric, word, None, None):
        print('YES')
    else:
        print('NO')
'''
3 3
abc
bba
aac
abb
'''
