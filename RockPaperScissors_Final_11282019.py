
#we import these two class because we need them in our code
from tkinter import *

import random, time

# All images were drawn by Dennis Phan

# This is our code for the game, rock,paper,scissors

# our code is run & divided into different chunk of functions
# The overall view of the code is this (in order):
# 0.the starting code: (where)-at the most bottom part of the entire program written (what)-set global variables{user_score,bot_score...etc}, Start the starting screen
# 1.starting screen: (where)-at the top most of our code (what)-introduce the user to our game, give them rules, let the user click to start choosing screen
# 2.choosing screen:(where)-under the starting screen (what)- allow the user to choose their opponent{bots}that behave differently.
# 3.After the user have choose the bot, the game will run using that specific {bot function}
# 3.1 (Monkey bot)-always tie with the user,the code is right under choosing screen, 3.2 (average joe bot)-will guess rock paper scissors randomly, code is under monkey bot, 3.3 (Brain bot)-will "learn" from the user's guessing pattern everytime it wins or lose, code is under the avg joe bot

# All the bot have similar code, Code for each bot have similar structure of (in order):
# i).(setting up game screen) -display score, graphic and rock paper scissors bottons that would input the user's choice,run the logic scheme and change score according to who win, the bottons will also run function that checks whether game ends 
# ii).By looking at the round count, the program would decide whether the game ends, it would then decide who wins and give out winner,loser or dra screen accordingly
#
# I will then explain the design choice beside each code

def Start_Starting_Screen(): #from: https://www.tutorialspoint.com/python/python_gui_programming.htm
    #Loading up the basic of a empty Starting Screen    
    Starting_Screen =Tk() #from: https://www.tutorialspoint.com/python/python_gui_programming.htm
        
    Starting_Screen.title("Rock Paper Scissors") # from: https://www.tutorialspoint.com/python/python_gui_programming.htm
    
    Starting_Screen.geometry("1071x400") # from:https://www.tutorialspoint.com/python/python_gui_programming.htm
    #This fuctions are defined to runs when the button is clicked, when user click the button, the interface is gonna close and and the program is going to move on to the next screen 
      
    
    def To_Choosing_Screen ():
        Starting_Screen.destroy()
        Start_Choosing_Screen()
    
     
    #These are the features we add on to the Starting screens
    Starting_sentence=Label(Starting_Screen)
    #this paths the image file on the computer
    img = PhotoImage(file="D:/RPS/rockpaperscissors.gif")  #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    Starting_sentence.config(image=img)  #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    Starting_sentence.pack()  #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    Starting_sentence.place(x=0,y=0)
    
    rl=Label(Starting_Screen)
    imgrule = PhotoImage(file="D:/rps/rules_list.gif")  #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    rl.config(image=imgrule) #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    rl.pack() #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    rl.place(x=635,y=0) 
    

     
           
    
    Start_button=Button(Starting_Screen,text="start!",bd=25,font=100, command = To_Choosing_Screen) #from: https://www.youtube.com/watch?v=QPeS0TI0yNo
    img1 = PhotoImage(file="D:/rps/start.png") #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    Start_button.config(image=img1)  #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    Start_button.pack()      #from stockoverflow.com/questions/10133856/how-to-add-an-image-in-tkinter
    Start_button.place(x=760,y=310)
    

    
    #This is just a reqiured code for the interface to run
    #it creates a loop for the entire interface without it, the code wont run and nothing will show up 
    #besides the size and the title of the window
    Starting_Screen.mainloop()
    



