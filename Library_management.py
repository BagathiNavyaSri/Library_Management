class Library():
    def ask_Info(self):
        print("<=||=> WELCOME TO OUR LIBRARY <=||=>")
        Books = {'id8459':'Deep Learning', 'id0521':'Java Programming'}
        while True:
            print(" 1. Add Book \n 2. Available Books \n 3. Borrow Book \n 4. Exit")
            choice = int(input("Enter your choice:"))
        
            if choice == 1:
                id = input("Enter the referral id of the book: ")
                title = input("Enter the title of the book: ")
                Books[id] = title
                print(f'Book with title \"{title}\" and referral id \"{id}\" has been successfully added!')
                print()
        
            elif choice == 2:
                print(f'No. of Books available in the library are : {len(Books)}. The books are: \n\n(Referral Id) -> (Title)')
                for id,title in Books.items():
                    print(id,"->",title)
                    
            elif choice == 3:
                borrow_bookid = input("Enter the referral id of the book you want to  borrow:")
                if borrow_bookid in Books.keys():
                    removed_book = Books.pop(borrow_bookid)
                    print(f'Here is your Book : \"{removed_book}\"')
                else:
                    print(f'Sorry..The Book with referral id "{borrow_bookid}" is not available.')
                print()
            elif choice == 4:
                break

            else:
                print("Invalid choice entered!!")              
lib = Library()  
lib.ask_Info()              


            