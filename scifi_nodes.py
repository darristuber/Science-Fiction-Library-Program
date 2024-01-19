### DARRI STUBER
## BINARY TREE NODE CLASS FOR SCIFILI
#data = title

# Node class for a binary tree
class scifi_BNode:
    def __init__(self, d=None, a=None, c=None, p=None, l=None, r=None):
        self._data = d
        self._author = a
        self._cis = c
        self._priority = p
        self._left = l
        self._right = r
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, d):
        self._data= d
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, a):
        self._author = a
    @property
    def cis(self):
        return self._cis
    @cis.setter
    def cis(self, c):
        self._cis = c
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self, p):
        self._priority = p
    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, l):
        self._left = l
    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, r):
        self._right = r
    
    def ImALeaf(self):
        if (self._left == None) and (self._right == None):
            return True
        return False
    
    def __str__(self):
        return str(self.title)
    
#Node class for linked list
class scifi_LNode:
    def __init__(self, d=None, p = None, l=None):
        self._data = d
        self._priority = p
        self._link = l

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, d):
        self._data = d
    @property
    def priority(self):
        return self._priority
    @priority.setter
    def priority(self, p):
        self._priority = p
    @property
    def link(self):
        return self._link
    @link.setter
    def link(self, l):
        self._link = l
