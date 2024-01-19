### DARRI STUBER
### \SCIFI LIBRARY BINARY TREE CLASS

from scifi_nodes import scifi_BNode

class binaryTree:
    def __init__(self, r = None, c = None):
        self._root = r
        self._curr = c
        self._numLevels = 0
    
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, n):
        self._root = n
    @property
    def curr(self):
        return self._curr
    @curr.setter
    def curr(self, n):
        self._curr = n
    
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False
    def isRoot(self):
        if self.curr == self.root:
            return True
        else:
            return False
    
    def isLeaf(self):
        if self.curr == None:
            return 'empty value passed - not leaf'
        if self.curr.left == None and self.curr.right == None:
            return True
        else:
            return False
    
    def getData(self):
        if self.curr == None:
            return None
        else:
            return self.curr.data
    def getAuthor(self):
        if self.author == None:
            return None
        else:
            return self.curr.author
    def setData(self, d):
        self.curr.data = d
        
    def goRoot(self):
        self.curr = self.root
    
    def goLeft(self):
        if self.curr == None:
            return None
        else:
            self.curr = self.curr.left
    
    def goRight(self):
        if self.curr == None:
            return None
        else:
            self.curr = self.curr.right
        
    def getMin(self):
        self.goRoot()
        if self.curr == None:
            return 'Empty list no minimum'
        while self.curr.left != None:
            self.goLeft()
        return self.getData()

    def getMax(self):
        self.goRoot()
        if self.curr == None:
            return 'Empty list no maximum'
        while self.curr.right != None:
            self.goRight()
        return self.getData()

    # recursive function to insert
    # only used inside binaryTree class!!!
    def insertNode(self, here, n, level = 0):
        if here == None:
            here = n
        else:
            if n.data < here.data:
                 here.left, level = self.insertNode(here.left, n)
            else:
                here.right, level = self.insertNode(here.right, n)
        level += 1
        return (here, level)
        
    # inserts a node (n)
    # This is the method you'll call outside of this class
    def insert(self, n):
        if self.isEmpty() == True:
            self.root = n
            self.curr = n
            self.numLevels = 1
        else:
            self.goRoot()
            self.curr, level = self.insertNode(self.curr, n)
            if level > self.numLevels:
                self.numLevels = level
            
    # does the actual counting
    # again, used only in-class
    def count(self, n):
         if n == None:
             return 0
         else:
             l = 1
             l += self.count(n.left);
             l += self.count(n.right);
             return l
            
    # use this outside of the class
    def getSize(self):
        return self.count(self.root)
    
    # next 2 methods find a node in the tree or returns None if not there
    def findIt(self, n, what):
        #print('what: {}'.format(what))
        #print('n.data: {}'.format(n.data))
        if n == None:
            return None # not found
        if n.data == what:
            return n
        
        elif what < n.data:
            return self.findIt(n.left, what)
        elif what > n.data:
            return self.findIt(n.right, what)
    def search(self, what):
        self.curr = self.findIt(self.root, what)
        return self.curr
    
    def getPriority(self, what):
        self.search(what)
        if self.curr.data != None:
            return self.curr.priority
    def getStatus(self, what):
        self.search(what)
        if self.curr.data != None:
            if self.curr.cis == 1:
                return('Available')
            elif self.curr.cis == 0:
                return('Checked Out')
    def findAuthor(self, what):
        self.search(what)
        if self.curr.data != None:
            return self.curr.author 
    def checkIn(self, what):
        self.search(what)
        if self.curr != None:
            if self.curr.cis == 1:
                return('{} is already here'.format(what))
            elif self.curr.cis == 0:
                self.curr.cis = 1
                return('{} is returned'.format(what))
    def checkOut(self, what):
        self.search(what)
        if self.curr != None:
            if self.curr.cis == 0:
                return('Book is not available to be checked out')
            elif self.curr.cis == 1:
                self.curr.cis = 0
                return('{} is now checked out'.format(what))
    #like find it but instead of finding what it finds the parent of what
    def findParent(self, n, what):

        if n.left.data == what: 
            return n
        elif n.right.data == what:
            return n
        elif what < n.data:
            return self.findParent(n.left, what)
        elif what > n.data:
            return self.findParent(n.right, what)
    def goParent(self): #def goParent(self, what = self.curr.data):
        self.curr = self.findParent(self.root, self.curr.data)
        return self.curr
    
    def remove(self, what):
        self.search(what) #find what we are looking for
        if self.search(what) == None: #if we cant find it we cant remove it
            return ('That value does not exist')
        temp = self.getData() # save data to replace leaf_loc with later
        remove_loc = self.curr #remove loc is original location of what, leaf_loc is the original location of the leaf we want to switch what data with
        if (self.isRoot()== True) and (self.isLeaf() == True): #if we only have one value in the tree it is now none
            self = None
            return 'Tree Emptied'
            
        if self.isLeaf() == True: #set parent in case it doesnt go to inner loop (because we dont need to find leaf node to switch)
            leaf_loc = self.curr #save location of node we want to put the remove data in before we delete
            self.goParent()
            parent = self.curr #save parent data location
            self.curr = leaf_loc
        while self.isLeaf() !=True: #find the leaf node where we will put remove data
            if self.curr.left != None: #go left once then all the way right
                self.goLeft()
                while self.curr.right != None:
                    self.goRight()

            else: #go right once and then all the way left in case it doesnt work the other way
                self.goRight()
                while self.curr.left != False:
                    self.goLeft()
                    
            #temp one - the data we want to remove
            #temp two - the data of the leaf (value we are putting in original node)
            temp2 = self.getData()
            leaf_loc = self.curr
            self.goParent() #save parent of leaf for later
            parent = self.curr
            self.curr = leaf_loc
            
            #make leaf node to what data
            self.setData(temp)#we are at the leaf node that we want to be our remove data, set data to what data
            
            
            #replace what data with leaf data
            self.curr = remove_loc
            self.setData(temp2) #set original node equal to leaf data
            
            #go back to leaf node so we exit the loop
            self.curr = leaf_loc
            
            
        target = self.getData() # data that we are removing, save for comparison later
        if self.isRoot() == True:
            self = None #empty the whole list our data only has one value 
        else: #remove leaf node with remove data
            self.curr = parent
            if self.curr.left.data == target:
                self.curr.left = None 
            elif self.curr.right.data == target:
                self.curr.right = None 
        
        

    
    ### traversal methods ###
    def inOrder(self, n):
        # n is self.curr (starts at root)
        #want left, node, right 
        s = []
        #add left to node
        if n.left != None: 
            if n.left.ImALeaf() == True:
                s.append(n.left.data)
            else: #left child is a parent, want to get that data
                for r in self.inOrder(n.left):
                    s.append(r)
                
        s.append(n.data) #add node data
            
       #add right to data
        if n.right != None: 
            if n.right.ImALeaf() == True:
                s.append(n.right.data)
            else: #right is parent we want those values
                for r in self.inOrder(n.right):
                    s.append(r)
        return(s)

    
    def traverseInOrder(self):
        self.goRoot()
        if self.curr == None:
            return "Empty Tree"
        return(self.inOrder(self.curr))
    
    def AinOrder(self, n, wantedAuthor):
        # n is self.curr (starts at root)
        #want left, node, right 
        titles = []
        #add left to node
       
        if n.left != None:
            if n.left.ImALeaf() == True:
                if n.left.author == wantedAuthor:
                    titles.append(n.left.data)
            else: #left child is a parent, want to get that data
                for book in self.AinOrder(n.left, wantedAuthor):
                    titles.append(book)
        if str(n.author) == str(wantedAuthor):
            titles.append(n.data) #add node data
            
       #add right to data
        if n.right != None:
            if n.right.ImALeaf() == True:
                if n.right.author == wantedAuthor:
                    titles.append(n.right.data)
            else: #right is parent we want those values
                for book in self.AinOrder(n.right, wantedAuthor):
                    titles.append(book)
        return(titles)
    def authorList(self, author):
        #starts with traverse in order
        #check if authuor matches
        #if author matches add title and checkout to line in array or list
        #once tree is completely went through print list of titles and checked out
        self.goRoot()
        if self.curr == None:
            return "No Books"
        return(self.AinOrder(self.curr, author))
    
    def PreOrder(self, n):
        # n is self.curr (starts at root)
        s = []
        s.append(n.data)
        
        #want node, left, right
        if n.left != None: 
            if n.left.ImALeaf() == True:
                s.append(n.left.data)
            else: #left child is a root
                for r in self.PreOrder(n.left):
                    s.append(r)
                
       #add right to data
        if n.right != None: 
            if n.right.ImALeaf() == True:
                s.append(n.right.data)
            else:
                for r in self.PreOrder(n.right):
                    s.append(r)
        return(s)
               
    def traversePreOrder(self):
        self.goRoot()
        if self.curr == None:
            return 'Empty Tree'
        return(self.PreOrder(self.curr))
        
        
    def PostOrder(self, n):
        # n is self.curr (starts at root)
        s = []
        #want left, right, node
        if n.left != None: 
            if n.left.ImALeaf() == True:
                s.append(n.left.data)
            else: #left child is a root
                for r in self.PostOrder(n.left):
                    s.append(r)
                
       #add right to data
        if n.right != None:
            if n.right.ImALeaf() == True:
                s.append(n.right.data)
            
            else:
                for r in self.PostOrder(n.right):
                    s.append(r)
                
        s.append(n.data)# str(n.data) #add node data
        return(s)
        
    def traversePostOrder(self):
        self.goRoot()
        if self.curr == None:
            return "Empty Tree"
        return(self.PostOrder(self.curr))
        
    # returns a string that when printed
    # shows the tree in tree form
    # for example:
    #         M
    #      F      T
    #    B   H  R   W
    
    #recursion to get the kids of a given node and record the level
    def getKids(self, loc, level = 1):
        ks = '' #create empty string
        tabs = self.numLevels - level #determine level of tabs for new level
        ks +='\t' *(tabs) #add the desired number of tabs to beginning of level
        if loc.left != None: #check to ensure left kid exists
            Left_kid = loc.left #get left data
            ks += str(Left_kid.data) # add left data
            left_babies = self.getKids(Left_kid, level + 1) #save left kids to add after right data
        else:
            left_babies = '' #just so left_babies is defined for later
        ks += '\t '*tabs # add tabs between left and right values
        if loc.right != None: 
            Right_kid = loc.right 
            ks += str(Right_kid.data) #add right data
            right_babies = self.getKids(Right_kid, level + 1) #get right kids for later
        else:
            right_babies = ''
        
        ks += '\n'*2 #add new lines
        ks += str(left_babies) #add left babies
        ks += str(right_babies) #add right babies
        return ks #return string
        
  
        return s
    def __str__(self):
        self.goRoot()
        if self.curr == None:
            return 'Empty Tree - cannot print'
        loc = self.curr
        
        kids = self.getKids(loc) #get next level data
        s = '\t '* self.numLevels #create right number of tabs for root to print
        s += str(loc.data) #add root to string
        s += '\n'*2 #add new lines
        s += kids #add kid values obtained from recursion
        
        return(s)
    
    
    
