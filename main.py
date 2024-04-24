from tkinter import *
from tkinter import messagebox
import ast
import pygame

pygame.mixer.init()
sound = pygame.mixer.Sound("sounds/click_sound.mp3")

with open("files/signed_user.txt", "r") as file:
    s = file.read()
    d = ast.literal_eval(s)

def where_window(w, h):
    screen_width = screen.winfo_screenwidth()
    screen_height = screen.winfo_screenheight()
    x = int(screen_width/2 - w/2)
    y = int((screen_height/2 - h/2) - 100)
    return x, y


def signnnnn(type, username_signin, user_password_signin):
    width2 = 300
    height2 = 200
    screen.title("Click game")

    if type == "second":
        frame_signin.destroy()
        frame_signup.destroy()

    x2, y2 = where_window(width2, height2)

    screen.geometry(f"{width2}x{height2}+{x2}+{y2}")
    bg_screen_game = "#9aa8e0"
    screen.config(bg=bg_screen_game)

    with open("files/users.txt", "r+") as file2:
        d = file2.read()
        s = ast.literal_eval(d)
        file2.close()

    def load():
        with open("files/users.txt", "r+") as file3:
            d = file3.read()
            s = ast.literal_eval(d)
            file3.close()

        num = s[username_signin]["score"]
        return num

    number = load()

    with open("files/signed_user.txt", "w") as file6:
        file6.write(str({"name": username_signin, "password": user_password_signin}))
        file6.close()

    def click(num):
        n = num()
        n += 1

        with open("files/users.txt", "w") as file3:
            s[username_signin]["score"] = n
            file3.write(str(s))
            file3.close()
        number = n
        if len(str(number)) >= 14 and len(str(number)) <= 16:
            counter_label.config(text=number, font=("Times New Roman", 25))
        elif len(str(number)) > 16:
            counter_label.config(text=number, font=("Times New Roman", 20))
        else:
            counter_label.config(text=number, font=("Times New Roman", 30))
        counter_label.place(anchor="center", x=width2 / 2, y=50)

    def clear():
        sound.play()
        msg_box = messagebox.askquestion('Restart Score', 'Are you sure with restart score?',
                                         icon="question")
        if msg_box == 'yes':
            with open("files/users.txt", "w") as file4:
                s[username_signin]["score"] = 0
                file4.write(str(s))
                file4.close()
            counter_label.config(text=0, font=("Times New Roman", 30))
            counter_label.place(anchor="center", x=width2 / 2, y=50)


    def log_out():
        sound.play()
        msg_box = messagebox.askquestion("Log Out", "Are you sure with log out?", icon="question")
        if msg_box == "yes":
            with open("files/signed_user.txt", "w") as file4:
                file4.write(str({}))
                file4.close()
            screen.destroy()

    frame_game = Frame(screen, bg=bg_screen_game, width=width2, height=height2)
    frame_game.place(anchor="nw", x=0, y=0)

    counter_label = Label(frame_game, bg=bg_screen_game, fg="black", text=number)
    if len(str(number)) >= 14 and len(str(number)) <= 16:
        counter_label.config(font=("Times New Roman", 25))
    elif len(str(number)) > 16:
        counter_label.config(font=("Times New Roman", 20))
    else:
        counter_label.config(font=("Times New Roman", 30))
    counter_label.place(anchor="center", x=width2 / 2, y=50)

    photo = PhotoImage(file="imgs/button.png")
    click_button = Button(frame_game, image=photo, bg=bg_screen_game, border=0, activebackground=bg_screen_game,
                          command=lambda: click(load), cursor="hand2")
    click_button.place(x=width2 / 2, y=150, anchor="center")

    clear_label = Label(frame_game, font=("Times New Roman", 8), bg=bg_screen_game, fg="black")
    clear_label.place(anchor="sw", x=6, y=148)

    photo2 = PhotoImage(file="imgs/restart.png")
    clear_button = Button(frame_game, image=photo2, bg=bg_screen_game, border=0, activebackground=bg_screen_game,
                          command=clear, cursor="hand2")
    clear_button.place(anchor="sw", x=0, y=height2)

    screen.bind("<space>", lambda event: click(load))

    restart_label = Label(frame_game, font=("Times New Roman", 8), bg=bg_screen_game, fg="black")
    restart_label.place(anchor="nw", x=width2 - 92, y=110)

    photo3 = PhotoImage(file="imgs/close_img.png")
    log_out_button = Button(frame_game, image=photo3, border=0, bg=bg_screen_game, activebackground=bg_screen_game,
                            command=log_out, cursor="hand2")
    log_out_button.place(anchor="ne", x=width2 - 1, y=63)

    def in_restart_button():
        restart_label.config(text="Sign out and save")

    def in_clear_button():
        clear_label.config(text="Restart score")

    def in_exit_button():
        exit_label.config(text="Save and leave")

    def in_list_people_button():
        people_list_label.config(text="Top 3 players")

    def out_restart_clear_button():
        restart_label.config(text="")
        clear_label.config(text="")
        exit_label.config(text="")
        people_list_label.config(text="")

    def move():
        x3 = frame_game.winfo_pointerx() - frame_game.winfo_rootx()
        y3 = frame_game.winfo_pointery() - frame_game.winfo_rooty()
        # print(f"x = {x3}")
        # print(f"y = {y3}")

        if y3 >= 62 and x3 >= 248 and y3 <= 113 and x3 <= 299:
            in_restart_button()
        elif y3 >= 146 and x3 >= 1 and y3 <= 197 and x3 <= 53:
            in_clear_button()
        elif y3 >= 8 and x3 >= 242 and y3 <= 53 and x3 <= 293:
            in_exit_button()
        elif y3 >= 128 and x3 >= 243 and y3 <= 179 and x3 <= 294:
            in_list_people_button()
        else:
            out_restart_clear_button()

    frame_game.bind("<Motion>", lambda event: move())

    if len(username_signin) <= 12:
        name_label = Label(frame_game, text=username_signin, font=("Times New Roman", 15, "bold"), fg="black",
                            bg=bg_screen_game)
    else:
        name_label = Label(frame_game, text=username_signin, font=("Times New Roman", 12, "bold"), fg="black",
                           bg=bg_screen_game)
    name_label.place(x=0, y=0)

    photo4 = PhotoImage(file="imgs/exit.png")

    exit_label = Label(frame_game, font=("Times New Roman", 8), bg=bg_screen_game, fg="black")
    exit_label.place(anchor="ne", x=width2-7, y=47)

    def exit_game():
        sound.play()
        screen.destroy()

    exit_button = Button(frame_game, image=photo4, bg=bg_screen_game, border=0, activebackground=bg_screen_game,
                         cursor="hand2", command=exit_game)
    exit_button.place(anchor="ne", x=width2 - 7, y=3)

    people_list_label = Label(frame_game, bg=bg_screen_game, fg="black", font=("Times New Roman", 8))
    people_list_label.place(anchor="ne", x=width2 - 7, y=176)

    def labels(where, score_list, names_list):
        global root
        winners_list = []
        winners_score_list = []
        for rank in range(1, where):
            the_number = max(score_list)
            player_index = score_list.index(the_number)

            winners_list.append(f"{names_list[player_index]}")
            winners_score_list.append(the_number)

            names_list.remove(names_list[player_index])
            score_list.remove(the_number)

        bg_rank = "#cce5ef"
        # bg_rank = "white"
        x4, y4 = where_window(200, 185)

        x4 += 275

        try:
            root.destroy()

        except:
            pass

        root = Toplevel()
        root.title("Rank")
        root.geometry(f"200x185+{x4}+{y4}")
        root.resizable(False, False)
        root.config(bg=bg_rank)
        root.iconbitmap("imgs/rank_ico.ico")

        frame_rank = Frame(root, bg=bg_rank, width=200, height=185, background=bg_rank)
        frame_rank.place(x=0, y=0)

        if where >= 4:
            first_colors = ["#cda226", "#7c8a94", "#775e16"]
            second_winners = [winners_list[0], winners_list[1], winners_list[2]]
            third_score = [winners_score_list[0], winners_score_list[1], winners_score_list[2]]
        elif where == 3:
            first_colors = ["#cda226", "#7c8a94"]
            second_winners = [winners_list[0], winners_list[1]]
            third_score = [winners_score_list[0], winners_score_list[1]]
        else:
            first_colors = ["#cda226"]
            second_winners = [winners_list[0]]
            third_score = [winners_score_list[0]]

        first_y = -55
        second_y = -55
        third_y = -25

        for color in first_colors:
            first_y += 60
            Label(frame_rank, fg=color, bg=bg_rank, font=("Times New Roman", 16, "bold"), text=f"{(1 + first_colors.index(color))}.").place(
                x=10, y=first_y)

        for one_score in third_score:
            third_y += 60
            Label(frame_rank, font=("Times New Roman", 14), bg=bg_rank, fg="grey", text=one_score).place(x=50, y=third_y)

        for winner in second_winners:
            if winner == username_signin:
                name_bg_color = "black"
                name_fg_color = "white"
            else:
                name_bg_color = bg_rank
                name_fg_color = "black"

            second_y += 60
            Label(frame_rank, font=("Times New Roman", 16, "bold"), bg=name_bg_color, fg=name_fg_color, text=winner).place(
                x=35, y=second_y)

        root.mainloop()

    def get_names_and_score():
        sound.play()
        names_list = []
        score_list = []
        with open("files/users.txt", "r") as file3:
            a = file3.read()
            r = ast.literal_eval(a)
            file3.close()
            for name in r.keys():
                names_list.append(name)
                score_list.append(r[name]["score"])
            if len(score_list) >= 3:
                labels(4, score_list, names_list)
            elif len(score_list) == 2:
                labels(3, score_list, names_list)
            elif len(score_list) == 1:
                labels(2, score_list, names_list)

    photo5 = PhotoImage(file="imgs/list_people.png")
    people_list_button = Button(frame_game, image=photo5, bg=bg_screen_game, border=0, activebackground=bg_screen_game,
                                cursor="hand2", command=get_names_and_score)
    people_list_button.place(anchor="ne", x=width2 - 6, y=129)

    screen.mainloop()


