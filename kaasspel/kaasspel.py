import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter import *
from PIL import ImageTk, Image


window = tk.Tk()
window.resizable(0, 0)
window.config(bg='grey')
Realsubmit = True

input5 = tk.IntVar()
frame = tk.Frame(window)
frame.place(relx=0.0)


def check():
    global Realsubmit
    Realsubmit = False
    submit()


def beginscherm():
    global frame, button1, vragen, gekozenkaas1, gekozenkaas, button3, img, input5, plaatje1
    img = ImageTk.PhotoImage(Image.open("beginscherm.png"))
    window.geometry("500x465")
    try:
        gekozenkaas1.destroy()
        gekozenkaas.destroy()
        button3.destroy()
    except NameError:
        print('')
    datetekst = tk.Label(frame, text='Kaas-Calculator', font='Helvetica 30 bold')
    datetekst.grid(row=0, column=0, ipadx='15', ipady='5', padx='85', columnspan=2, pady=20)

    plaatje1 = tk.Label(frame, image=img, width=350, height=233)
    plaatje1.grid(row=1, column=0, columnspan=2)

    button1 = ttk.Button(frame, text='Start')
    button1.grid(row=2, column=0, ipadx='14', ipady='12', pady=40, columnspan=2)
    button1.configure(command=startgame)


def submit():
    global inputs, kaas, vragen, vraag, Radiobutton1, Radiobutton2, tekst1, tekst2, button2, gekozenkaas, gekozenkaas1, button3, frame, Realsubmit, plaatje1, img
    if Realsubmit:
        inputs[vragen - 1]=(input5.get())
        vragen += 1

    if input5.get() == 1:
        img = ImageTk.PhotoImage(Image.open(f"vraag1-1.png"))
    else:
        img = ImageTk.PhotoImage(Image.open(f"vraag1-2.png"))

    if inputs[0] == 0:
        vraag.config(text='Zitten er gaten in?')
        if input5.get() == 1:
            img = ImageTk.PhotoImage(Image.open(f"vraag2-2.png"))
        else:
            img = ImageTk.PhotoImage(Image.open(f"vraag2-1.png"))

        if inputs[1] == 0:
            vraag.config(text='Is de kaas belachelijk duur?')

            if input5.get() == 1:
                img = ImageTk.PhotoImage(Image.open(f"vraag3-2.png"))
            else:
                img = ImageTk.PhotoImage(Image.open(f"vraag3-1.png"))

            if inputs[2] == 0:
                kaas = 'Emmenthaler'
            elif inputs[2] == 1:
                kaas = 'Leerdammer'

        elif inputs[1] == 1:
            vraag.config(text='Is de kaas zo hard als steen?')
            if input5.get() == 1:
                img = ImageTk.PhotoImage(Image.open(f"vraag3-2-2.png"))
            else:
                img = ImageTk.PhotoImage(Image.open(f"vraag3-2-1.png"))

            if inputs[2] == 0:
                kaas = 'Pammigiano-Reggiano'
            elif inputs[2] == 1:
                kaas = 'Goudse-kaas'

    elif inputs[0] == 1:
        vraag.config(text='Heeft de kaas blauwe schimmels?')
        if input5.get() == 1:
            img = ImageTk.PhotoImage(Image.open(f"vraag2-2-2.png"))
        else:
            img = ImageTk.PhotoImage(Image.open(f"vraag2-2-1.png"))

        if inputs[1] == 0:
            vraag.config(text='Heeft de kaas een korst?')

            if input5.get() == 1:
                img = ImageTk.PhotoImage(Image.open(f"vraag4-2.png"))
            else:
                img = ImageTk.PhotoImage(Image.open(f"vraag4-1.png"))

            if inputs[2] == 0:
                kaas = 'Blue-de-Roche'
            elif inputs[2] == 1:
                kaas = 'Foumme-d-Ambert'

        elif inputs[1] == 1:
            vraag.config(text='Heeft de kaas een korst?')

            if input5.get() == 1:
                img = ImageTk.PhotoImage(Image.open(f"vraag4-2.png"))
            else:
                img = ImageTk.PhotoImage(Image.open(f"vraag4-1.png"))

            if inputs[2] == 0:
                kaas = 'Cambert'
            elif inputs[2] == 1:
                kaas = 'Mozzarella'

    Realsubmit = True
    plaatje1.config(image=img)

    if vragen == 4:
        img = ImageTk.PhotoImage(Image.open(f"{kaas}.png"))
        plaatje1.config(image=img)
        vraag.destroy()
        Radiobutton1.destroy()
        Radiobutton2.destroy()
        tekst1.destroy()
        tekst2.destroy()
        button2.destroy()

        window.geometry("500x480")
        gekozenkaas = tk.Label(frame, text=f'De: {kaas}.', font='Helvetica 20 bold')
        gekozenkaas.grid(row=2, column=0, columnspan=2, pady=2)
        gekozenkaas1 = tk.Label(frame, text=f'Heb jij in gedachten!', font='Helvetica 15 bold')
        gekozenkaas1.grid(row=3, column=0, columnspan=2)
        button3 = ttk.Button(frame, text='Opnieuw spelen')
        button3.grid(row=4, column=0, ipadx='14', ipady='12', pady=12, columnspan=2)
        button3.configure(command=beginscherm)


def startgame():
    global button1, vragen, vraag, value, kaas, inputs, Radiobutton1, Radiobutton2, tekst1, tekst2, button2, gekozenkaas, gekozenkaas1, button3

    window.geometry("500x600")
    button1.destroy()

    vraag = tk.Label(frame, text='Is de kaas geel?', font='Helvetica 20 bold')
    vraag.grid(row=2, column=0, columnspan=2, pady=20)

    vragen = 1
    kaas = ""
    inputs = [2, 2, 2]
    input5.set(0)
    check()

    Radiobutton1 = tk.Radiobutton(frame, variable=input5, value=0, command=check)
    Radiobutton1.grid(row=3, column=0, sticky=E, padx=50)
    Radiobutton2 = tk.Radiobutton(frame, variable=input5, value=1, command=check)
    Radiobutton2.grid(row=3, column=1, sticky=W, padx=50)

    tekst1 = tk.Label(frame, text='Ja', font='Helvetica 15')
    tekst1.grid(row=4, column=0, sticky=E, padx=50)
    tekst2 = tk.Label(frame, text='Nee', font='Helvetica 15')
    tekst2.grid(row=4, column=1, sticky=W, padx=50)

    button2 = ttk.Button(frame, text='Submit')
    button2.grid(row=5, column=0, ipadx='14', ipady='12', pady=40, columnspan=2)
    button2.configure(command=submit)


beginscherm()
window.mainloop()
