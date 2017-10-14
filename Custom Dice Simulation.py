from tkinter import *
import random

#Function for player dice
def player():
    odd = random.randrange(1,9,1)
    switcher = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 5,
        7: 5,
        8: 6,
        }
    return switcher[odd]

#Function for bank dice
def bank():
    reg = int(random.randrange(1,7,1))
    return reg

#Function for probability
def prob():
    global total_trials
    global bank_win_prob
    global player_win_prob
    total_trials += 1
    total_trials_label.config(text = "Total Trials: " + str(total_trials))
    bank_win_prob = round(bank_win_num / total_trials, 5)
    player_win_prob = round(player_win_num / total_trials, 5)
    bank_win_prob_label.config(text = "Bank Win Probability: " + str(bank_win_prob))
    player_win_prob_label.config(text = "Player Win Probability: " + str(player_win_prob))

#Variable setup for win counters
bank_win_num = 0
player_win_num = 0
bank_win_prob = 0
player_win_prob = 0
total_trials = 0

#Tkinter window setup
main = Tk()
main.title("Custom Dice Simulator")
main.geometry("500x275")

#Bank dice images setup
one_bank = PhotoImage(file = "1_bank.gif")
two_bank = PhotoImage(file = "2_bank.gif")
three_bank = PhotoImage(file = "3_bank.gif")
four_bank = PhotoImage(file = "4_bank.gif")
five_bank = PhotoImage(file = "5_bank.gif")
six_bank = PhotoImage(file = "6_bank.gif")

#Player dice images setup
one_player = PhotoImage(file = "1_player.gif")
two_player = PhotoImage(file = "2_player.gif")
three_player = PhotoImage(file = "3_player.gif")
four_player = PhotoImage(file = "4_player.gif")
five_player = PhotoImage(file = "5_player.gif")
six_player = PhotoImage(file = "6_player.gif")

#Who wins label setup
win_label = Label(main, text="")
win_label.pack()

#Player roll label
player_label = Label(main, text="Player \n Rolled: ")
player_label.place(x=60, y= 100)

#Bank roll label
bank_label = Label(main, text="Bank \n Rolled: ")
bank_label.place(x=60, y = 35)

#Bank die label
bank_die = Label(main)
bank_die.place(x = 120, y = 30)

#Player die label
player_die = Label(main)
player_die.place(x = 120, y = 95)

#Bank die label 2
bank_die_2 = Label(main)
bank_die_2.place(x = 180, y = 30)

#Player die label 2
player_die_2 = Label(main)
player_die_2.place(x = 180, y = 95)

#Bank die label 3
bank_die_3 = Label(main)
bank_die_3.place(x = 240, y = 30)

#Player die label 3
player_die_3 = Label(main)
player_die_3.place(x = 240, y = 95)

#Bank die label 4
bank_die_4 = Label(main)
bank_die_4.place(x = 300, y = 30)

#Player die label 4
player_die_4 = Label(main)
player_die_4.place(x = 300, y = 95)

#Bank die label 5
bank_die_5 = Label(main)
bank_die_5.place(x = 360, y = 30)

#Player die label 5
player_die_5 = Label(main)
player_die_5.place(x = 360, y = 95)

#Bank win counter label
bank_win_label = Label(main, text="Bank Wins: " + str(bank_win_num))
bank_win_label.place(y = 160)

#Player win counter label
player_win_label = Label(main, text="Player Wins: " + str(player_win_num))
player_win_label.place(y = 180)

#Total Trials
total_trials_label = Label(main, text = "Total Trials: " + str(total_trials))
total_trials_label.place(y=200)

#Bank win probability label
bank_win_prob_label = Label(main, text = "Bank Win Probability: " + str(bank_win_prob))
bank_win_prob_label.place(y = 225)

#Player win probability label
player_win_prob_label = Label(main, text = "Player Win Probability: " + str(player_win_prob))
player_win_prob_label.place(y = 245)

#Simulation Number Label
sim_num_label = Label(main, text = "Number of Simulations")
sim_num_label.place(y=215, x = 285)

#Dice Number Label
dice_num_label = Label(main, text = "Number\nof Dice")
dice_num_label.place(x = 5, y = 0)

#Number of simulations Label
sim_num_entry = Entry(main, width = 5)
sim_num_entry.place(y = 210, x = 435)

#Option Menu for Bank Dice
bank_dice_num_options = StringVar(main)
bank_dice_num_options.set("1")
bank_dice_num_opt_menu = OptionMenu(main, bank_dice_num_options, "1", "2", "3", "4", "5")
bank_dice_num_opt_menu.config(width = 5)
bank_dice_num_opt_menu.place(y=40)
bank_dice_num_real = int(bank_dice_num_options.get())

