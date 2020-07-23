import time

class STimer(object):
    def __init__(self):
        self.max_depth = 20
        self.cur_depth = -1
        self.cur_name = [None] * self.max_depth
        self.stack = []
        for i in range(self.max_depth):
            self.stack.append({})

    def TIC(self, name):
        self.cur_depth = self.cur_depth + 1
        self.cur_name[self.cur_depth] = name
        if(self.cur_depth == self.max_depth):
            print("STimer max_depth (20) reached. Ignore section '{}'".format(name))
            return
        print("start:", name, self.cur_depth)
        '''get cur time '''
        st = time.perf_counter()
        d = self.stack[self.cur_depth]
        c = d.get(name)
        if(c == None):
          d[name] = [1, st, 0] # cnt, cur_start, total, subsection
        else:
          c[0] = c[0] + 1
          c[1] = st 

    def TOC(self):
        depth = self.cur_depth
        if(depth < 0):
          print("STimer: incorrect sequence of TIC/TOC calls")
          return
        if(depth >= self.max_depth):
          print("STimer: cur_depth is still to big: {}".format(depth))
          self.cur_depth = self.cur_depth - 1
          return
        name = self.cur_name[depth]
        if(name == None or name == ""):
          print("STimer: cur_name is None. It looks strange")
          self.cur_depth = self.cur_depth - 1
          return
        '''get cur time '''
        st = time.perf_counter()
        d = self.stack[self.cur_depth]
        c = d.get(name)
        c[2] = c[2] + (st - c[1])
        c[1] = 0
        print("exit section", name)
        self.cur_depth = self.cur_depth - 1

    def print_stack(self):
        print("===== Stack =====")
        print(self.stack)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("See you!")


if (__name__ == "__main__"):
    t = STimer()
    t.TIC("A")
    t.TIC("B1")
    time.sleep(1)
    t.TOC()
    t.TIC("B2")
    time.sleep(2)
    t.TOC()

    t.TOC()
    for i in range(3):
       t.TIC("Loop")
       time.sleep(1)
       t.TOC()

    t.print_stack()
