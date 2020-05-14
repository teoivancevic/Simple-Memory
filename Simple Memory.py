import tkinter as tk
from tkinter import messagebox
import random
import time
import threading



class MainWindow:
    

    
    playerName = ""
    difficulty = 0

    pairList = [1,1,2,2,3,3,4,4,5,5,0]
    btnName = [["","","","",""], ["","","","",""]]
    isSecond = False
    
    Curri = None
    Currj = None
    Lasti = None
    Lastj = None

    isPressed = [[False,False,False,False,False], [False,False,False,False,False]]

    defLabel = "Gumb"
    correctPairs = 0
    setDiff = 0
    moves = 0

    
    def __init__(self, master):
        self.master = master
        self.master.geometry('510x120')
        self.master.resizable(False, False)

        #self.timer = Timer(2.0, self.ResetGumb)

        #self.txtFrame = tk.Frame(width = 200, height = 100)
        #self.btnFrame = tk.Frame(width = 200, height = 100)
        #frame = tk.Frame(width = 1000, height = 700)
        #frame.pack()

        #self.grid = np.diag(np.ones(3))
        #self.buttons = [[tk.Button()]*7]*7
        self.buttons = [[None for _ in range(7)] for _ in range(7)]
        
        self.nameLabel = tk.Label(text = "Player name: ", width = 20)
        self.scaleLabel = tk.Label(text = "Difficulty: ", width = 20)
        
        self.nameBox = tk.Entry(self.master, width = 20)
        self.scale = tk.Scale(self.master, width = 20, from_=2, to = 5, orient = "horizontal")

        self.playGameBtn = tk.Button(self.master, width = 20, height = 2, text = "Play game", command = self.playGame)

        
        self.nameLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        self.nameBox.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "nsw")

        self.scaleLabel.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        self.scale.grid(row = 1, column = 1, padx = 10, pady = 10)
        ##self.submitNameBtn.grid(row = 0, column = 1, padx = 10, pady = 10)
        
        self.playGameBtn.grid(row = 0, column = 2, rowspan = 2, padx = 10, pady = 10)
        

    def playGame(self):
        self.playerName = self.nameBox.get()
        if(self.playerName == ""):
            self.playerName = "Player"
        
        difficulty = self.scale.get()
        self.setDiff = difficulty
        #messagebox.showinfo("", playerName + str(difficulty))
        self.nameBox.destroy()
        self.scale.destroy()
        self.playGameBtn.destroy()
        
        self.nameLabel["text"] += self.playerName
        self.scaleLabel["text"] += str(difficulty)
        #self.name = tk.Label(text = playerName, width = 20)
        #self.name.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "nsw")
        
        #self.diff = tk.Label(text = difficulty, width = 20)
        #self.diff.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = "nsw")

        self.fillNames(difficulty)  

        for i in range(2):
            for j in range(difficulty):
                
                self.buttons[i][j] = tk.Button(text = self.defLabel, width = 10, 
                        command = lambda i=i, j=j: self.btnPress(self.buttons[i][j], i, j))
                self.buttons[i][j].grid(row = i, column = j+1)
        
        geo = "" + str(170 + difficulty*80 + 15) + "x" + "90" 
        self.master.geometry(geo)

    '''
    def resetBtns(self, button):
        button["text"] = self.defLabel
        self.buttons[self.Lasti][self.Lastj]["text"] = self.defLabel
    '''
    
    def btnPress(self, button, i, j):
        if(not self.isPressed[i][j]):
            self.isPressed[i][j] = True

            button["text"] =  self.btnName[i][j]
        
            self.changeText(button, i, j)
            #time.sleep(1)
            #button.after(1000, self.changeText(button, i, j))
            #self.master.after(1000, self.changeText(button, i, j))
        else:
    	    pass

        
        
    

    def changeText(self, button, i, j):
        #button["text"] = self.btnName[i][j]
        if(self.isSecond):
            #button["text"] = self.btnName[i][j]
            if(button["text"] != self.buttons[self.Lasti][self.Lastj]["text"]):
                #time.sleep(0)
                #self.timer.start()
                self.Curri = i
                self.Currj = j
                threading.Timer(1.5, self.ResetGumb).start()

                self.isPressed[self.Curri][self.Currj] = False
                self.isPressed[self.Lasti][self.Lastj] = False
                #self.buttons[self.Lasti][self.Lastj]["text"] = self.defLabel
                pass
            else:
                self.correctPairs += 1

            self.isSecond = False
            self.moves += 1
            
            #self.timer._stop
            

            self.checkGameEnd()
            
        else:
            #self.timer.cancel()
            
            self.c = True
            #button["text"] = self.btnName[i][j]
            self.isSecond = True
            self.Lasti = i
            self.Lastj = j

    def ResetGumb(self):
        #messagebox.showinfo('Tu sam','poruka')
        self.buttons[self.Lasti][self.Lastj]["text"] = self.defLabel
        self.buttons[self.Curri][self.Currj]["text"] = self.defLabel

    def fillNames(self, maxPair):
        for i in range(2):
            for j in range(maxPair):
                searching = True
                while(searching):
                    random.seed(a=None, version=2)
                    a = random.randint(0, maxPair*2)
                    if(self.pairList[a] != 0 and a < maxPair*2):
                        label = str(self.pairList[a])
                        self.btnName[i][j] = label
                        #self.scaleLabel["text"] += str(a)
                        
                        self.pairList[a] = 0
                        searching = False

    def checkGameEnd(self):
        if(self.correctPairs == self.setDiff):
            messagebox.showinfo("Kraj igre!", "Bravo " + self.playerName + ", uspješno ste riješili memory na težini " + str(self.setDiff) + " u " + str(self.moves) + " poteza!")
            self.master.destroy()
        
        
        #self.buttons[self.Lasti][self.Lastj]["text"] = 'tra' # self.defLabel
        #time.sleep(1)


        #self.master.withdraw()



def main(): 
    root = tk.Tk()
    root.title("Simple Memory")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()