#Option Menu for Player Dice
player_dice_num_options = StringVar(main)
player_dice_num_options.set("1")
player_dice_num_opt_menu = OptionMenu(main, player_dice_num_options, "1", "2", "3", "4", "5")
player_dice_num_opt_menu.config(width = 5)
player_dice_num_opt_menu.place(y=100)
player_dice_num_real = int(player_dice_num_options.get())

#Function for closing window
def close_window():
    main.destroy()

#Bank Die 1 Images
def bank_die_images(banknum):
    if banknum == 1:
        bank_die.config(image = one_bank)
    elif banknum == 2:
        bank_die.config(image = two_bank)
    elif banknum == 3:
        bank_die.config(image = three_bank)
    elif banknum == 4:
        bank_die.config(image = four_bank)
    elif banknum == 5:
        bank_die.config(image = five_bank)
    elif banknum == 6:
        bank_die.config(image = six_bank)

#Bank Die 2 Images
def bank_die_2_images(banknum2):
    if banknum2 == 1:
        bank_die_2.config(image = one_bank)
    elif banknum2 == 2:
        bank_die_2.config(image = two_bank)
    elif banknum2 == 3:
        bank_die_2.config(image = three_bank)
    elif banknum2 == 4:
        bank_die_2.config(image = four_bank)
    elif banknum2 == 5:
        bank_die_2.config(image = five_bank)
    elif banknum2 == 6:
        bank_die_2.config(image = six_bank)

#Bank Die 3 Images
def bank_die_3_images(banknum3):
    if banknum3 == 1:
        bank_die_3.config(image = one_bank)
    elif banknum3 == 2:
        bank_die_3.config(image = two_bank)
    elif banknum3 == 3:
        bank_die_3.config(image = three_bank)
    elif banknum3 == 4:
        bank_die_3.config(image = four_bank)
    elif banknum3 == 5:
        bank_die_3.config(image = five_bank)
    elif banknum3 == 6:
        bank_die_3.config(image = six_bank)

#Bank Die 4 Images
def bank_die_4_images(banknum4):
    if banknum4 == 1:
        bank_die_4.config(image = one_bank)
    elif banknum4 == 2:
        bank_die_4.config(image = two_bank)
    elif banknum4 == 3:
        bank_die_4.config(image = three_bank)
    elif banknum4 == 4:
        bank_die_4.config(image = four_bank)
    elif banknum4 == 5:
        bank_die_4.config(image = five_bank)
    elif banknum4 == 6:
        bank_die_4.config(image = six_bank)
        
#Bank Die 5 Images
def bank_die_5_images(banknum5):
    if banknum5 == 1:
        bank_die_5.config(image = one_bank)
    elif banknum5 == 2:
        bank_die_5.config(image = two_bank)
    elif banknum5 == 3:
        bank_die_5.config(image = three_bank)
    elif banknum5 == 4:
        bank_die_5.config(image = four_bank)
    elif banknum5 == 5:
        bank_die_5.config(image = five_bank)
    elif banknum5 == 6:
        bank_die_5.config(image = six_bank)

#Player Die 1 Images
def player_die_images(playnum):
    if playnum == 1:
        player_die.config(image = one_player)
    elif playnum == 2:
        player_die.config(image = two_player)
    elif playnum == 3:
        player_die.config(image = three_player)
    elif playnum == 4:
        player_die.config(image = four_player)
    elif playnum == 5:
        player_die.config(image = five_player)
    elif playnum == 6:
        player_die.config(image = six_player)
        
#Player Die 2 Images
def player_die_2_images(playnum2):   
    if playnum2 == 1:
        player_die_2.config(image = one_player)
    elif playnum2 == 2:
        player_die_2.config(image = two_player)
    elif playnum2 == 3:
        player_die_2.config(image = three_player)
    elif playnum2 == 4:
        player_die_2.config(image = four_player)
    elif playnum2 == 5:
        player_die_2.config(image = five_player)
    elif playnum2 == 6:
        player_die_2.config(image = six_player)
#Player Die 3 Images
def player_die_3_images(playnum3):
    if playnum3 == 1:
        player_die_3.config(image = one_player)
    elif playnum3 == 2:
        player_die_3.config(image = two_player)
    elif playnum3 == 3:
        player_die_3.config(image = three_player)
    elif playnum3 == 4:
        player_die_3.config(image = four_player)
    elif playnum3 == 5:
        player_die_3.config(image = five_player)
    elif playnum3 == 6:
        player_die_3.config(image = six_player)

