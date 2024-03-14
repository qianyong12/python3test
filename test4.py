from typing import List


class Solution:
    def process(self, array: List) -> bool:
        for ind, num in enumerate(array):
            if ind % 2:
                # num = 1
                array[ind] = 1
        return True


if __name__ == '__main__':
    s = Solution()
    a = [0 for _ in range(0, 10)]
    print(a)
    s.process(a)  # 表现出函数调用对参数的修改
    print(a)
