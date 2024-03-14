from typing import List

class Dir:
    def __init__(self):
        self.dir = {}

class FileSystem:
    def __init__(self):
        self.root = Dir()
        self.cur = self.root

    def make_dir(self, dir_name: str) -> bool:
        if dir_name in self.cur.dir:
            return False
        else:
            self.cur.dir[dir_name] = Dir()
            return True

    def create_file(self, file_name: str) -> bool:
        if file_name in self.cur.dir:
            return False
        else:
            self.cur.dir[file_name] = None
            return True

    def change_dir(self, path_name: str) -> bool:
        path = path_name.strip().split('/')
        if path[-1] == '':
            path = path[:-1]
        else:
            path = path
        now_pos = self.cur
        if len(path) == 0:
            return True
        elif len(path) == 1 and path[0] == '':
            # root
            self.cur = self.root
            return True
        elif path[0] == '':
            temp = self.root
            for name in path[1:]:
                if name in temp.dir.keys() and temp.dir[name]:
                    self.cur = temp.dir[name]
                    temp = self.cur
                else:
                    self.cur = now_pos
                    return False
        else:
            for name in path:
                if name in self.cur.dir.keys() and self.cur.dir[name]:
                    self.cur = self.cur.dir[name]
                else:
                    self.cur = now_pos
                    return False
        return True

    def remove(self, name: str) -> bool:
        if name in self.cur.dir:
            del self.cur.dir[name]
            return True
        else:
            return False

    def list_dir(self) -> List[str]:
        res_dir = []
        res_file = []

        for name in self.cur.dir.keys():
            if self.cur.dir[name]:
                res_dir.append(name)
            else:
                res_file.append(name)

        res_dir.sort(reverse=False)
        res_file.sort(reverse=False)

        return res_dir + res_file
