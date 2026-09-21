'''
OOP - Instagram
Basic structure
'''

class User:
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def login(self):
        print("\nThe user is loged in\n")

    def sign_up(self):
        print("\nThe user has signed up\n")

    def post(self,post):
        self.post = post
        # Aqui name contendra todo el objeto de post

    def message(self,message):
        self.message = message

    def create_post(self):
        print(f"\nThe user {self.name} created a post from the type: {self.post.type} and with the description: {self.post.description}\n")

    def show_message(self):
        print(f"\nThe user {self.name} received a comment from {self.message.user} on the date {self.message.date}\n")


class Post:
    def __init__(self,type,description,date):
        self.type = type
        self.description = description
        self.date = date

    def upload(self):
        print("\nThe post is up\n")

    def delete(self):
        print("\nThe post has been deleted\n")

    def comment(self,comment):
        self.comment = comment

    def show_comment(self):
        print(f"\nThe user {self.comment.user} made a post of the type {self.type} and the user {self.comment.receiver} commented on {self.comment.date}\n")



class Comment:
    def __init__(self,user,receiver,length,date):
        self.user = user
        self.receiver = receiver
        self.length = length
        self.date = date

    def upload(self):
        print("\nThe comment is up\n")

    def delete(self):
        print("\nThe comment has been deleted\n")

    def show(self):
        print(f"\nType of post: {self.post.type} description of the post: {self.post.desciption}\n")


class Message:
    def __init__(self,user,length,date):
        self.user = user
        self.length = length
        self.date = date

    def upload(self):
        print("\nThe message is up\n")

    def delete(self):
        print("\nThe message has been deleted\n")


# Relationship between a user and a post, to use the function create_post() in the class User.
# It prints "The user {self.name} created a post from the type: {self.post.type} and with the description: {self.post.description}"
user1 = User("Adrian","adrian@gmai.com","6181234567")
post1 = Post("photo","Last summer","11/09/2026")

user1.post(post1)
user1.create_post()

# Relationship between post and comment, to use the function show_comment() in the class Post.
# It prints "The user {self.comment.user} made a post of the type {self.type} and the user {self.comment.receiver} commented on {self.comment.date}"
post2 = Post("video","Everything has changed","14/02/2026")
comment1 = Comment("@dulce","@adrian","68","15-02-2026")

post2.comment(comment1)
post2.show_comment()

# Relationship between user and message,  to use the function show_message() in the Class User
# It prints "The user {self.name} received a comment from {self.message.user} on the date {self.message.date}"
user2 = User("Langdon","langdon@gmai.com","6181234567")
message1 = Message("@melking","40","04/07/2026")

user2.message(message1)
user2.show_message()
