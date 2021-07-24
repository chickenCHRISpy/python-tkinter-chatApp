import socket
import threading
from tkinter import *

PORT=3000
SERVER= "192.168.56.1"
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

class chatbox:

    def __init__(self):
        #chat hidden window(temporary)
        self.Window = Tk()
        self.Window.withdraw()

        #login window with user name
        self.login = Toplevel()

        #title for login window
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        #create label
        self.label = Label(self.login,
       text="LOGIN to continue...",
       justify=CENTER,
       font="Arial 14 bold" )
        self.label.place(relx=0.1, rely=0.2)
        

        self.labelName = Label(self.login,text="Name: ",font="Helvetica 12")
        self.labelName.place(relheight=0.2,relx=0.1,rely=0.2)

        #entry box
        self.entryName = Entry(self.login, font="Helvetica 14")
        self.entryName.place(relwidth=0.4,relheight=0.12,relx=0.35,rely=0.2)

        #focus cursor
        self.entryName.focus()

        #continue button 
        self.go = Button(self.login,text="CONTINUE",font="Arial 14 bold",command=lambda: self.toChatWindow(self.entryName.get()))

        self.go.place(relx=0.4,rely=0.55)
        self.Window.mainloop()

    def toChatWindow(self, name):
        self.login.destroy()
        self.layout(name)

        #thread creation for recieving of msgs
        rcv = threading.Thread(target=self.receive)
        rcv.start()

    #main layout of the chat
    def layout(self, name):

        self.name = name
        #to show chat window
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width=False,height=False)
        self.Window.configure(width=478,height=558,bg="#207398")
        self.labelHead = Label(self.Window,bg="#207398",fg="#EAECEE",text=self.name,font="Times 24 bold italic", pady=5)

        self.labelHead.place(relwidth=1)
        self.line = Label(self.Window,width=458,bg="#22CB5C")

        self.line.place(relwidth=1,rely=0.07,relheight=0.012)

        self.txtCons = Text(self.Window,width=28,height=2,bg="#17202A",fg="#EAECEE",font="Helvetica 14",padx=5,pady=5)

        self.txtCons.place(relheight=0.745,relwidth=1,rely=0.08)

        self.labelBottom = Label(self.Window,bg="#95aec7",height=80)

        self.labelBottom.place(relwidth=1,rely=0.825)

        self.entryMsg = Entry(self.labelBottom,bg="#03203C",fg="#EAECEE",font="Helvetica 13")

        #place the given widget in chat window
        self.entryMsg.place(relwidth=0.74,relheight=0.06,rely=0.008,relx=0.011)

        self.entryMsg.focus()

        #create a Send Button
        self.buttonMsg = Button(self.labelBottom,text="SEND",font="Arial 10 bold",width=20,bg="#E5D68A",command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,rely=0.008,relheight=0.06,relwidth=0.22)

        self.txtCons.config(cursor="arrow")

        #scrollbar
        scrollbar = Scrollbar(self.txtCons)

        #placing into gui window
        scrollbar.place(relheight=1,relx=0.974)

        scrollbar.config(command=self.txtCons.yview)

        self.txtCons.config(state=DISABLED)

        #function for basic thread starting
    def sendButton(self, msg):
        self.txtCons.config(state=DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()
        
        #recieveing msg
    def receive(self):
        while True:
            try:
                message = client.recv(1024).decode(FORMAT)

                #send client name from server
                if message == 'NAME':
                    client.send(self.name.encode(FORMAT))
                else:
                    self.txtCons.config(state=NORMAL)
                    self.txtCons.insert(END,message + "\n\n")
                    self.txtCons.config(state=DISABLED)
                    self.txtcons.see(END)
            except:
                #print error in log
                print("An error occured!")
                client.close()
                break

        #function to send msg
    def sendMessage(self):
        self.txtCons.config(state=DISABLED)
        while True:
            message = (f"{self.name}: {self.msg}")
            client.send(message.encode(FORMAT))
            break

msg = chatbox()



                    
    


        
         