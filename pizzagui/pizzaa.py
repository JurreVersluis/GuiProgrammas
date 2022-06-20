import tkinter as tk
from tkinter import font
from tkinter.messagebox import showinfo
from tkinter import *
from PIL import ImageTk, Image
import re

window = tk.Tk()
window.resizable(0, 0)
window.config(bg='grey')

myFont = font.Font(family='Helvetica')
frame = tk.Frame(window)
frame.place(relx=0.0)
prevvalue = 1

img = [ImageTk.PhotoImage(Image.open("Pizza.png")), ImageTk.PhotoImage(Image.open("small.png")), ImageTk.PhotoImage(Image.open("med.png")), ImageTk.PhotoImage(Image.open("groot.png")), ImageTk.PhotoImage(Image.open("paypal.png"))]
teksten = ['Small | 4.29', 'Med | 6.49', 'Groot | 7.99', 'Online ', 'Contant ', 'Naam: ', 'Nummer: ', 'Adress: ']


def beginscherm():
    global label, plaatje, button, frame

    window.geometry("502x500")
    window.title('Bestellen')
    frame.destroy()
    frame = tk.Frame(window)
    frame.place(relx=0.0)

    label = tk.Label(frame, text='Pizza-Calculator', font='Helvetica 48 bold')
    label.grid(row=0, column=0, columnspan=2, pady=20)

    plaatje = tk.Label(frame, image=img[0], width=250, height=250)
    plaatje.grid(row=1, column=0, columnspan=2)

    button = tk.Button(frame, text='Bestel', font='Helvetica 13 bold', bg='green', command=bestellen)
    button.grid(row=2, column=0, pady=40, columnspan=2, ipadx=40, ipady=12)


def bon():
    global frame, pizzahoeveelheden, Radiobutton1, prijzenLijst, totaal
    window.geometry("355x310")
    window.title('Bonnetje')
    for item in window.winfo_children():
        item.destroy()
    frame = tk.Frame(window)
    frame.place(relx=0.02, rely=0.0)
    frame.config(bg='grey')

    label2 = tk.Label(frame, text=f' Bon', font='Arial 35 bold', justify='center', fg='green', bg='grey')
    label2.grid(row=0, column=0, pady=25)

    for i in range(3):
        label3 = tk.Label(frame, text=f'Kleine pizza: {pizzahoeveelheden[i].get()}  x  {teksten[i][-4:]} =  €{pizzahoeveelheden[i].get() * float(teksten[i][-4:])}', font='Arial 14 bold', fg='black', bg='grey')
        label3.grid(row=i + 1, column=0)

    label4 = tk.Label(frame, text=('€{:.2f}'.format(pizzahoeveelheden[0].get() * 4.29 + pizzahoeveelheden[1].get() * 6.49 + pizzahoeveelheden[2].get() * 7.99)), font='Arial 15 bold', fg='black', bg='grey')
    label4.grid(row=5, column=0, pady=15)
    button1 = tk.Button(frame, text='Opnieuw bestellen', font='Helvetica 13 bold', bg='white', command=beginscherm, justify='center')
    button1.grid(row=6, column=0, ipadx=90, ipady=2)


def afrekenen():
    global formulier, valide
    valide = True
    for item in formulier:
        if not 5 < len(item.get()) < 25:
            valide = False
    if not formulier[1].get().isnumeric():
        valide = False
    try:
        if not re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', formulier[3].get()):
            valide = False
    except:
        print('test')

    if valide:
        bon()
    else:
        tk.messagebox.showinfo(title='Whoopsss..', message='Deze gegevens zijn niet valide!')