screen = Tk()
screen.title("Login")
width = 448
height = 250
x, y = where_window(width, height)

screen.geometry(f"448x250+{x}+{y}")
screen.resizable(False, False)
screen.iconbitmap("imgs/icon_game.ico")
screen.config(bg="white")

try:
    username_signin = d["name"]
    user_password_signin = d["password"]

    signnnnn("first", username_signin, user_password_signin)

except:
    def signup_function():
        username_signup = user_signup.get()
        user_password_signup = password_signup.get()
        user_conform_password_signup = conform_password_signup.get()

        with open("files/users.txt", "r") as file:
            d = file.read()
            r = ast.literal_eval(d)

        if (username_signup == "Nickname" or user_password_signup == "Password" or user_conform_password_signup == "Conform password") or (username_signup == "" or user_password_signup == "" or user_conform_password_signup == ""):
            messagebox.showerror("Invalid informations", "Please enter all informations!")
        elif username_signup in r.keys():
            messagebox.showerror("Nickname exists", "The entered nickname already exists")
        elif len(username_signup) < 4 or len(username_signup) > 14:
            messagebox.showerror("Invalid number of characters",
                                "Min. number of characters in nickname: 4\nMax. number of characters in nickname: 14")
        elif user_password_signup == user_conform_password_signup:
            if len(user_password_signup) < 4 or len(user_password_signup) > 14:
                messagebox.showerror("Invalid number of characters",
                                "Min. number of characters in password: 4\nMax. number of characters in password: 14")
            else:
                with open("files/users.txt", "r+") as file:
                    d = file.read()
                    r = ast.literal_eval(d)

                    new_dict = {username_signup: {"password": user_password_signup, "score": 0}}
                    r.update(new_dict)
                    file.truncate()

                with open("files/users.txt", "w") as file_2:
                    file_2.write(str(r))
                    file_2.close()
                messagebox.showinfo("Signed Up", "Succesfully signed up!")

                promeny = [user_signup, password_signup, conform_password_signup]
                names = ["Nickname", "Password", "Conform password"]

                for number in range(3):
                    promeny[number].delete(0, END)
                    promeny[number].insert(0, names[number])
                    promeny[number].config(fg="grey")

        else:
            messagebox.showerror("Doesn´t match", "Password and conform password doesn´t match!")


    def signin_function():
        sound.play()
        username_signin = user_signin.get()
        user_password_signin = password_signin.get()

        with open("files/users.txt", "r") as file:
            d = file.read()
            r = ast.literal_eval(d)
            file.close()

        if (username_signin == "Nickname" or user_password_signin == "Password") or (username_signin == "" or user_password_signin == ""):
            messagebox.showerror("Invalid informations", "Please enter all informations!")
        elif username_signin in r.keys() and user_password_signin == r[username_signin]["password"]:

            signnnnn("second", username_signin, user_password_signin)

        else:
            messagebox.showerror("Invalid", "Invalid nickname or password!")


    frames_bg = "white"
    sign_in_bg = frames_bg[:]
    sign_up_bg = frames_bg[:]
    sign_up_fg = "#293b85"

    frame_signin = Frame(screen, width=224, height=250, bg=frames_bg)
    frame_signin.place(x=0, y=0)
    frame_signup = Frame(screen, width=224, height=250, bg=frames_bg)
    frame_signup.place(x=224, y=0)

    # Kliknutí na Entry
    def click_in(who, promn):
        text = promn.get()
        if text == who:
            promn.delete(0, END)
            if promn == password_signup or promn == conform_password_signup or promn == user_signup:
                promn.config(fg=sign_up_fg)

            else:
                promn.config(fg="black")

    # Kliknutí z Entry
    def click_out(who, promn):
        text = promn.get()
        if text == "":
            promn.insert(0, who)
            promn.config(fg="grey")

    ################################# SIGN IN #############################
    # Nadpis
    heading_signin = Label(frame_signin, fg="black", bg=sign_in_bg, font=("Microsoft YaHei UI Light", 25, "bold"),
                           text="Sign In")
    heading_signin.place(x=112, y=30, anchor="center")

    # Nickname Entry
    user_signin = Entry(frame_signin, fg="grey", bg=sign_in_bg, font=("Microsoft YaHei UI Light", 11), border=0)
    user_signin.insert(0, "Nickname")
    user_signin.place(anchor="center", x=112, y=80)
    user_signin.bind("<FocusIn>", lambda event: click_in("Nickname", user_signin))
    user_signin.bind("<FocusOut>", lambda event: click_out("Nickname", user_signin))

    Frame(frame_signin, bg="black", height=2, width=165).place(anchor="center", x=112, y=92)

    # Password Entry
    password_signin = Entry(frame_signin, fg="grey", bg=sign_in_bg, font=("Microsoft YaHei UI Light", 11), border=0)
    password_signin.insert(0, "Password")
    password_signin.place(anchor="center", x=112, y=130)
    password_signin.bind("<FocusIn>", lambda event: click_in("Password", password_signin))
    password_signin.bind("<FocusOut>", lambda event: click_out("Password", password_signin))

    Frame(frame_signin, bg="black", height=2, width=165).place(anchor="center", x=112, y=142)

    # Play button
    signin_button = Button(frame_signin, text="Play", width=10, fg="white", bg="black", command=signin_function)
    signin_button.place(anchor="center", x=112, y=170)

    ########################## SIGN UP ###############################
    # Nadpis
    heading_signup = Label(frame_signup, fg=sign_up_fg, bg=sign_up_bg, font=("Microsoft YaHei UI Light", 25, "bold"),
                           text="Sign Up")
    heading_signup.place(x=112, y=30, anchor="center")

    # Nickname Entry
    user_signup = Entry(frame_signup, fg="grey", bg=sign_up_bg, font=("Microsoft YaHei UI Light", 11), border=0)
    user_signup.insert(0, "Nickname")
    user_signup.place(anchor="center", x=112, y=80)
    user_signup.bind("<FocusIn>", lambda event: click_in("Nickname", user_signup))
    user_signup.bind("<FocusOut>", lambda event: click_out("Nickname", user_signup))

    Frame(frame_signup, bg=sign_up_fg, height=2, width=165).place(anchor="center", x=112, y=92)

    # Password Entry
    password_signup = Entry(frame_signup, fg="grey", bg=sign_up_bg, font=("Microsoft YaHei UI Light", 11), border=0)
    password_signup.insert(0, "Password")
    password_signup.place(anchor="center", x=112, y=130)
    password_signup.bind("<FocusIn>", lambda event: click_in("Password", password_signup))
    password_signup.bind("<FocusOut>", lambda event: click_out("Password", password_signup))

    Frame(frame_signup, bg=sign_up_fg, height=2, width=165).place(anchor="center", x=112, y=142)

    # Conform Entry
    conform_password_signup = Entry(frame_signup, fg="grey", bg=sign_up_bg, font=("Microsoft YaHei UI Light", 11),
                                    border=0)
    conform_password_signup.insert(0, "Conform password")
    conform_password_signup.place(anchor="center", x=112, y=180)
    conform_password_signup.bind("<FocusIn>", lambda event: click_in("Conform password", conform_password_signup))
    conform_password_signup.bind("<FocusOut>", lambda event: click_out("Conform password", conform_password_signup))

    Frame(frame_signup, bg=sign_up_fg, height=2, width=165).place(anchor="center", x=112, y=192)

    # Sign Up button
    signup_button = Button(frame_signup, text="Sign Up", width=15, bg=sign_up_fg, fg="white", command=signup_function)
    signup_button.place(anchor="center", x=112, y=220)

    screen.mainloop()
