class lib:
    def __init__(self,name,author,status=True):
         self.name=name
         self.author=author
         self.status=status

    def checkout(self):
         if self.status==True :
             self.status=False
             print("thanks for taking the book " , self.name)
         else:
              print("bookm not available", self.name)
 
    def return_book(self):
         self.status=True
         print("thanks for returing the book ",self.name)

    def check(self):
         if self.status==True:
              print("available ")
         else :
              print("book not available")


book1=lib("Rich Dad Poor Dad"," Robert Kiyosaki")
book2=lib("Clean Code", "Robert C. Martin")  
book3=lib("The Pragmatic Programmer","Andrew Hunt")      


book1.check()
book2.check()
book3.check()

book1.checkout()
book2.checkout()
book3.checkout()

book1.check()
book2.check()
book3.check()

book1.return_book()
book2.return_book()
book3.return_book()


book1.check()
book2.check()
book3.check()