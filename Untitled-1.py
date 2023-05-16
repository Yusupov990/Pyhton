from tkinter import  *
win = Tk()
win.title("BIND")
win.geometry("300x500")
def DAV(event):
    l.config(bg="green")

def DAV1(event):
    l.config(bg="orange")

l = Button(win, text="UZB")
l.pack()
l.bind("<Return>",DAV)
l.bind("<G>",DAV1)
win.mainloop()

