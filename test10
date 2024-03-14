from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        dp = [0 for _ in range(0, len(word))]  # 列表初始化简单写法
        for i in range(0, len(word)):
            if i == 0:
                if not int(word[0]) % m:
                    dp.append(1)
                else:
                    dp.append(0)
            elif dp[i - 1]:
                if not int(word[i]) % m:
                    dp.append(1)
                else:
                    dp.append(0)
            elif not int(word[0:i + 1]) % m:
                dp.append(1)
            else:
                dp.append(0)
        return dp
