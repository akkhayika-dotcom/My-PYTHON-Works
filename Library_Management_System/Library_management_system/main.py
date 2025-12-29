def adding_books():
    number_of_books=int(input("Enter the number of books you want to add:"))
    book_list=[]
    try:
         for books in range(number_of_books):
             b={}
             b["name"]=input(f"Enter the name of the book_{books+1}:")
             b["isbn"]=input(f"Enter the isbn of the book_{books+1}:")
             b["author"]=input(f"Enter the author of the book_{books+1}:")
             b["genre"]=input(f"Enter the genre of the book_{books+1}:")
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
    try:
        for book in book_details:
           if book.get("name")==name:
               print("Book found!! Enter the updated details.....")
               book["name"]=input("Enter the updated name:")
               book["isbn"]=input("Enter the updated isbn:")
               book["author"]=input("Enter the updated author:")
               book["genre"]=input("Enter the updated genre:")
               
               found=0
        if found==1:
            print("Book not found!! Please try again...")
        else:
            print("Book details have been updated.", book_details)
    except Exception as e:
        print(e)
    return book_details


def delete_books(book_details):
    name=input("Enter the name of the book you want to delete:")
    found=0
    try:
        for book in book_details: 
         if book.get("name")==name:
             print("Book found!! Deleting....")
             book_details.remove(book)
             
             found=0
        if found==1:
            print("Book not found!!!")
        else:
            print("Book deleted....",book_details)
    except Exception as e:
        print(e)
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