#Player Die 4 Images
def player_die_4_images(playnum4):
    if playnum4 == 1:
        player_die_4.config(image = one_player)
    elif playnum4 == 2:
        player_die_4.config(image = two_player)
    elif playnum4 == 3:
        player_die_4.config(image = three_player)
    elif playnum4 == 4:
        player_die_4.config(image = four_player)
    elif playnum4 == 5:
        player_die_4.config(image = five_player)
    elif playnum4 == 6:
        player_die_4.config(image = six_player)

#Player Die 5 Images
def player_die_5_images(playnum5):
    if playnum5 == 1:
        player_die_5.config(image = one_player)
    elif playnum5 == 2:
        player_die_5.config(image = two_player)
    elif playnum5 == 3:
        player_die_5.config(image = three_player)
    elif playnum5 == 4:
        player_die_5.config(image = four_player)
    elif playnum5 == 5:
        player_die_5.config(image = five_player)
    elif playnum5 == 6:
        player_die_5.config(image = six_player
                            )


#Function for roll button
def bank_top_dice_funct(bank_dice_num):

    #Clear Dice Images

    bank_die.config(image = "")
    bank_die_2.config(image = "")
    bank_die_3.config(image = "")
    bank_die_4.config(image = "")
    bank_die_5.config(image = "")

    #Number of Bank Dice and Connecting that to the images and 
    if bank_dice_num == 1:
        banknum = bank()
        bank_die_images(banknum)
        bank_top_num = banknum
    elif bank_dice_num == 2:
        banknum = bank()
        banknum2 = bank()
        bank_die_images(banknum)
        bank_die_2_images(banknum2)
        if banknum >= banknum2:
            bank_top_num = banknum
        elif banknum2 > banknum:
            bank_top_num = banknum2
    elif bank_dice_num == 3:
        banknum = bank()
        banknum2 = bank()
        banknum3 = bank()
        bank_die_images(banknum)
        bank_die_2_images(banknum2)
        bank_die_3_images(banknum3)
        if banknum >= banknum2:
            bank_top_num = banknum
        elif banknum2 > banknum:
            bank_top_num = banknum2
        if bank_top_num < banknum3:
            bank_top_num = banknum3
    elif bank_dice_num == 4:
        banknum = bank()
        banknum2 = bank()
        banknum3 = bank()
        banknum4 = bank()
        bank_die_images(banknum)
        bank_die_2_images(banknum2)
        bank_die_3_images(banknum3)
        bank_die_4_images(banknum4)
        if banknum >= banknum2:
            bank_top_num = banknum
        elif banknum2 > banknum:
            bank_top_num = banknum2
        if bank_top_num < banknum3:
            bank_top_num = banknum3
        if bank_top_num < banknum4:
            bank_top_num = banknum4
    elif bank_dice_num == 5:
        banknum = bank()
        banknum2 = bank()
        banknum3 = bank()
        banknum4 = bank()
        banknum5 = bank()
        bank_die_images(banknum)
        bank_die_2_images(banknum2)
        bank_die_3_images(banknum3)
        bank_die_4_images(banknum4)
        bank_die_5_images(banknum5)
        if banknum >= banknum2:
            bank_top_num = banknum
        elif banknum2 > banknum:
            bank_top_num = banknum2
        if bank_top_num < banknum3:
            bank_top_num = banknum3
        if bank_top_num < banknum4:
            bank_top_num = banknum4
        if bank_top_num < banknum5:
            bank_top_num = banknum5
            
    return bank_top_num

def player_top_dice_fuct(player_dice_num):
        
    #Clear Dice Images
        
    player_die.config(image = "")
    player_die_2.config(image = "")
    player_die_3.config(image = "")
    player_die_4.config(image = "")
    player_die_5.config(image = "")
    
    if player_dice_num == 1:
        playnum = player()
        player_die_images(playnum)
        player_top_num = playnum
        
    elif player_dice_num == 2:
        playnum = player()
        playnum2 = player()
        player_die_images(playnum)
        player_die_2_images(playnum2)
        if playnum >= playnum2:
            player_top_num = playnum
        elif playnum2 > playnum:
            player_top_num = playnum2
            
    elif player_dice_num == 3:
        playnum = player()
        playnum2 = player()
        playnum3 = player()
        player_die_images(playnum)
        player_die_2_images(playnum2)
        player_die_3_images(playnum3)
        if playnum >= playnum2:
            player_top_num = playnum
        elif playnum2 > playnum:
            player_top_num = playnum2
        if player_top_num < playnum3:
            player_top_num = playnum3
            
    elif player_dice_num == 4:
        playnum = player()
        playnum2 = player()
        playnum3 = player()
        playnum4 = player()
        player_die_images(playnum)
        player_die_2_images(playnum2)
        player_die_3_images(playnum3)
        player_die_4_images(playnum4)
        if playnum >= playnum2:
            player_top_num = playnum
        elif playnum2 > playnum:
            player_top_num = playnum2
        if player_top_num < playnum3:
            player_top_num = playnum3
        if player_top_num < playnum4:
            player_top_num = playnum4
            
    elif player_dice_num == 5:
        playnum = player()
        playnum2 = player()
        playnum3 = player()
        playnum4 = player()
        playnum5 = player()
        player_die_images(playnum)
        player_die_2_images(playnum2)
        player_die_3_images(playnum3)
        player_die_4_images(playnum4)
        player_die_5_images(playnum5)
        if playnum >= playnum2:
            player_top_num = playnum
        elif playnum2 > playnum:
            player_top_num = playnum2
        if player_top_num < playnum3:
            player_top_num = playnum3
        if player_top_num < playnum4:
            player_top_num = playnum4
        if player_top_num < playnum5:
            player_top_num = playnum5

    return player_top_num