#This stage is when the user choose which bot they want to play against
def Start_Choosing_Screen():
    #Loading up the empty choosing screen
    Choosing_Screen=Tk()
        
    Choosing_Screen.title("Choose your challenger!")
    
    Choosing_Screen.geometry("700x600")

    #Setting up functions so that when the user clicked the corresponding botton, the program is gonna move on to the corresponding gamemode    
    def To_Game_Screen_avg_joe():
        Choosing_Screen.destroy()
        Start_Game_Screen_avg_joe()
        
    def To_Game_Screen_monkey ():
        Choosing_Screen.destroy()
        Start_Game_Screen_monkey()
        
    def To_Game_Screen_brain():
        Choosing_Screen.destroy()
        Start_Game_Screen_brain()
    
    
    #Features for the choosing screen     
    Sentence=Label(Choosing_Screen)
    challenger_img = PhotoImage(file="D:/rps/choose_your_challenger.gif")
    Sentence.config(image=challenger_img)
    Sentence.pack()     
    Sentence.place(x=170,y=70)    
    
    choose_bot1=Button(Choosing_Screen,text="bot1",bd=2,font=100, command = To_Game_Screen_avg_joe)
    img123 = PhotoImage(file="D:/rps/average_joe.png")
    choose_bot1.config(image=img123)
    choose_bot1.pack()     
    choose_bot1.place(x=10,y=120)
     
    
    choose_bot2=Button(Choosing_Screen,text="bot2",bd=2,font=100, command = To_Game_Screen_monkey)
    monkey = PhotoImage(file="D:/rps/monkey_see_monkey_do.png")
    choose_bot2.config(image=monkey)
    choose_bot2.pack()     
    choose_bot2.place(x=220,y=140)
     
    
    choose_bot3=Button(Choosing_Screen,text="bot3",bd=2,font=100, command = To_Game_Screen_brain)
    img3 = PhotoImage(file="D:/rps/brain.png")
    choose_bot3.config(image=img3)
    choose_bot3.pack()    
    choose_bot3.place(x=500,y=140)
    
    #Essential thing for any interface
    Choosing_Screen.mainloop()
    
    
