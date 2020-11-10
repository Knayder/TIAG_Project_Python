
def sz_pol(A, sz, key = lambda x: x):
    if len(A) == 0: return 0
    a, b = 0, len(A) - 1
    while b - a > 1:
        j = (a + b) // 2
        if key(A[j]) == sz: return j
        if key(A[j]) > sz: b = j
        else: a = j
    if sz > key(A[b]): return b + 1
    return b

def war_tab(A): #O(n*log(k))
    """ 
    z surowej tablicy buduje tablice wartości, 
    gdzie element to [wartosc, ilosc], 
    posortowane wdł. wartosci rosnąco 
    """
    newtab = [[A[0], 1]]
    for i in A[1:]:
        j = sz_pol(newtab, i, lambda x: x[0])
        if newtab[j][0] == i: newtab[j][1] += 1
        else: newtab.insert(j, [i, 1])
    return newtab


class Stock:
    def __init__(self):
        self.qtab = []
    def size(self):
        return len(self.qtab)
    def push(self, val):
        self.qtab.insert(0, val)
    def pull(self):
        v = self.qtab[0]
        self.qtab = self.qtab[1:]
        return v
    def head(self):
        return self.qtab[0]

class Queue:
   def __init__(self):
      self.qtab = []
   def size(self):
      return len(self.qtab)
   def push(self, val):
      self.qtab.append(val)
   def pull(self):
      v = self.qtab[0]
      self.qtab = self.qtab[1:]
      return v

class PriorityQueue:
    def __init__(self, keys = 0):
        self.qtab = []
        self.keys = keys
    def size(self):
        return len(self.qtab)
    def push(self, val, prio):
        self.qtab.insert(sz_pol(self.qtab, prio, key = lambda x: x[1]), [val, prio])
    def pull(self):
        if self.keys == 0:
            v = self.qtab[0]
            self.qtab = self.qtab[1:]
        else:
            v = self.qtab[len(self.qtab) - 1]
            del self.qtab[len(self.qtab) - 1]
        return v
    def __str__(self):
        return str(self.qtab)
    def __repr__(self):
        return str(self)
    def head(self):
        return self.qtab[0]


class BSTNode:
    def __init__(self, key, value, color = "red"):
        self.left = None
        self.right = None
        self.parent = None
        self.deleted = False
        self.key = key
        self.value = value
        self.color = color

class BSTDict:
    def __init__( self ):
        self.tree = None


    def insert( self, key, value ):
        if self.tree == None:
            self.tree = BSTNode(key, value)
            return
        node = self.tree
        while key != node.key:
            if key > node.key:
                if node.right == None:
                    node.right = BSTNode(key, value)
                    return
                node = node.right
            else:
                if node.left == None:
                    node.left = BSTNode(key, value)
                    return
                node = node.left
        node.value = value
    
    def find_succesor(self, node):
        if node.right == None: return node.left
        if node.left == None: return node.right
        suc = node.right
        if suc.left == None:
            suc.left = node.left
            return suc
        while suc.left.left != None: suc = suc.left
        node.key = suc.left.key
        node.value = suc.left.value
        suc.left = None
        return node
    
    def remove( self, key ):
        node = self.tree
        while key != node.right.key or key != node.left.key:
            if key > node.key:
                if node.right == None: return
            node = node.right
        else:
            if node.left == None: return
            node = node.left
        if key == node.right.key:
            node.right = self.find_succesor(node.right)
        else: node.left = self.find_succesor(node.left)

class Matrix:
    def __init__(self, A):
        self.A = A
        self.y = len(A)
        self.x = max(map(len, A))
    def __abs__(self):
        if self.x != self.y: raise ValueError("Macierz niekwadratowa!")
        suma = 0
        for i in range(self.y):
            iloczyn = 1
            for j in range(self.y):
                try:
                    iloczyn *= self.A[j][(j + i) % self.x]
                except IndexError: iloczyn = 0
            suma += iloczyn
        for i in range(self.y):
            iloczyn = 1
            for j in range(self.y):
                try:
                    iloczyn *= self.A[j][((self.x - j) - i) % self.x]
                except IndexError: iloczyn = 0
            suma -= iloczyn
        return suma
    
