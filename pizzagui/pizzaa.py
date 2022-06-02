import tkinter as tk
from tkinter import ttk, font
from tkinter.messagebox import showinfo
from tkinter.ttk import Combobox
from tkinter import *
from PIL import ImageTk, Image


window = tk.Tk()
window.resizable(0, 0)
window.config(bg='grey')
img = ImageTk.PhotoImage(Image.open("Pizza.png"))
img1 = ImageTk.PhotoImage(Image.open("small.png"))
img2 = ImageTk.PhotoImage(Image.open("med.png"))
img3 = ImageTk.PhotoImage(Image.open("groot.png"))
img4 = ImageTk.PhotoImage(Image.open("paypal.png"))

myFont = font.Font(family='Helvetica')
frame = tk.Frame(window)
frame.place(relx=0.0)
prevvalue = 1


def beginscherm():
    global datetekst, plaatje1, button1, frame

    window.geometry("502x500")
    window.title('Bestellen')
    frame.destroy()
    frame = tk.Frame(window)
    frame.place(relx=0.0)

    datetekst = tk.Label(frame, text='Pizza-Calculator', font='Helvetica 48 bold')
    datetekst.grid(row=0, column=0, columnspan=2, pady=20)

    plaatje1 = tk.Label(frame, image=img, width=250, height=250)
    plaatje1.grid(row=1, column=0, columnspan=2)

    button1 = tk.Button(frame, text='Bestel', font='Helvetica 13 bold', bg='green', command=bestellen)
    button1.grid(row=2, column=0, pady=40, columnspan=2, ipadx=40, ipady=12)


def check():
    global prijsklein, kleine_pizza, prijsmed, prijsgroot, totaal
    prijsklein.set('€{:.2f}'.format(kleine_pizza.get() * 4.29))
    prijsmed.set('€{:.2f}'.format(med_pizza.get() * 6.49))
    prijsgroot.set('€{:.2f}'.format(grote_pizza.get() * 7.99))
    totaal.set('€{:.2f} Afrekenen'.format(kleine_pizza.get() * 4.29 + med_pizza.get() * 6.49 + grote_pizza.get() * 7.99))


def bon():
    global frame
    window.geometry("355x310")
    window.title('Bonnetje')
    frame.destroy()
    frame = tk.Frame(window)
    frame.place(relx=0.02, rely=0.0)
    frame.config(bg='grey')
    Radiobutton3.destroy()
    Radiobutton4.destroy()
    label11 = tk.Label(frame, text=f' Bon', font='Arial 35 bold', justify='center', fg='green', bg='grey')
    label11.grid(row=0, column=0, pady=25)

    label12 = tk.Label(frame, text=f'Kleine pizza: {kleine_pizza.get()}  x  4,29 =  {prijsklein.get()}', font='Arial 14 bold', fg='black', bg='grey')
    label12.grid(row=1, column=0)
    label13 = tk.Label(frame, text=f'Medium pizza: {med_pizza.get()}  x  4,29 =  {prijsmed.get()}', font='Arial 14 bold', fg='black', bg='grey')
    label13.grid(row=2, column=0)
    label14 = tk.Label(frame, text=f'Grote pizza: {grote_pizza.get()}  x  4,29 =  {prijsgroot.get()}', font='Arial 14 bold', fg='black', bg='grey')
    label14.grid(row=3, column=0)
    label15 = tk.Label(frame, text='                                                          ----------+', font='Arial 12 bold', fg='black', bg='grey')
    label15.grid(row=4, column=0)
    label16 = tk.Label(frame, text=('Totaal: {:>28.2f} €'.format(kleine_pizza.get() * 4.29 + med_pizza.get() * 6.49 + grote_pizza.get() * 7.99)), font='Arial 15 bold', fg='black', bg='grey')
    label16.grid(row=5, column=0, pady=9)
    button17 = tk.Button(frame, text='Opnieuw bestellen', font='Helvetica 13 bold', bg='white', command=beginscherm, justify='center')
    button17.grid(row=6, column=0, ipadx=90, ipady=2)


def betalen2():
    valide = True
    getallen = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if len(input1.get()) > 40 or len(input1.get()) < 2:
        valide = False
    if 15 > len(input3.get()) > 9:
        for letter in input3.get():
            if letter not in getallen:
                valide = False
    else:
        valide = False

    if not len(input2.get()) > 2:
        valide = False

    if input5.get() == 0:
        if '@' not in input4.get() or len(input4.get()) < 2:
            valide = False
    if valide:
        bon()
    else:
        tk.messagebox.showinfo(title='Whoopsss..', message='Deze gegevens zijn niet valide!')


def betaalmanier():
    global input5, frame, img4, plaatje5, entry4, prevvalue, input4

    if input5.get() == 0 and prevvalue != 0:
        plaatje5 = tk.Label(frame, image=img4, width=30, height=16)
        plaatje5.grid(row=3, column=0)

        input4 = tk.StringVar()
        entry4 = tk.Entry(frame, textvariable=input4, font='Arial 12 bold', justify='center', width=25)
        entry4.grid(row=3, column=1, sticky=tk.W, padx=5, pady=1)
        window.geometry("500x200")
        window.title('Online')
    elif input5.get() == 1:
        plaatje5.destroy()
        entry4.destroy()
        window.geometry("500x175")
        window.title('Contant')
    prevvalue = input5.get()


