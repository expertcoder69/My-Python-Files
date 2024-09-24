stud={}
books=[{"id":1,"name":"Wings Of Fire","author":"- APJ Abdul Kalam","available":True},
       {"id":2,"name":"Great Expectations","author":"- Charles Dickens","available":True},
       {"id":3,"name":"And Then There Were None","author":"- Agatha Christie","available":True},
       {"id":4,"name":"Hamlet","author":"- Shakespeare","available":True},
       {"id":5,"name":"War and Peace","author":"- Leo Tolstoy","available":True},
       {"id":6,"name":"God of Small Things","author":"- Arundhati Roy","available":True},
       {"id":7,"name":"Crime and Punishment","author":"- Dostoevsky","available":True},
       {"id":8,"name":"The Stand","author":"- Stephen King","available":True},
       {"id":9,"name":"Inferno","author":"- Dan Brown","available":True},
       {"id":10,"name":"Persuasion","author":"- Jane Austen","available":True}]
print("\n    WELCOME TO LIBRARY MANAGEMENT SYSTEM   ")
print("-----------------------------------------------")
name=input("Enter your name: ")
dict1={"student name":name}
while True:
    print("\n    WELCOME TO LIBRARY MANAGEMENT SYSTEM   ")
    print("-----------------------------------------------")
    print("Enter 1. To display available books")
    print("Enter 2. To borrow a book")
    print("Enter 3. To return a book")
    print("Enter 4. To exit")
    a=int(input("Select a choice from 1-4: "))
    
    if a==1:
        print("\nBOOKS AVAILABLE IN THE LIBRARY")
        print("---------------------------------")
        for book in books:
            if book["available"]==True:
                print(book["id"],book["name"],book["author"])
            else:
                print("Not in this list")
            
    elif a==2:
        book_id=eval(input("\nEnter ID of the book to be borrowed:"))
       # print(books[book_id-1])
        if book_id>10:
            print("\nINVALID BOOK ID")
        elif books[book_id-1]["available"]==True:
             books[book_id-1]["available"]=False
        else:
            print("\nBook is not available at the moment!\nPlease try another book")
            q=eval(input("Enter ID of the book to be borrowed: "))
            print(books[q-1])

    elif a==3:
        print("\n   BOOKS TO BE RETURNED   ")
        print("--------------------------")
        while True:
            n=int(input("No. of books to return: "))
            if n>3:
                print("Only 3 books can be returned at once.")
                f=int(input("No. of books to return: "))
            else:
                pass
            for i in(0,n,-1):
                book_id=int(input("Enter the ID of the book to be returned: "))
                for i in range(0,n,3):
                   books[book_id-1]["available"]==True
            else:
                print("Books have been returned")
                print("-----------------------------------------------")
                print("Enter 1. To display available books ")
                print("Enter 2. To borrow a book")
                print("Enter 3. To return a book")
                print("Enter 4. To exit")
                a=int(input("\nSelect a choice from 1-4: "))
                
    elif a==4:
       print("Thank you")
       break