class BST_prze_node:
    def __init__(self, span, delta):
        self.span = span
        self.N = []
        if span[1] - span[0] > delta:
            self.right = BST_prze_node([(span[0] + span[1])//2, span[1]], delta)
            self.left = BST_prze_node([span[0], (span[0] + span[1])//2], delta)
            self.leaf = False
        else: self.leaf = True
    def __and__(self, other):
        if other is BST_prze_node: sp = other.span
        else: sp = other
        odp = [ max([sp, self.span], key = lambda x: x[0])[0], min([sp, self.span], key = lambda x: x[1])[1]]
        if odp[0] >= odp[1]: return None
        return odp
    def __iadd__(self, other):
        if (self & other) == self.span:
            self.N.append(other)
            return self
        if self.leaf:
            return self
        if (self.right & other) != None: self.right += other
        if (self.left & other) != None: self.left += other
        return self
    def __isub__(self, other):
        if (self & other) == self.span:
            try:
                self.N.remove(other)
            except ValueError: None
            return self
        if self.leaf:
            return self
        if (self.right & other) != None: self.right -= other
        if (self.left & other) != None: self.left -= other
        return self
    def __repr__(self):
        return str(self.span)
    def __str__(self):
        return str(self.span)

class BST_przedzialow:
    def __init__(self, span, delta = 1):
        self.root = BST_prze_node(span, delta)
    
    def __iadd__(self, other):
        self.root += other
        return self
    def __isub__(self, other):
        self.root -= other
        return self
    def __repr__(self):
        def rek(v, tab):
            for i in v.N:
                if i not in tab: tab.append(i)
            if not v.leaf:
                rek(v.left, tab)
                rek(v.right, tab)
        tab = []
        rek(self.root, tab)
        return str(tab)



class vertex:
    def __init__(self, N, _id = None):
        self.N = N
        self._id = _id
    def __str__(self):
        return str(self._id)
    def __lt__(self, other):
        return self._id < other._id
    def __gt__(self, other):
        return self._id > other._id
    def __repr__(self):
        return str(self._id)# + " : " + str([str(i) for i in self.N])
    

def ToDo(x, i):
    x.time = i

def DFS_t(G, key_n = lambda x: x.N, to_do = ToDo):
    i = [0]
    for v in G: v.visited = False
    def DFS(V, i):
        for v in key_n(V):
            if not v.visited:
                v.visited = True
                DFS(v, i)
        to_do(V, i[0])
        i[0] += 1
    for v in G:
        if not v.visited: DFS(v, i)
    for v in G:
        del v.visited
    return None

def reverse(G, key_n = lambda x: x.N, key_add = lambda x, v: x.N.append(v), key_it = list):
    A = [vertex(key_it([]), i._id) for i in G]
    for i in G:
        for v in key_n(i):
            d = min(filter(lambda x: v._id == x._id, A))
            k = min(filter(lambda x: i._id == x._id, A))
            key_add(d, k)
    return A

def konst_NDG_lista_S(A):
    G = [vertex([], i) for i in range(len(A))]
    for v in range(len(G)):
        for i in A[G[v]._id]:
            if G[i] not in G[v].N: G[v].N.append(G[i])
            if G[v] not in G[i].N: G[i].N.append(G[v])
    return G

def NDWG_konst_list(A):
    G = [vertex([], i) for i in range(len(A) + 1)]
    for i in range(len(G)): G[i].N = [[G[v[0]], v[1]] for v in A[i]]
    return G

def NDWG_konst_mat(A):
    G = [vertex([], i) for i in range(len(A))]
    G.sort(key = lambda x: x._id)
    for i in range(len(A)): 
        for j in range(len(A[i])):
            G[i].N.append((G[A[i][j][0]], A[i][j][1]))
            G[A[i][j][0]].N.append((G[i], A[i][j][1]))
    return G


def BFS(G, Start, End):
    def trasa(x):
        Trass = []
        while x != None:
            Trass += [x]
            x = x.parent
        return Trass[::-1]
    Q = PriorityQueue()
    for v in G: v.visited = False
    Q.push([G[Start], None], 0)
    while Q.size() > 0:
        n = Q.pull()
        v = n[0][0]
        if v.visited: continue
        v.parent = n[0][1]
        v.dist = n[1]
        v.visited = True
        if v == G[End]: return [trasa(v), v.dist]
        for i in v.N:
            if not i[0].visited: Q.push([i[0], v], n[1] + i[1])
    return None
