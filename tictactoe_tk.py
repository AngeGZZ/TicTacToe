from tkinter import *

fenetre = Tk()
fenetre.title("TicTacToe")
fenetre.config(bg="#87CEEB")
# fenetre.geometry("280x300")
fenetre.geometry("850x750")
fenetre.resizable(width=False, height=False)
fenetre.iconbitmap("icone.ico")
check = True
count = 0
winner = False


def disable_button():
    b1.config(state='disabled')
    b2.config(state='disabled')
    b3.config(state='disabled')
    b4.config(state='disabled')
    b5.config(state='disabled')
    b6.config(state='disabled')
    b7.config(state='disabled')
    b8.config(state='disabled')
    b9.config(state='disabled')


def win():
    global winner
    # Check win pour X
    if (b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X"):
        b1.config(bg="green", text=" ")
        b2.config(bg="green", text=" ")
        b3.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(
            text="Le joueur jouant avec les X l'emporte")
    if (b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X"):
        b4.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b6.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")
    if (b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X"):
        b7.config(bg="green", text=" ")
        b8.config(bg="green", text=" ")
        b9.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")
    if (b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X"):
        b1.config(bg="green", text=" ")
        b4.config(bg="green", text=" ")
        b7.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")
    if (b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X"):
        b2.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b8.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")
    if (b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X"):
        b3.config(bg="green", text=" ")
        b6.config(bg="green", text=" ")
        b9.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")
    if (b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X"):
        b1.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b9.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")
    if (b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X"):
        b3.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b7.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les X l'emporte")

# Check win pour O
    if (b1["text"] == "O" and b2["text"] == "O" and b3['text'] == "O"):
        b1.config(bg="green", text=" ")
        b2.config(bg="green", text=" ")
        b3.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
       # winner_name.config(text = "Partie gagnée par" +)
    if (b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O"):
        b4.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b6.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
    if (b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O"):
        b7.config(bg="green", text=" ")
        b8.config(bg="green", text=" ")
        b9.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
    if (b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O"):
        b1.config(bg="green", text=" ")
        b4.config(bg="green", text=" ")
        b7.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
    if (b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O"):
        b2.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b8.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
    if (b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O"):
        b3.config(bg="green", text=" ")
        b6.config(bg="green", text=" ")
        b9.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
    if (b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O"):
        b1.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b9.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
    if(b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O"):
        b3.config(bg="green", text=" ")
        b5.config(bg="green", text=" ")
        b7.config(bg="green", text=" ")
        winner = True
        disable_button()
        win_button.config(text="Le joueur jouant avec les O l'emporte")
# Check si égalité
    if count == 9 and winner == False:
        disable_button()
        win_button.config(
            text="Egalité! Appuyez sur reset dans les options pour rejouer!")


def button_click(b):
    global check, count

    if b['text'] == ' ' and check == True:
        b['text'] = "X"
        check = False
        count += 1
        win()
    elif b['text'] == ' ' and check == False:
        b['text'] = "O"
        check = True
        count += 1
        win()


def reset():
    global winner, count, check
    b1.config(text=" ", state="normal", bg="SystemButtonFace")
    b2.config(text=" ", state="normal", bg="SystemButtonFace")
    b3.config(text=" ", state="normal", bg="SystemButtonFace")
    b4.config(text=" ", state="normal", bg="SystemButtonFace")
    b5.config(text=" ", state="normal", bg="SystemButtonFace")
    b6.config(text=" ", state="normal", bg="SystemButtonFace")
    b7.config(text=" ", state="normal", bg="SystemButtonFace")
    b8.config(text=" ", state="normal", bg="SystemButtonFace")
    b9.config(text=" ", state="normal", bg="SystemButtonFace")
    win_button.config(text="La partie est en cours")
    winner = False
    count = 0
    check = True


menu_option = Menu(fenetre)
fenetre.config(menu=menu_option)

options_menu = Menu(menu_option, tearoff=False)
menu_option.add_cascade(label="Options du jeu", menu=options_menu)
options_menu.add_command(label="Reset le jeu", command=reset)
options_menu.add_command(label="Quitter", command=fenetre.destroy)


win_button = Label(text="La partie est en cours", font=("Helvetica", 20))
b1 = Button(fenetre, text=" ", command=lambda: button_click(b1),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b2 = Button(fenetre, text=" ", command=lambda: button_click(b2),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b3 = Button(fenetre, text=" ", command=lambda: button_click(b3),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b4 = Button(fenetre, text=" ", command=lambda: button_click(b4),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b5 = Button(fenetre, text=" ", command=lambda: button_click(b5),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b6 = Button(fenetre, text=" ", command=lambda: button_click(b6),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b7 = Button(fenetre, text=" ", command=lambda: button_click(b7),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b8 = Button(fenetre, text=" ", command=lambda: button_click(b8),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b9 = Button(fenetre, text=" ", command=lambda: button_click(b9),
            height=6, width=12, bg="SystemButtonFace", font=("Helvetica", 20))
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)

b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)

b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)


win_button.place(x=3, y=650)

fenetre.mainloop()
