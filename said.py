from tkinter import *
root = Tk()
entryNumberX = Entry(root, show=None, font=('Arial', 25))
entryNumberX.place(relx=0.25, rely=0.2, relwidth=0.2, relheight=0.1)


entryNumberY = Entry(root, show=None, font=('Arial', 25))
entryNumberY.place(relx=0.55, rely=0.2, relwidth=0.2, relheight=0.1)

entryEqual = Entry(root, show=None, font=('Arial', 25))
entryEqual.place(relx=0.35, rely=0.4, relwidth=0.3, relheight=0.1)

buttonAddition = Button(root, text="Addition")
buttonAddition.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.1)


root.title("  X+Y=Z  ")
root.geometry('600x500')
root.mainloop()
