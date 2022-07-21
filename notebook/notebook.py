import tkinter.filedialog as tfd
import tkinter as tk
window = tk.Tk()
window.title("Notebook by Savelii")
window.geometry("400x400")
fileName = ""
def openFile():
    contentText.delete(1.0,"end")
    global fileName
    fileName = tfd.askopenfilename()
    with open(fileName) as file:
        contentText.insert(1.0,file.read())

def saveAsFile():
    global fileName
    fileName = tfd.asksaveasfilename()
    content = contentText.get(1.0,"end")
    with open(fileName,"w") as file:
        file.write(content)

def newFile():
    contentText.delete(1.0,"end")
    global fileName

def saveFile():
    global fileName
    if fileName == "":
        saveAsFile()
    else:
        content = contentText.get(1.0,"end")
        with open(fileName,"w") as file:
            file.write(content)
openFileIcon = tk.PhotoImage(file="open_file.gif")
newFileIcon = tk.PhotoImage(file="new_file.gif")
safeFileIcon = tk.PhotoImage(file="save_file.gif")
contentText = tk.Text(window,wrap="word")
contentText.place(x=0,y=0,relwidth=1,relheight=1)
mainMenu = tk.Menu(window)
window.configure(menu=mainMenu)
fileMenu = tk.Menu(mainMenu,tearoff=0)
mainMenu.add_cascade(label="Файл",menu=fileMenu)
fileMenu.add_command(label="Новый файл",image=newFileIcon,compound="left",command=newFile)
fileMenu.add_command(label="Открыть",image=openFileIcon,compound="left",command=openFile)
fileMenu.add_command(label="Сохранить",image=safeFileIcon,compound="left",command=saveFile)
fileMenu.add_command(label="Сохранить как",image=safeFileIcon,compound="left",command=saveAsFile)











window.mainloop()