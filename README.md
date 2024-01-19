# Science-Fiction-Library-Program
Creating a library management system for the Science Fiction Library using various data structures.

SciFiLi Program Description:
Each of the following tasks is most efficiently accomplished by using a data
structure, sometimes the same one and sometimes not. You need to decide which will be most
appropriate for each task.

  1. The day starts with the program reading the file of books and storing them internally in a single data structure.
  2. The librarian needs to be able to search by title or author.
      a.  If searching by author, output should list all books by that author.
      b. The search should also tell if the book is checked out or not.
  3. The librarian needs to be able to check in/out books.
  a. Note: When people return books, they stick a pile in front of the librarian. Emulate the return process.
  4. At the end of the day, when the librarian quits the program, output all books to a file (alphabetically by title) and if they’re checked in or out.
  5. If the library catches fire, the most important books need to be rescued first! Output a list of books (checked in only) that need to be rescued in order of importance.
  
  Create a simple text-based or GUI menu to allow the user to select each task.


About the input file:
Each book has one line in the text file showing all of the relevant information. 
For example:
  Watership Down, AdamsR, 0, 7
Each piece of information is separated by “, “ and is in a specific order:
  Title, Author, CheckInStatus, Priority
  
Title and Author are strings. CheckInStatus is a Boolean (1 = in, 0 = out). Priority is an integer, with 1
being the most important book in the library, 2 the next most important, etc.