def betalen():
    global frame, input5, input1, input2, input3, Radiobutton3, Radiobutton4
    window.geometry("500x175")
    window.title('Contant')
    frame.destroy()
    frame = tk.Frame(window)
    frame.place(relx=0.19, rely=0.2)
    frame.config(bg='grey')

    input5 = tk.IntVar(value=1)
    Radiobutton3 = tk.Radiobutton(window, variable=input5, value=0, command=betaalmanier, text='Online ')
    Radiobutton3.grid(row=0, column=0, sticky=E, ipadx=90)
    Radiobutton4 = tk.Radiobutton(window, variable=input5, value=1, command=betaalmanier, text='Contant ')
    Radiobutton4.grid(row=0, column=1, sticky=W, ipadx=90)

    label1 = tk.Label(frame, text='Naam: ', font='Arial 12 bold', justify='center', fg='black', bg='grey')
    label1.grid(row=0, column=0, sticky=tk.E, padx=5)

    input1 = tk.StringVar()
    entry1 = tk.Entry(frame, textvariable=input1, font='Arial 12 bold', justify='center', width=25)
    entry1.grid(row=0, column=1, sticky=tk.W, padx=5)

    label2 = tk.Label(frame, text='Adress: ', font='Arial 12 bold', justify='center', fg='black', bg='grey')
    label2.grid(row=2, column=0, sticky=tk.E, padx=5)

    input2 = tk.StringVar()
    entry2 = tk.Entry(frame, textvariable=input2, font='Arial 12 bold', justify='center', width=25)
    entry2.grid(row=2, column=1, sticky=tk.W, padx=5)

    label3 = tk.Label(frame, text='Nummer: ', font='Arial 12 bold', justify='center', fg='black', bg='grey')
    label3.grid(row=1, column=0, sticky=tk.E, padx=5)

    input3 = tk.StringVar()
    entry3 = tk.Entry(frame, textvariable=input3, font='Arial 12 bold', justify='center', width=25)
    entry3.grid(row=1, column=1, sticky=tk.W, padx=5)

    button5 = tk.Button(frame, text='Betaal', font='Helvetica 13 bold', bg='green', command=betalen2, justify='center')
    button5.grid(row=4, column=0, pady=15, ipadx=25, ipady=2)

    label10 = tk.Label(frame, textvariable=totaal, font='Arial 12 bold', justify='center', fg='black', bg='grey')
    label10.grid(row=4, column=1, sticky=tk.E, padx=5)


def bestellen():
    global prijsklein, kleine_pizza, med_pizza, grote_pizza, prijsmed, prijsgroot, totaal, frame
    window.geometry("762x492")
    window.title('Hoeveel Pizza')
    button1.destroy(), plaatje1.destroy(), datetekst.destroy()

    plaatje2 = tk.Label(frame, image=img1, width=250, height=250)
    plaatje2.grid(row=0, column=0)
    plaatje3 = tk.Label(frame, image=img2, width=250, height=250)
    plaatje3.grid(row=0, column=1)
    plaatje4 = tk.Label(frame, image=img3, width=250, height=250)
    plaatje4.grid(row=0, column=2)

    tekst1 = tk.Label(frame, text='Small | 4,29', font='Helvetica 12 bold')
    tekst1.grid(row=1, column=0, pady=20)
    tekst2 = tk.Label(frame, text='Med | 6,49', font='Helvetica 12 bold')
    tekst2.grid(row=1, column=1, pady=20)
    tekst3 = tk.Label(frame, text='Groot | 7,99', font='Helvetica 12 bold')
    tekst3.grid(row=1, column=2, pady=20)

    kleine_pizza = tk.IntVar()
    spinbox2 = tk.Spinbox(frame, from_=0, to=100, width=3, font='Arial 12 bold', justify='center', textvariable=kleine_pizza, wrap=True, command=check)
    spinbox2.grid(row=2, column=0, ipady=3)

    med_pizza = tk.IntVar()
    spinbox3 = tk.Spinbox(frame, from_=0, to=100, width=3, font='Arial 12 bold', justify='center', textvariable=med_pizza, wrap=True, command=check)
    spinbox3.grid(row=2, column=1, ipady=3)

    grote_pizza = tk.IntVar()
    spinbox4 = tk.Spinbox(frame, from_=0, to=100, width=3, font='Arial 12 bold', justify='center', textvariable=grote_pizza, wrap=True, command=check)
    spinbox4.grid(row=2, column=2, ipady=3)

    spinbox2['state'], spinbox3['state'], spinbox4['state'] = 'readonly', 'readonly', 'readonly'

    prijsklein = tk.StringVar()
    prijs1 = tk.Label(frame, textvariable=prijsklein, font='Helvetica 12 bold')
    prijs1.grid(row=3, column=0, pady=20)

    prijsmed = tk.StringVar()
    prijs2 = tk.Label(frame, textvariable=prijsmed, font='Helvetica 12 bold')
    prijs2.grid(row=3, column=1, pady=20)

    prijsgroot = tk.StringVar()
    prijs3 = tk.Label(frame, textvariable=prijsgroot, font='Helvetica 12 bold')
    prijs3.grid(row=3, column=2, pady=20)

    totaal = tk.IntVar()
    prijstotaal = tk.Button(frame, textvariable=totaal, font='Helvetica 13 bold', bg='green', justify=CENTER, command=betalen)
    prijstotaal.grid(row=4, column=1, pady=20, ipady=5, ipadx=20)
    prijsklein.set('€0.00'), prijsmed.set('€0.00'), prijsgroot.set('€0.00'), totaal.set('€0.00 Afrekenen')


beginscherm()
window.mainloop()
