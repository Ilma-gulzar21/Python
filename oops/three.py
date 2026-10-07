
class book:
 def __init__(self,title,author):
     self.title=title
     self.author=author
     self.list=[]
     

 def addReview(self):
        while True:
              review=input("Enter a review = ")
              self.list.append(review)
              print("review added")
       
              des=input("are you want to send review again type yes or No")
              if des =="no":
                  break
       
        print("reviews send by  @",self.author)
        print(len(self.list))
        print("all reviews ",self.list)
       
obj=book("english","ilma")
obj.addReview()



