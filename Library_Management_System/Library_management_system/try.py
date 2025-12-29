def adding_books():
    number_of_books=int(input("Enter the number of books you want to add:"))
    book_list=[]
   
    for books in range(number_of_books):
           
        try:
            b={} 
            
            name=input(f"Enter the name of the book_{books+1}:")

            if not name.isalpha():
                print("\nIncorrect name!!\nName should only contain letters from A-Z or a-z...")
                adding_books()
            b["name"]=name

            isbn=input(f"Enter the isbn of the book_{books+1}:")
            if int(isbn) not in range(1000,10000):
                print("\nIncorrect ISBN!!\nPlease try again later")
                adding_books()
            b["isbn"]=isbn
        
            author=input(f"Enter the author of the book_{books+1}:")
            if not author.isalpha():
                print("\nAuthor name not found!!!\nAuthor name should only contain letters from A-Z or a-z...")
                adding_books()
            b["author"]=author
            genre=input(f"Enter the genre of the book_{books+1}:")
            if not genre.isalpha():
                print("\nGenre not found!!\nGenre should only contain letters from A-Z or a-z...")
                adding_books()
            b["genre"]=genre

            book_list.append(b)

        except Exception as e:
            print(e)
          
    return book_list

def view_books(book_details):
    try:
        for i in book_details:
            for j in i:
                print(f"{j}={i[j]}")
           
    except Exception as e:
        print(e)
    


def update_books(book_details):
    name=input("Enter the name of the book you want to update:")
    found=0
    
    for book in book_details:
        if book.get("name")==name:
            print("Book found!! Enter the updated details.....")
            found=1
            try:
                name=input("Enter the updated name:")
                if not name.isalpha():
                    print("\nIncorrect name!!\nName should only contain letters from A-Z or a-z...")
                    update_books(book_details)
                book["name"]=name

                isbn=int(input("Enter the updated isbn:"))
                if isbn not in range(1000,10000):
                    print("\nIncorrect ISBN!!\nPlease try again later")
                    update_books(book_details)
                book["isbn"]=isbn
                

                author=input("Enter the updated author:")
                if not author.isalpha():
                    print("\nAuthor name not found!!!\nAuthor name should only contain letters from A-Z or a-z...")
                    update_books(book_details)
                book["author"]=author


                genre=input("Enter the updated genre:")
                if not genre.isalpha():
                    print("\nGenre not found!!\nGenre should only contain letters from A-Z or a-z...")
                    update_books(book_details)
                book["genre"]=genre
            # found=1
            except Exception as e:
              print(e)
                
            # found=1
    if found==0:
        print("Book not found!! Please try again...")
    else:
        print("Book details have been updated.", book_details)
            
            
    return book_details


def delete_books(book_details):
    name=input("Enter the name of the book you want to delete:")
    found=0
    
    for book in book_details: 
         if book.get("name")==name:
             print("Book found!! Deleting....")
            #  book_details.remove(book)
             
             found=1
             try:
                 name=input("Enter the name of the book you want to delete:")
                 if not name.isalpha():
                     print("\nIncorrect name!!\nName should only contain letters from A-Z or a-z...")

             except Exception as e:
                 print(e)      
         book_details.remove(book)      
         
         if found==0:
            print("Book not found!!!")
         else:
            # book_details.remove(book)
            print("Book deleted....",book_details)
    
    return book_details


def main():
        print("********* WELCOME TO OUR LIBRARY *********")
        book_data=None
        while True:
            print("To add books press-----> 1")
            print("To view books press-----> 2")
            print("To update books press-----> 3")
            print("To delete books press-----> 4")
            print("To exit press-----> 5")
            choose=input("Enter your choice:")

            if choose=="5":
                print("EXITING.....")
                break
            elif choose=="1":
                print("Adding books.....")
                book_details=adding_books()
                book_data=book_details
                print(book_data)
            elif choose=="2":
                print("Viewing books.....")
                book_details=view_books(book_data)
                print("Books=",book_data)
            elif choose=="3":
                print("Updating book.....")
                book_details=update_books(book_data)
                print("Updated books=",book_data)
            elif choose=="4":
                print("Deleting books.....")
                book_details=delete_books(book_data)
                print(book_data)
            else:
                print("INCORRECT CHOICE!!!")



main()