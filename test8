# 答题框内的代码仅为待实现代码，执行或提交代码时，仅包含待实现部分，不要包含其它代码。

class BrowserHistorySys:
    def __init__(self, homepage: str, max_count: int):
        self.cur = homepage
        self.max_cnt = max_count
        self.cnt = 1
        self.s = []
        self.ind = 1
        self.s.append(homepage)
        pass

    def visit(self, url: str) -> int:
        if url != self.cur:
            self.cur = url
            if self.ind == self.max_cnt:
                self.s = self.s[1:]
                indnext = self.ind
            else:
                indnext = self.ind + 1
            if self.ind < self.cnt:
                for i in range(self.ind, self.cnt):
                    self.s.pop()
                self.ind = indnext
                self.cnt = self.ind
                self.s.append(url)
                return self.cnt
            elif self.cnt < self.max_cnt:
                self.cnt = self.cnt + 1
            self.ind = indnext
            self.s.append(url)
        return self.cnt

    def back(self) -> str:
        if self.ind - 1:
            self.ind = self.ind - 1
            self.cur = self.s[self.ind - 1]
        return self.cur

    def forward(self) -> str:
        if self.ind != self.cnt:
            self.ind = self.ind + 1
            self.cur = self.s[self.ind - 1]
        return self.cur