def Start_Game_Screen_monkey():
    #Setting up the basic empty monkey game screen
    Game_Screen_monkey=Tk()    
    Game_Screen_monkey.title("Gaming screen")
    Game_Screen_monkey.geometry("760x520")
    
    # functions for the quit button, it simply close the interface        
    def close_window ():
            Game_Screen_monkey.destroy()
        

            # We make these variable quantities global, not only because these variables are used in many different functions in our code-save us from confusion over naming seperate variable, but to also make these quantities throughout our entire program editable by functions. 
            #This code right here is just to state the global variables into the function so that the function will run with these global variables    
    global rnd,user_score,user_choice,bot_score,Num_of_Draw
    
    
    #Displaying score board,round number when the interface pop up, before the user clicked any button
    Show_user_score=Label(Game_Screen_monkey,text="Your score : "+str(user_score), font = ('gothic',12)) #from https://www.youtube.com/watch?v=9Kdn9uIYhKw 
    Show_user_score.place(x=420,y=450)
    
  
    Show_bot_score=Label(Game_Screen_monkey,text="Challenger's score : "+str(bot_score),font = ('gothic',12)) #from https://www.youtube.com/watch?v=9Kdn9uIYhKw 
    Show_bot_score.place(x=20,y=450)    
    
    Show_Number_of_Draw=Label(Game_Screen_monkey,text="Draw counter : "+str(Num_of_Draw),font = ('gothic',12)) #from https://www.youtube.com/watch?v=9Kdn9uIYhKw 
    Show_Number_of_Draw.place(x=220,y=450)     
    
    choices = ("r","p","s")
    
    
    Showround=Label(Game_Screen_monkey,text="Round: "+str(rnd), font = ('gothic',12))       
    Showround.place(x=280,y=100)  
    

    # These are functions that get triggered when the user clicked on rock or paper or scissors botton, These functions will input user choice, choose choices for bot, run the logic of the game, decide who wins the round and return the new value of scores and rounds
    # We make play rock,play scissors and play paper into separate functions because we want the code to input the corresponding user choice when the user clicked a specific rock,paper,scissors button 
    
    def play_rock():
        global user_choice
        user_choice="r"
        run_monkey()
    #These end checks at the bottom of the functions make sure that the program knows when to end the game, every time after the program runs and return scores, it would see if the game ends.
        endcheck_monkey()
    def play_paper():
        global user_choice
        user_choice="p"
        run_monkey()
        endcheck_monkey()
        
    def play_scissors():
        global user_choice
        user_choice="s" 
        run_monkey()
        endcheck_monkey()

    
    #These are the Key Feature for the Monkey game screen, displaying monkey and buttons    
    overlay=Label(Game_Screen_monkey)
    overlay_img = PhotoImage(file="D:/rps/overlay_test.png")
    overlay.config(image=overlay_img)
    overlay.pack()
    overlay.place(x=0,y=0)
    
    #We have a exit botton, it just a nice thing to have in a game design
    Exit=Button(Game_Screen_monkey,text="Exit game",bd=25,font = ('gothic',12), command = close_window)
    Exit.place(x=600,y=420)      
    
    #Instead of displaying text on the rock,paper scissors buttons, we use pictures to show rock, paper, scissors.
    rock=Button(Game_Screen_monkey,text="rock",bd=2,font=100, command= play_rock )
    rock_img = PhotoImage(file="D:/rps/rock.png")
    rock.config(image=rock_img)
    rock.pack()     
    rock.place(x=23,y=225)
         
        
    paper=Button(Game_Screen_monkey,text="paper",bd=2,font=100, command = play_paper)
    paper_img = PhotoImage(file="D:/rps/paper.png")
    paper.config(image=paper_img)
    paper.pack()     
    paper.place(x=220,y=205)
         
     
    scissors=Button(Game_Screen_monkey,text="scissors",bd=2,font=100, command = play_scissors)
    scissors_img = PhotoImage(file="D:/rps/scissors.png")
    scissors.config(image=scissors_img)
    scissors.pack()
    scissors.place(x=483,y=203)
        
    
    #This is the logic part of the game, it triggered every time when the user clicked the button, it takes in user choice, make up a bot choice, decide who win then return score, paste new score and round onto score & round board 
    def run_monkey():
        #we have to restate these global variables again because this run function is a sepapate function then the game screen function
        global rnd,user_score,user_choice,bot_score,Num_of_Draw
        
        #This is a unique feature for the gamemode of playing against the monkey, it will always tie with you
        bot_choice = user_choice 
        
        #This code is to display result, it simply paste a text on the game screen
        if user_choice == bot_choice : #all these outcomes from rock, paper, scissors from https://www.youtube.com/watch?v=9Kdn9uIYhKw 

            Show_result=Label(Game_Screen_monkey,text="Draw! You and the challenger picked the same choice!                                                                                                                                     ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
            Num_of_Draw=Num_of_Draw+1
            Show_Number_of_Draw=Label(Game_Screen_monkey,text="Draw counter:  "+str(Num_of_Draw),font = ('gothic',12))
            Show_Number_of_Draw.place(x=220,y=450)            
                
      
                
        #The run function will take in the global variable "rnd"-roundnumber and add one to it every time the function runs
        #The code below is to add 1 to "rnd" and paste a new round board on top of the previous round board.
        rnd=rnd+1
        Showround=Label(Game_Screen_monkey,text="Round: "+str(rnd), font = ('gothic',12))
        Showround.place(x=280,y=100)         
                
        #Then the code release the new round number and score back into global variable, setting the global variable into new value
        return rnd,user_score,user_choice,bot_score,Num_of_Draw
 
    #This is the function behind the how the program check if the game ends,it check whether the round number reach the end, compare user and bot's score then run the function that would display corresponding winner & loser screen
    #Of course, since the monkey bot will always try to tie with you, we don't need to compare score or display who win and who lost, we just have to check round number and display draw screen when game ends 
    def endcheck_monkey():
        global rnd,user_score,user_choice,bot_score,Num_of_Draw
        if rnd==6:
                time.sleep(1)
                Game_Screen_monkey.destroy()
               #To display draw screen
                draw_monkey()
        
    
            
    Game_Screen_monkey.mainloop()            


    
def draw_monkey():
    #Display Draw screen, 
    Draw_screen=Tk()
    Draw_screen.title("Draw!")
    Draw_screen.geometry("414x146")
  
    draw_label=Label(Draw_screen)
    draw_img1 = PhotoImage(file="D:/rps/draw.png")
    draw_label.config(image=draw_img1)
    draw_label.pack()
    draw_label.place(x=0,y=0)  
    
    Draw_screen.mainloop()
    










# average joe will play rock paper scissors using random generator, the code for the gamemode is similar to how the monkeygamemode is run , expect minor differences that I will explain at the botoom
def Start_Game_Screen_avg_joe():
   #The code here have identical structure to the monkey gamemode, expect different image to display joe
    Game_Screen=Tk()    
    Game_Screen.title("gaming screen")
    Game_Screen.geometry("760x520")
            
    def close_window ():
            Game_Screen.destroy()
        

    
    global rnd,user_score,user_choice,bot_score,Num_of_Draw
    
    Show_user_score=Label(Game_Screen,text="Your score : "+str(user_score), font = ('gothic',12))
    Show_user_score.place(x=420,y=450)
    
  
    Show_bot_score=Label(Game_Screen,text="Challenger's score : "+str(bot_score),font = ('gothic',12))
    Show_bot_score.place(x=20,y=450)    
    
    Show_Number_of_Draw=Label(Game_Screen,text="Draw counter : "+str(Num_of_Draw),font = ('gothic',12))
    Show_Number_of_Draw.place(x=220,y=450)     
    
    choices = ("r","p","s")
    
    
    Showround=Label(Game_Screen,text="Round: "+str(rnd), font = ('gothic',12))       
    Showround.place(x=280,y=100)  
    

    
    def play_rock():
        global user_choice
        user_choice="r"
        #different run function name than run_monkey or run_brain to avoid confusion, bascally run() means run_Joe()
        run()
        end_check()
    def play_paper():
        global user_choice
        user_choice="p"
        run()
        end_check()
        
    def play_scissors():
        global user_choice
        user_choice="s" 
        run()
        end_check()

    
    overlay=Label(Game_Screen)
    overlay_img = PhotoImage(file="D:/rps/overlay_avg_joe.png")
    overlay.config(image=overlay_img)
    overlay.pack()
    overlay.place(x=0,y=0)
    
    Exit=Button(Game_Screen,text="Exit game",bd=25,font = ('gothic',12), command = close_window)
    Exit.place(x=600,y=420)      
    
    rock=Button(Game_Screen,text="rock",bd=2,font=100, command= play_rock )
    rock_img = PhotoImage(file="D:/rps/rock.png")
    rock.config(image=rock_img)
    rock.pack()     
    rock.place(x=23,y=225)
         
        
    paper=Button(Game_Screen,text="paper",bd=2,font=100, command = play_paper)
    paper_img = PhotoImage(file="D:/rps/paper.png")
    paper.config(image=paper_img)
    paper.pack()     
    paper.place(x=220,y=205)
         
     
    scissors=Button(Game_Screen,text="scissors",bd=2,font=100, command = play_scissors)
    scissors_img = PhotoImage(file="D:/rps/scissors.png")
    scissors.config(image=scissors_img)
    scissors.pack()
    scissors.place(x=483,y=203)
        
    
    
    def run():
        
        global rnd,user_score,user_choice,bot_score,Num_of_Draw
        
        
        bot_choice = random.choice(choices)
       # We use separate if&elif statement to display all possible win or lose result, we want to be specific because it is much more entertaining for the user to see both player's choice compare to only knowing who win the run       
        if user_choice == bot_choice :
         # We paste a new score board on top of the old ones everytime when we are updateing it
            Show_result=Label(Game_Screen,text="Draw! You and the challenger picked the same choice!                                                                                                                                     ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
            #it is good game design to see the number of draw between user and the bot
            Num_of_Draw=Num_of_Draw+1
            Show_Number_of_Draw=Label(Game_Screen,text="Draw counter:  "+str(Num_of_Draw),font = ('gothic',12))
            Show_Number_of_Draw.place(x=220,y=450)            
                
        elif user_choice == "r" and bot_choice == "s" :
            Show_result=Label(Game_Screen,text="You picked rock, Challenger picked scissor. Rock blunts scissors, You win this round!                    ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
            
            user_score = user_score + 1
            Show_user_score=Label(Game_Screen,text="Your score:  "+str(user_score),font = ('gothic',12))
            Show_user_score.place(x=420,y=450)            
        elif user_choice == "p" and bot_choice == "r" :
            Show_result=Label(Game_Screen,text="You picked paper, Challenger pioked rock. Paper covers rock, You won this round!                     ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
            
            user_score = user_score + 1
            Show_user_score=Label(Game_Screen,text="Your score:  "+str(user_score),font = ('gothic',12))
            Show_user_score.place(x=420,y=450)            
        elif user_choice== "s" and bot_choice == "p" :
            Show_result=Label(Game_Screen,text="You picked scissors, Challenger picked paper. Scissors cuts paper, You won this round!                          ",font = ('gothic',12))
            Show_result.place(x=10,y=150) 
            
            user_score = user_score + 1
            Show_user_score=Label(Game_Screen,text="Your score:  "+str(user_score),font = ('gothic',12))
            Show_user_score.place(x=420,y=450)            
        elif user_choice == "r" and bot_choice == "p" :
                Show_result=Label(Game_Screen,text="You picked rock, Challenger picked paper. Paper covers rock, Challenger won this round!                           ",font = ('gothic',12))
                Show_result.place(x=10,y=150)
                
                bot_score = bot_score + 1
                Show_bot_score=Label(Game_Screen,text="Challenger's score:  "+str(bot_score),font = ('gothic',12))
                Show_bot_score.place(x=20,y=450)            
        elif user_choice == "p" and bot_choice == "s" :
                Show_result=Label(Game_Screen,text="You picked paper, Challenger picked scissors. Scissors cuts paper, Challenger won this round!          ",font = ('gothic',12))
                Show_result.place(x=10,y=150)
                
                bot_score = bot_score + 1
                Show_bot_score=Label(Game_Screen,text="Challenger's score:  "+str(bot_score),font = ('gothic',12))
                Show_bot_score.place(x=20,y=450)            
        elif user_choice == "s" and bot_choice == "r"  :
                Show_result=Label(Game_Screen,text="You picked scissors, Challenger picked rock. Rock blunts scissors, Challenger won this round!           ",font = ('gothic',12))
                Show_result.place(x=10,y=150)
            
                bot_score = bot_score + 1
                Show_bot_score=Label(Game_Screen,text="Challenger's score:  "+str(bot_score),font = ('gothic',12))
                Show_bot_score.place(x=20,y=450)
       
            
            
            
                
                
        
        rnd=rnd+1
        Showround=Label(Game_Screen,text="Round: "+str(rnd), font = ('gothic',12))
        Showround.place(x=280,y=100)         
                
        
        return rnd,user_score,user_choice,bot_score,Num_of_Draw
 #These functions will display different screens according to the result in the end check function below
    def user_win_joe():
        
        Winner_Screen=Tk() 
        Winner_Screen.title("You are the winner!")
        Winner_Screen.geometry("519x149")    
        
        win=Label(Winner_Screen)
        win_img = PhotoImage(file="D:/rps/winner.png")
        win.config(image=win_img)
        win.pack()
        win.place(x=0,y=0)   
        
        Winner_Screen.mainloop()
    
    
    
    
    def bot_win_joe():
        
        Loser_screen=Tk()
        Loser_screen.title("You lost!")
        Loser_screen.geometry("424x129")
        
        loser=Label(Loser_screen)
        loser_img = PhotoImage(file="D:/rps/loser.png")
        loser.config(image=loser_img)
        loser.pack()
        loser.place(x=0,y=0) 
        
        Loser_screen.mainloop()
        
    def draw_joe():    
        Draw_screen=Tk()
        Draw_screen.title("Draw!")
        Draw_screen.geometry("414x146")
        
        draw_label1=Label(Draw_screen)
        draw_img5 = PhotoImage(file="D:/rps/draw.png")
        draw_label1.config(image=draw_img5)
        draw_label1.pack()
        draw_label1.place(x=0,y=0)  
        
        Draw_screen.mainloop()
 #The end check of avg Joe include more thing than the endcheck of monkey, it decide who is the winner and display corresponding screen
    def end_check():
        global rnd,user_score,user_choice,bot_score,Num_of_Draw
        if rnd==5:
    
            if user_score> bot_score:
                time.sleep(3)
    
                Game_Screen.destroy()
                user_win_joe()
    
            elif user_score < bot_score :
                time.sleep(3)
                Game_Screen.destroy()
                bot_win_joe()
    
            elif user_score==bot_score:
                time.sleep(3)
                Game_Screen.destroy()
                draw_joe()        
    

        
    
            
    Game_Screen.mainloop()            



#The structure for the Brain gamemode is similar to Average Joe Gamemode, everything is the same expect the brain bot will learn from the user's guessing pattern and increase it probability of countering the user everytime it wins or loss
def Start_Game_Screen_brain():
    Game_Screen=Tk()    
    Game_Screen.title("gaming screen")
    Game_Screen.geometry("760x520")
            
    def close_window ():
            Game_Screen.destroy()
        

    
    global rnd,user_score,user_choice,bot_score,Num_of_Draw,choices
    
    Show_user_score=Label(Game_Screen,text="Your score : "+str(user_score), font = ('gothic',12))
    Show_user_score.place(x=420,y=450)
    
  
    Show_bot_score=Label(Game_Screen,text="Challenger's score : "+str(bot_score),font = ('gothic',12))
    Show_bot_score.place(x=20,y=450)    
    
    Show_Number_of_Draw=Label(Game_Screen,text="Draw counter : "+str(Num_of_Draw),font = ('gothic',12))
    Show_Number_of_Draw.place(x=220,y=450)     
     
    Showround=Label(Game_Screen,text="Round: "+str(rnd), font = ('gothic',12))       
    Showround.place(x=280,y=100)  
    

    
    def play_rock():
        global user_choice
        user_choice="r"
        run_brain()
        end_check_brain()
    def play_paper():
        global user_choice
        user_choice="p"
        run_brain()
        end_check_brain()
        
    def play_scissors():
        global user_choice
        user_choice="s" 
        run_brain()
        end_check_brain()

    
    overlay=Label(Game_Screen)
    overlay_img = PhotoImage(file="D:/rps/overlay_brain.png")
    overlay.config(image=overlay_img)
    overlay.pack()
    overlay.place(x=0,y=0)
    
    Exit=Button(Game_Screen,text="Exit game",bd=25,font = ('gothic',12), command = close_window)
    Exit.place(x=600,y=420)      
    
    rock=Button(Game_Screen,text="rock",bd=2,font=100, command= play_rock )
    rock_img = PhotoImage(file="D:/rps/rock.png")
    rock.config(image=rock_img)
    rock.pack()     
    rock.place(x=23,y=225)
         
        
    paper=Button(Game_Screen,text="paper",bd=2,font=100, command = play_paper)
    paper_img = PhotoImage(file="D:/rps/paper.png")
    paper.config(image=paper_img)
    paper.pack()     
    paper.place(x=220,y=205)
         
     
    scissors=Button(Game_Screen,text="scissors",bd=2,font=100, command = play_scissors)
    scissors_img = PhotoImage(file="D:/rps/scissors.png")
    scissors.config(image=scissors_img)
    scissors.pack()
    scissors.place(x=483,y=203)
        
    
    
    def run_brain():
        
        global rnd,user_score,user_choice,bot_score,Num_of_Draw,choices
        
        bot_choice = random.choice(choices)
            
        if user_choice == bot_choice :

            Show_result=Label(Game_Screen,text="Draw! You and the challenger picked the same choice!                                                                                                                                     ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
         
            Num_of_Draw=Num_of_Draw+1
            Show_Number_of_Draw=Label(Game_Screen,text="Draw counter:  "+str(Num_of_Draw),font = ('gothic',12))
            Show_Number_of_Draw.place(x=220,y=450)            
                
        elif user_choice == "r" and bot_choice == "s" :
            Show_result=Label(Game_Screen,text="You picked rock, Challenger picked scissor. Rock blunts scissors, You win this round!                ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
            user_score = user_score + 1
            Show_user_score=Label(Game_Screen,text="Your score:  "+str(user_score),font = ('gothic',12))
            Show_user_score.place(x=420,y=450)
            #The Key to brain bot's learning pattern is the append command here. The bot will adjust it choice list so that it will have the higher probability of countering the user if the user pick the same thing again and again,
            #For example everytime the bot lose to rock or win against rock, it would add a "p"-paper into it "choices" list, increasing the probability that the random generator will pick a "p" out of everything in the choices list  
            #from https://www.tutorialspoint.com/python/list_append.htm AND 
            #  https://www.w3schools.com/python/ref_list_append.asp
            choices.append("p")
        elif user_choice == "p" and bot_choice == "r" :
            Show_result=Label(Game_Screen,text="You picked paper, Challenger pioked rock. Paper covers rock, You won this round!                   ",font = ('gothic',12))
            Show_result.place(x=10,y=150)
            user_score = user_score + 1
            Show_user_score=Label(Game_Screen,text="Your score:  "+str(user_score),font = ('gothic',12))
            Show_user_score.place(x=420,y=450) 
            choices.append("s")
        elif user_choice== "s" and bot_choice == "p" :
            Show_result=Label(Game_Screen,text="You picked scissors, Challenger picked paper. Scissors cuts paper, You won this round!                        ",font = ('gothic',12))
            Show_result.place(x=10,y=150) 
            user_score = user_score + 1
            Show_user_score=Label(Game_Screen,text="Your score:  "+str(user_score),font = ('gothic',12))
            Show_user_score.place(x=420,y=450)
            choices.append("r")
        elif user_choice == "r" and bot_choice == "p" :
                Show_result=Label(Game_Screen,text="You picked rock, Challenger picked paper. Paper covers rock, Challenger won this round!                      ",font = ('gothic',12))
                Show_result.place(x=10,y=150)
                bot_score = bot_score + 1
                Show_bot_score=Label(Game_Screen,text="Challenger's score:  "+str(bot_score),font = ('gothic',12))
                Show_bot_score.place(x=20,y=450)
                choices.append("p")
        elif user_choice == "p" and bot_choice == "s" :
                Show_result=Label(Game_Screen,text="You picked paper, Challenger picked scissors. Scissors cuts paper, Challenger won this round!                   ",font = ('gothic',12))
                Show_result.place(x=10,y=150)
                bot_score = bot_score + 1
                Show_bot_score=Label(Game_Screen,text="Challenger's score:  "+str(bot_score),font = ('gothic',12))
                Show_bot_score.place(x=20,y=450)  
                choices.append("s")
        elif user_choice == "s" and bot_choice == "r"  :
                Show_result=Label(Game_Screen,text="You picked scissors, Challenger picked rock. Rock blunts scissors, Challenger won this round!           ",font = ('gothic',12))
                Show_result.place(x=10,y=150)
                bot_score = bot_score + 1
                Show_bot_score=Label(Game_Screen,text="Challenger's score:  "+str(bot_score),font = ('gothic',12))
                Show_bot_score.place(x=20,y=450)
                choices.append("r")
                
        
        rnd=rnd+1
        Showround=Label(Game_Screen,text="Round: "+str(rnd), font = ('gothic',12))
        Showround.place(x=280,y=100)         
                
        
        
        return rnd,user_score,user_choice,bot_score,Num_of_Draw
 
 
    def end_check_brain():
        global rnd,user_score,user_choice,bot_score,Num_of_Draw
        if rnd==5:
    
            if user_score> bot_score:
                time.sleep(3)
    
                Game_Screen.destroy()
                user_win_brain()
    
            elif user_score < bot_score :
                time.sleep(3)
                Game_Screen.destroy()
                bot_win_brain()
    
            elif user_score==bot_score:
                time.sleep(3)
                Game_Screen.destroy()
                draw_brain()
        
    
            
               

 


    def user_win_brain():
        
        Winner_Screen=Tk() 
        Winner_Screen.title("You are the winner!")
        Winner_Screen.geometry("519x149")    
        
        win=Label(Winner_Screen)
        win_img = PhotoImage(file="D:/rps/winner.png")
        win.config(image=win_img)
        win.pack()
        win.place(x=0,y=0)   
        
        Winner_Screen.mainloop()
    
    
    
    
    def bot_win_brain():
        
        Loser_screen=Tk()
        Loser_screen.title("You lost!")
        Loser_screen.geometry("424x129")
        
        loser=Label(Loser_screen)
        loser_img = PhotoImage(file="D:/rps/loser.png")
        loser.config(image=loser_img)
        loser.pack()
        loser.place(x=0,y=0) 
        
        Loser_screen.mainloop()
        
    def draw_brain():
        
        Draw_screen=Tk()
        Draw_screen.title("Draw!")
        Draw_screen.geometry("414x146")
        
        draw_label=Label(Draw_screen)
        draw_img3 = PhotoImage(file="D:/rps/draw.png")
        draw_label.config(image=draw_img3)
        draw_label.pack()
        draw_label.place(x=0,y=0)  
        
        Draw_screen.mainloop()
     
    def end_check_brain():
        global rnd,user_score,user_choice,bot_score,Num_of_Draw
        if rnd==5:
            
            if user_score > bot_score:
                time.sleep(3)
                Game_Screen.destroy()
                user_win_brain()
                
            elif user_score < bot_score :
                time.sleep(3)
                Game_Screen.destroy()
                bot_win_brain()
    
            elif user_score==bot_score:
                time.sleep(3)
                Game_Screen.destroy()
                draw_brain()    
    
    Game_Screen.mainloop() 
    
    
    
    

    
     
         
    
    
                    
 
#GLOBAL VARIABLES and the starting code of the game
# from: https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
user_score = 0
bot_score = 0
Num_of_Draw=0
rnd = 0
user_choice="0"
choices = ["r","p","s"]
Start_Starting_Screen()
