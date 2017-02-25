class LinkedList:
    def __init__(self):
        self._link=None

    def __str__(self):
        p = self._link
        s = ''
        while p:
            s += str(p[0]) + ' '
            p = p[1]
        return s

    def push_front(self, data):
        self._link = [data, self._link]

    def pop(self,data):
        p = self._link
        if p == None:
            return None
        #elif p[1]==None:
         #   k = None
          #  if p[0]==data:
           #     k = data
            #    p = p[1]
            #return k
        else:
            k = None
            f = p
            while p and p[0]!=data:
                f = p
                p = p[1]
            if p and p[0]==data:
                k = data
                if f!=p:
                    f[1] = p[1]
                else:
                    self._link = p[1]
            return k
