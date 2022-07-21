import tkinter
window = tkinter.Tk()
window.title("мой калькулятор")
window.geometry("300x300")

def add():
    num1 = text_num1.get()
    num1=int(num1)
    num2 = text_num2.get()
    num2=int(num2)
    result = num1+num2
    print(result)
    text_resultat.delete(0,"end")
    text_resultat.insert(0,result)


def sub():
    num1 = text_num1.get()
    num1=int(num1)
    num2 = text_num2.get()
    num2=int(num2)
    result = num1-num2
    print(result)
    text_resultat.delete(0,"end")
    text_resultat.insert(0,result)



button_add = tkinter.Button(window,text="+",command=add)
button_add.place(x=95,y=110)
button_sub = tkinter.Button(window,text="-",command=sub)
button_sub.place(x=160,y=110)
text_num1 = tkinter.Entry(window,width=20)
text_num1.place(x=95,y=40)
text_num2 = tkinter.Entry(window,width=20)
text_num2.place(x=95,y=81)
text_resultat = tkinter.Entry(window,width=20)
text_resultat.place(x=95,y=221)














window.mainloop()