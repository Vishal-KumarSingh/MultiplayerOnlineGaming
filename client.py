from tkinter import *
from websocket import create_connection
from threading import Thread
import json
def validation():
                global myframe,oppframe,waitmsg
                if 1 in myframe and 2 in myframe and 3 in myframe:
                    waitmsg.configure(text="You won the match")
                if 4 in myframe and 5 in myframe and 6 in myframe:
                    waitmsg.configure(text="You won the match")
                if 7 in myframe and 8 in myframe and 9 in myframe:
                    waitmsg.configure(text="You won the match")
                if 1 in myframe and 4 in myframe and 7 in myframe:
                    waitmsg.configure(text="You won the match")
                if 2 in myframe and 5 in myframe and 8 in myframe:
                    waitmsg.configure(text="You won the match")
                if 3 in myframe and 6 in myframe and 9 in myframe:
                    waitmsg.configure(text="You won the match")
                if 1 in myframe and 5 in myframe and 9 in myframe:
                    waitmsg.configure(text="You won the match")
                if 3 in myframe and 5 in myframe and 7 in myframe:
                    waitmsg.configure(text="You won the match")
                if 1 in oppframe and 2 in oppframe and 3 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 4 in oppframe and 5 in oppframe and 6 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 7 in oppframe and 8 in oppframe and 9 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 1 in oppframe and 4 in oppframe and 7 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 2 in oppframe and 5 in oppframe and 8 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 3 in oppframe and 6 in oppframe and 9 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 1 in oppframe and 5 in oppframe and 9 in oppframe:
                    waitmsg.configure(text="You loosed the match")
                if 3 in oppframe and 5 in oppframe and 7 in oppframe:
                    waitmsg.configure(text="You loosed the match")


class Receive(Thread):
    def run(self):
        global ws,frame,oppframe,move_status
        while True:
             opp_move = json.loads(ws.recv())
             if 'pos' in opp_move:
                 frame[opp_move["pos"]].configure(bg="blue")
                 oppframe.append(opp_move["pos"])
                 print(oppframe)
                 move_status=1
                 validation()
def reset():
    welcome.place_forget()
    yourconnid.place_forget()
    oppname.place_forget()
    namefied.place_forget()
    oppfied.place_forget()
    startgame.place_forget()

def clicked(events):
    global opp_conn_id,frame,move_status,myframe,oppframe
    if move_status==1:
        if not events in myframe:
            if not events in oppframe:
                msg = '{"action":"mymove","pos":'+str(events)+',"connectionId":"'+opp_conn_id+'"}'
                print(msg)
                ws.send(msg)
                frame[events].configure(bg="red")
                myframe.append(events)
                move_status=0
                print(myframe)
                validation()
def startplay(event):
    global opp_conn_id,frame,waitmsg
    reset()
    opp_conn_id = oppfied.get()
    waitmsg = Label(master=root,text="Click on tiles to choose.\n Red is yours \n Blue is opponent")
    waitmsg.grid(row=1 ,column=1)
    frame[1]=Frame(master=root, bg="white", height="100",width="150",bd="5")
    frame[1].grid(row=2,column=1)
    frame[1].bind("<Button-1>",lambda event, events=1: clicked(events))
    frame[2] = Frame(master=root, bg="#aaaaaa", height="100",width="150",bd="5")
    frame[2].grid(row=2, column=2)
    frame[2].bind("<Button-1>",lambda event, events=2: clicked(events))
    frame[3]=Frame(master=root, bg="white", height="100",width="150",bd="5")
    frame[3].grid(row=2,column=3)
    frame[3].bind("<Button-1>", lambda event, events=3: clicked(events))
    frame[4] = Frame(master=root, bg="#aaaaaa", height="100",width="150",bd="5")
    frame[4].grid(row=3, column=1)
    frame[4].bind("<Button-1>", lambda event, events=4: clicked(events))
    frame[5] = Frame(master=root, bg="white", height="100",width="150",bd="5")
    frame[5].grid(row=3, column=2)
    frame[5].bind("<Button-1>", lambda event, events=5: clicked(events))
    frame[6] = Frame(master=root, bg="#aaaaaa", height="100",width="150",bd="5")
    frame[6].grid(row=3, column=3)
    frame[6].bind("<Button-1>", lambda event, events=6: clicked(events))
    frame[7] = Frame(master=root, bg="white", height="100",width="150",bd="5")
    frame[7].grid(row=4, column=1)
    frame[7].bind("<Button-1>", lambda event, events=7: clicked(events))
    frame[8] = Frame(master=root, bg="#aaaaaa", height="100",width="150",bd="5")
    frame[8].grid(row=4, column=2)
    frame[8].bind("<Button-1>", lambda event, events=8: clicked(events))
    frame[9]=Frame(master=root, bg="white", height="100",width="150",bd="5")
    frame[9].grid(row=4,column=3)
    frame[9].bind("<Button-1>", lambda event, events=9: clicked(events))

frame = ["","","","","","","","","",""]
myframe=[]
oppframe=[]
opp_conn_id=""
waitmsg=""
move_status=1
url ="wss://2po4jec9s7.execute-api.ap-south-1.amazonaws.com/production"
ws = create_connection(url)
ws.send("hello world")
conn_id = ws.recv()
root = Tk()
root.title("TicTacToe")
root.iconbitmap('icon.ico')
root.geometry("450x450")
welcome = Label(master=root,text="Welcome to TIC TAC TOE")
yourconnid = Label(master=root,text="Your Dynamic Id")
oppname = Label( master=root, text="Enter your friend Dynamic Id")
namefied = Label(master=root,text=conn_id)
print(conn_id)
oppfied = Entry(master=root)
startgame = Button(master=root , text="Start Game")
startgame.bind("<Button-1>",startplay)
welcome.place(x=100,y=20,width=200,height=20)
yourconnid.place(x=50,y=100)
oppname.place(x=50,y=200)
namefied.place(x=250,y=100)
oppfied.place(x=250,y=200)
startgame.place(x=150,y=250,height=30,width=100)
receive = Receive()
receive.start()
root.mainloop()

ws.close()