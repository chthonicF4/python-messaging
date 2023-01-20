
import tkinter as tk




Colour_palet = ["efd9ce","dec0f1","b79ced","957fef","7161ef"]#["407076","698996","97b1a6","c9c5ba","000000"]#["434a42","aca885","e1ca96","918b76","626c66"]#["407076","698996","97b1a6","c9c5ba","000000"]#["2d3142","bfc0c0","ffffff","4f5d75","ef8354"]

colour_dic = {
    "background" : "#"+Colour_palet[0],
    "forground" : "#"+Colour_palet[1],
    "forground_alt" : "#"+Colour_palet[2],
    "accent" : "#"+Colour_palet[3],
    "text" : "#"+Colour_palet[4]
}

def send():
    message = send_box.get()
    send_box.delete(0,len(send_box.get()))
    chat_add(message)
    
    pass

def chat_add(msg:str):
    msg = "[NONE] : "+str(msg)+"\n"
    chat.config(state="normal")
    chat.insert(tk.END,msg)
    chat.config(state="disabled")
    chat.yview_scroll(1,what="units")


root = tk.Tk()
root.geometry("700x500")
root.config(bg=colour_dic.get("background"))

# --------- sending bar ---------------

# config
size = 20
send_box_font = ("comic sans",size)
send_button_font = ("comic sans",size - 5)

# frame
send_bar  = tk.Frame(
    master=root,
    width=root.winfo_width(),
    height=20,
    bg=colour_dic.get("forground"),
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

chat_box_font = ("arial",size-5)

# chat box frame
chat_box = tk.Frame(
    master=root,
    bg=colour_dic.get("forground"),
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
    repeatinterval=1,
    jump=False,
    bg="red",
    borderwidth=100
)

chat['yscrollcommand'] = chat_scroll_bar.set

chat_box.columnconfigure(0,weight=1,minsize=10)
chat_box.rowconfigure(0,weight=1,minsize=10)

chat.grid(column=0,row=0,sticky=tk.NSEW)
chat_scroll_bar.grid(column=1,row=0,sticky=tk.NS)

# pack both frames
chat_box.pack(fill=tk.BOTH,expand=True,padx=10,pady=10)
send_bar.pack(fill=tk.X,side=tk.BOTTOM)

for x in range(100):
    chat_add(x)

root.mainloop()
