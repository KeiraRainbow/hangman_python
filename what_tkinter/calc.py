from tkinter import *

root = Tk()

txt1 = Entry(width=20)
txt2 = Entry(width=20)
plus = Button(text="+")
minus = Button(text="-")
mul = Button(text="*")
div = Button(text="/")
ans = Label(width=20, fg='black')

def aa():
  a = txt1.get()
  return int(a)


def bb():
  b = txt2.get()
  return int(b)


def p(event):
     c = aa()+bb()
    c = str(c)
    ans['text'] = ' '.join(c)

def mi(event):
    c = aa() - bb()
    c = str(c)
    ans['text'] = ' '.join(c)

def mu(event):
    c = aa() * bb()
    c = str(c)
    ans['text'] = ' '.join(c)

def d(event):
    c = aa() / bb()
    c = str(c)
    ans['text'] = ' '.join(c)


plus.bind('<Button-1>', p)
minus.bind('<Button-1>', mi)
mul.bind('<Button-1>', mu)
div.bind('<Button-1>', d)

txt1.pack()
txt2.pack()
plus.pack()
minus.pack()
mul.pack()
div.pack()
ans.pack()

root.mainloop()
