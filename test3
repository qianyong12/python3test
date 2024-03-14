from typing import List
class Solution:
    def exist(self, board, word):
        def dfs(row, col, index):
            # 如果索引已经达到单词的长度，表示已经找到了匹配的单词
            if index == len(word):
                return True
            # 检查边界条件，如果越界，返回False
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            # 如果当前字符是通配符 "?"，尝试匹配下一个字符
            if board[row][col] == "?":
                board[row][col] = "#"
                found = (
                        dfs(row - 1, col, index + 1)
                        or dfs(row + 1, col, index + 1)
                        or dfs(row, col - 1, index + 1)
                        or dfs(row, col + 1, index + 1)
                )
                board[row][col] = "?"
                return found
            # 如果当前字符不匹配，返回False
            if board[row][col] != word[index]:
                return False
            # 临时将当前字符标记为已访问
            temp = board[row][col]
            board[row][col] = "#"
            # 递归探索上、下、左、右四个方向
            found = (
                    dfs(row - 1, col, index + 1)
                    or dfs(row + 1, col, index + 1)
                    or dfs(row, col - 1, index + 1)
                    or dfs(row, col + 1, index + 1)
            )
            # 恢复当前字符为未访问状态
            board[row][col] = temp
            return found
        # 遍历网格中的每个字符，作为起始点尝试开始搜索
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True
        return False
    def get_num_words(self, char_matrix: List[List[str]], words: List[str]) -> int:
        count = 0
        # 在此添加你的代码
        for word in words:
            if self.exist(char_matrix, word):
                count += 1
        return count

if __name__ == "__main__":
    rows, cols = map(int, input().strip().split())
    char_matrix = [list(map(str, input().strip())) for _ in range(rows)]
    num = int(input().strip())
    words = list(map(str, input().strip().split()))
    function = Solution()
    results = function.get_num_words(char_matrix, words)
    #results = function.get_num_words(char_matrix, words)
    print(char_matrix)
    print(results)
'''
单词匹配输入示例
3 3
abc
def
ghl
3
abehl deb ae
'''
