#SCI-FI LIBRARY PROGRAM
#DARRI STUBER

from scifi_binTree import binaryTree
from scifi_nodes import scifi_BNode
from scifi_nodes import scifi_LNode
from Queue_Stack_Classes import Stack
from Queue_Stack_Classes import priorityQueue


#PART ONE:  The day starts with the program reading the file of books and storing them internally in a single data structure
file = open("SciFiLiBooks.txt") #import file
#each line in file is: Title, Author, Check in status (CIS), Priority
titleTree = binaryTree()
for line in file: #for line in the read in file
    line = line.strip('') #remove extra characters
    splitline = line.split(',') #split line into a list based on commas (read as csv)
    #save characteristics from split line to create binary tree node
    title = splitline[0]
    author = splitline[1]
    cis = int(splitline[2])
    priority = int(splitline[3])
    node = scifi_BNode(title, author, cis, priority)
    titleTree.insert(node)

#create menu
while True: 
    print('Choose what you would like to do by entering a number: ')
    print('\t'+'Enter 1 to search for books by title or author')
    print('\t'+'Enter 2 to check books in or out')
    print('\t'+'Enter 3 to get an alphabetical list of books with check-in status')
    print('\t'+'Enter 4 to get a list of available books in order of priority')
    activation = int(input())
    #PART TWO: The librarian needs to be able to search by title or author
        #If searching by author, output should list all books by that author
        #The search should also tell if the book is checked out or not.

    if activation == 1: 
        while True:
            search_method = input('Would you like to search by title or author? ').lower()
            if search_method == 'title':
                what = input('Type the title of the book you would like to find: ')
                if titleTree.search(what) != None:
                    status = titleTree.getStatus(what)
                    author = titleTree.findAuthor(what)
                    print('\t'+'{} by {}: {}'.format(what,author,status))
                else:
                    print('\t' + 'Not found')
            elif search_method == 'author':
                #the file has a space before the author name, must add to properly search
                wantedAuthor = str(' '+ input('Provide the author name to see their books and availability: '))
                Alist = titleTree.authorList(wantedAuthor)
                print('Books by{}'.format(wantedAuthor))
                for t in Alist:
                    status = titleTree.getStatus(t)
                    print('\t' +'{} (Status = {})'.format(t,status))
            else:
                print('Invalid Input')
            y = input('Do you have another search (yes/no)? ').lower()
            if y == 'no':
                break
            
        print()

    if activation == 2:
    #PART THREE: The librarian needs to be able to check in/out books (Evaluate the return process)
        #CHECK IN BOOKS: 
        #create stack for books to be returned and checked in
        #for each book in stack
            #change book status in title tree to returned (create method for this)
            #remove from stack
        #CHECK OUT BOOKS:
            #same as above
    #CHECK IN BOOKS
        checkInList = Stack()
        while True: 
            opt = input('Would you like to return or checkout a book? (return/checkout) ').lower()
            if opt == 'return':
                while True:
                    given = input('What book are you returning? ')
                    node = scifi_LNode(given)
                    checkInList.push(node)
                    y = input('Do you have another book to return (yes/no)? ').lower()
                    if y == 'no':
                        break

                while checkInList.peek() != None:
                    book = checkInList.peek()
                    #node = scifi_LNode(book)
                    #node = scifi_LNode(book)
                    print(titleTree.checkIn(book.data))
                    checkInList.pop()
                #CHECK OUT BOOKS
            
            elif opt == 'checkout':
                checkOutList = Stack()
                while True:
                    given = input('What book are you checking out? ')
                    node = scifi_LNode(given)
                    checkOutList.push(node)
                    y = input('Do you have another book to check out (yes/no)? ').lower()
                    if y == 'no':
                        break

                while checkOutList.peek() != None:
                    book = checkOutList.peek()
                    print(titleTree.checkOut(book.data))
                    checkOutList.pop()
            
            opt2 = input('Would you like to continue (yes/no)? ').lower()
            if opt2 == 'no':
                break

    
    print()
            

    if activation == 3:
        #PART FOUR: At the end of the day, when the librarian quits the program, output all books to a file (alphabetically by title) and if they’re checked in or out.
        #In order list of title tree (somehow attach if they are checked in or out)
        # file code from geeks for geeks https://www.geeksforgeeks.org/writing-to-file-in-python/

        allBooks = titleTree.traverseInOrder()
        array = []
        for t in allBooks:
            status = titleTree.getStatus(t)
            line = [t, status]
            array.append(line)
            
        with open('scifi_file.txt', 'w') as f:
            for row in array:
                new = '{} - {}'.format(row[0],row[1])
                f.write(new + '\n')
        with open('scifi_file.txt', 'r+') as file1:
           print(file1.read())
        print()

    if activation == 4:
        #PART FIVE: If the library catches fire, the most important books need to be rescued first! Output a list of books (checked in only – no need to rescue a book that isn’t there) that need to be rescued in order of importance
        #priority queue
        #if it is checked out pass
        #add to queue based on priority then title
        #output

        pQueue = priorityQueue()
        for book in titleTree.traverseInOrder():
            if titleTree.getStatus(book) == 'Checked out':
                pass
            else:
                p = titleTree.getPriority(book)
                pQueue.insertPQ(book, p)

        pQueue.goBeginning()
        priorityOutput = []
        while pQueue.isEnd() == False:
            removed = pQueue.dequeue()
            priorityOutput.append(removed)
            pQueue.goBeginning()
            
        pQueue.dequeue()
        arrayP = []
        
        for b in priorityOutput:
            line = [b.data, b.priority]
            arrayP.append(line)
        
        print('Checked-in books in order of priority: ')
        with open('scifi_priorityOutput.txt', 'w') as f:
            for row in arrayP:
                new = '{} (Priority = {})'.format(row[0],row[1])
                f.write('\t' + new + '\n')
                
        with open('scifi_priorityOutput.txt', 'r+') as file2:
           print(file2.read())
        print()
        
       
    exitDecision = input('Would you like to do something else from the menu(yes/no)? ').lower()
    if exitDecision == 'no':
        break
    print()      
                
