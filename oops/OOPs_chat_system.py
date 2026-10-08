class chat_system:

    def __init__(self, name, user_choice):
        self.name = name
        self.user_choice = user_choice
        self.data = {}

    def join_chatRoom(self):
        if self.user_choice == "no":
            print(self.name, "left the chat room")
        else:
            print(self.name, "joined the chatroom")

    def send_msg(self, msg):
        if self.name in self.data:
            self.data[self.name].append(msg)
        else:
            self.data[self.name] = [msg]

        print(self.name, ":", msg)

    def chat_history(self):
        print("___CHAT HISTORY___")
        print(self.data)


choice = input("Do you want to join the chat type yes or no = ")

if choice == "yes":
    name = input("Enter your name = ")

    user = chat_system(name, choice)
    user.join_chatRoom()

    msg = input("Enter message = ")
    user.send_msg(msg)

    user.chat_history()

else:
    print("You did not join the chat room")