def betaalmanier():
    global input3, frame, prevvalue, plaatje, entry, input2, formulier

    if input3.get() == 0 and prevvalue != 0:
        plaatje = tk.Label(frame, image=img[4], width=30, height=16)
        plaatje.grid(row=3, column=0)

        input2 = tk.StringVar()
        entry = tk.Entry(frame, textvariable=input2, font='Arial 12 bold', justify='center', width=25)
        entry.grid(row=3, column=1, sticky=tk.W, padx=5, pady=1)
        formulier.append(input2)
        window.geometry("500x200")
        window.title('Online')

    elif input3.get() == 1:
        try:
            plaatje.destroy(), entry.destroy()
            formulier.pop()
            window.geometry("500x175")
            window.title('Contant')
        except:
            print(formulier)
    prevvalue = input3.get()


def betalen():
    global frame, Radiobutton1, label1, totaal, input3, formulier

    window.geometry("500x175")
    window.title('Contant')
    frame.destroy()
    frame, input3, formulier = tk.Frame(window), tk.IntVar(value=1), []
    frame.place(relx=0.19, rely=0.2)
    frame.config(bg='grey')

    for i in range(2):
        Radiobutton1 = tk.Radiobutton(window, variable=input3, value=i, command=betaalmanier, text=teksten[i + 3])
        Radiobutton1.grid(row=0, column=i, sticky=E, ipadx=90)

    for i in range(3):
        label1 = tk.Label(frame, text=teksten[i + 5], font='Arial 12 bold', justify='center', fg='black', bg='grey')
        label1.grid(row=i, column=0, sticky=tk.E, padx=5)

        input1 = tk.StringVar()
        entry1 = tk.Entry(frame, textvariable=input1, font='Arial 12 bold', justify='center', width=25)
        entry1.grid(row=i, column=1, sticky=tk.W, padx=5)
        formulier.append(input1)

    button1 = tk.Button(frame, text='Betaal', font='Helvetica 13 bold', bg='green', command=afrekenen, justify='center')
    button1.grid(row=4, column=0, pady=15, ipadx=25, ipady=2)

    label2 = tk.Label(frame, textvariable=totaal, font='Arial 12 bold', justify='center', fg='black', bg='grey')
    label2.grid(row=4, column=1, sticky=tk.E, padx=5)


def check():
    global totaal
    for i in range(3):
        prijzenLijst[i].set('€{:.2f}'.format(pizzahoeveelheden[i].get() * float(teksten[i][-4:])))
    totaal.set('€{:.2f} Afrekenen'.format(pizzahoeveelheden[0].get() * 4.29 + pizzahoeveelheden[1].get() * 6.49 + pizzahoeveelheden[2].get() * 7.99))


def bestellen():
    global prijzenLijst, pizzahoeveelheden, totaal, frame
    window.geometry("762x492")
    window.title('Hoeveel Pizza')
    pizzahoeveelheden, prijzenLijst = [], []
    button.destroy(), plaatje.destroy(), label.destroy()

    for i in range(3):
        Pizza, Prijs, totaal = tk.IntVar(), tk.IntVar(), tk.IntVar()
        plaatje1 = tk.Label(frame, image=img[i + 1], width=250, height=250)
        plaatje1.grid(row=0, column=i)

        tekst = tk.Label(frame, text=teksten[i], font='Helvetica 12 bold')
        tekst.grid(row=1, column=i, pady=20)

        spinbox = tk.Spinbox(frame, from_=0, to=100, width=3, font='Arial 12 bold', justify='center', textvariable=Pizza, wrap=True, command=check, state='readonly')
        spinbox.grid(row=2, column=i, ipady=3)

        prijs = tk.Label(frame, textvariable=Prijs, font='Helvetica 12 bold')
        prijs.grid(row=3, column=i, pady=20)
        Prijs.set('€0.00')
        pizzahoeveelheden.append(Pizza)
        prijzenLijst.append(Prijs)

    prijstotaal = tk.Button(frame, textvariable=totaal, font='Helvetica 13 bold', bg='green', justify=CENTER, command=betalen)
    prijstotaal.grid(row=4, column=1, pady=20, ipady=5, ipadx=20)
    totaal.set('€0.00 Afrekenen')


beginscherm()
window.mainloop()