#Roll Button Function
def roll():
    
    #Global variables for function
    global bank_win_num
    global player_win_num

    bank_dice_num_real = int(bank_dice_num_options.get())
    player_dice_num_real = int(player_dice_num_options.get())
    
    bank_top_num = bank_top_dice_funct(bank_dice_num_real)
    player_top_num = player_top_dice_fuct(player_dice_num_real)

    #Determining if Bank or Player Wins
    if bank_top_num >= player_top_num:
        win_label.config(text = "Bank Wins!")
        bank_win_num = bank_win_num + 1
        bank_win_label.config(text = "Bank Wins: " + str(bank_win_num))
        prob()

    #When the player beats the bank 
    elif player_top_num > bank_top_num:
        win_label.config(text = "Player Wins!")
        player_win_num = player_win_num + 1
        player_win_label.config(text = "Player Wins: " + str(player_win_num))
        prob()
    
    
#Sim Button Function

def sim():
    sim_num = sim_num_entry.get()
    if str(sim_num) == "":
        sim_num = 0
    else:
        sim_num = int(sim_num)
    for i in range(0,sim_num):
        global bank_win_num
        global player_win_num

        bank_dice_num_real = int(bank_dice_num_options.get())
        player_dice_num_real = int(player_dice_num_options.get())
           
        bank_top_num = bank_top_dice_funct(bank_dice_num_real)
        player_top_num = player_top_dice_fuct(player_dice_num_real)
        
        #Clear Dice Images
        
        player_die.config(image = "")
        player_die_2.config(image = "")
        player_die_3.config(image = "")
        player_die_4.config(image = "")
        player_die_5.config(image = "")
        bank_die.config(image = "")
        bank_die_2.config(image = "")
        bank_die_3.config(image = "")
        bank_die_4.config(image = "")
        bank_die_5.config(image = "")
        win_label.config(text = "Simulation Complete")


        #When bank beats player 
        if bank_top_num >= player_top_num:
            bank_win_num = bank_win_num + 1
            bank_win_label.config(text = "Bank Wins: " + str(bank_win_num))
            prob()

        #When the player beats the bank 
        elif player_top_num > bank_top_num:
            player_win_num = player_win_num + 1
            player_win_label.config(text = "Player Wins: " + str(player_win_num))
            prob()

#Clear Function
def clear():
        global bank_win_num
        global player_win_num
        global bank_win_prob
        global player_win_prob
        global total_trials
        player_die.config(image = "")
        player_die_2.config(image = "")
        player_die_3.config(image = "")
        player_die_4.config(image = "")
        player_die_5.config(image = "")
        bank_die.config(image = "")
        bank_die_2.config(image = "")
        bank_die_3.config(image = "")
        bank_die_4.config(image = "")
        bank_die_5.config(image = "")
        win_label.config(text = "Clearing Complete")
        bank_win_num = 0
        player_win_num = 0
        bank_win_prob = 0
        player_win_prob = 0
        total_trials = 0
        bank_win_label.config(text = "Bank Wins: " + str(bank_win_num))
        player_win_label.config(text = "Player Wins: " + str(player_win_num))
        bank_win_prob_label.config(text = "Bank Win Probability: " + str(bank_win_prob))
        player_win_prob_label.config(text = "Player Win Probability: " + str(player_win_prob))
        total_trials_label.config(text = "Total Trials: " + str(total_trials))
        
#Roll button
roll_button = Button(main, text="Roll Once", command = roll)
roll_button.place(x = 215, y = 245)

#Run Sim Button
sim_button = Button(main, text="Run Sim", command = sim)
sim_button.place(x = 302, y = 245)

#Clear Button
clear_button = Button(main, text="Clear", command = clear)
clear_button.place(x = 381, y = 245)

#Quit Button
quit_button = Button(main, text="Quit", command = close_window)
quit_button.place(x = 441, y = 245)
main.mainloop()
