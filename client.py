from lib.networking import *
import threading , time , tkinter as tk


sock = connection()
nickname = str(input("Display Name : "))
server_addr = str(input("Address of server :"))
server_addr = (server_addr[:server_addr.index(":")],int(server_addr[server_addr.index(":")+1:]))

#try connect to server


def connect_to_server(server_addr,count=0):
    count += 1
    if count > 5 :
        print(f"could'nt connect to {server_addr}.")
        quit()
    try:
        sock.connect(server_addr)
    except :
        print(f"Connection timed out , retrying....")
        time.sleep(1)
        connect_to_server(server_addr,count)
    print("connected to server")


connect_to_server(server_addr)

time.sleep(0.1)

sock.send(nickname,"nick")

def recive(conn:connection):
    try :
        while True:
            msg ,flag = conn.recv()
            if flag == "msg":
                print(msg)
                chat_add(msg)
    except : 
        pass
    return


def send(msg):
        if msg == "\leave" :
            sock.send("","leave")
            sock.close()
            quit()
        sock.send(msg,"msg")

# _________-------- WINDOW -----------_________#


Colour_palet = ["000000","14213d","707070","c2c2c2","fca311"]
font = "Verdana"

colour_dic = {
    "background" : "#"+Colour_palet[0],
    "forground" : "#"+Colour_palet[1],
    "forground_alt" : "#"+Colour_palet[2],
    "accent" : "#"+Colour_palet[3],
    "text" : "#"+Colour_palet[4]
}

def send(*args):
    msg = send_box.get()
    send_box.delete(0,len(send_box.get()))
    if msg == "\leave" :
        sock.send("","leave")
        sock.close()
        quit()
    sock.send(msg,"msg")
    
    pass

def chat_add(msg:str):
    msg += "\n"
    chat.config(state="normal")
    chat.insert(tk.END,msg)
    chat.config(state="disabled")
    chat.yview_scroll(1,what="units")


root = tk.Tk()
root.geometry("700x500")
root.title(f"{server_addr} {nickname}")

root.config(
    bg=colour_dic.get("background")
    )

# --------- sending bar ---------------

# config
size = 20
send_box_font = (font,size)
send_button_font = (font,size - 5)

# frame
send_bar  = tk.Frame(
    master=root,
    width=root.winfo_width(),
    height=20,
    bg=colour_dic.get("background"),
    border=0
    )



# text box
send_box = tk.Entry(
    master=send_bar,
    width=140,
    font=send_box_font,
    bg=colour_dic.get("forground_alt"),
    fg=colour_dic.get("text"),
    borderwidth=1,
    insertbackground=colour_dic.get("text")
    )

send_bar.columnconfigure(0,weight=1,minsize=100)
send_box.grid(column=0,row=0,padx=10)

send_box.bind('<Return>',send)

# send button
send_button = tk.Button(
    master=send_bar,
    text="Send",
    command=send, 
    # style
    font=send_button_font,
    fg=colour_dic.get("text"),
    bg=colour_dic.get("forground_alt"),
    borderwidth=1,
    activebackground=colour_dic.get("forground")
    )

send_button.grid(column=1,row=0,padx=10)


# ----------- chat box ---------------

# font

chat_box_font = (font,size-5)

# chat box frame
chat_box = tk.Frame(
    master=root,
    bg=colour_dic.get("background"),
    width=root.winfo_width(),
    height=200
    )

# chat box 
chat = tk.Text(
    master=chat_box,
    width=2,
    height=2,
    bg = colour_dic.get("forground"),
    state="disabled",
    font=chat_box_font,
    fg=colour_dic.get("text")
    )

#scroll bar
chat_scroll_bar = tk.Scrollbar(
    master=chat_box,
    orient='vertical', 
    command=chat.yview,
    repeatinterval=1
)

chat['yscrollcommand'] = chat_scroll_bar.set

chat_box.columnconfigure(0,weight=1,minsize=10)
chat_box.rowconfigure(0,weight=1,minsize=10)

chat.grid(column=0,row=0,sticky=tk.NSEW)
chat_scroll_bar.grid(column=1,row=0,sticky=tk.NS)

# pack both frames
chat_box.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)
send_bar.pack(fill=tk.X,side=tk.BOTTOM)

recive_thread = threading.Thread(target=recive,args=(sock,))
recive_thread.start()


root.mainloop()



