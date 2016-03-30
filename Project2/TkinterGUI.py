from tkinter import Tk, Label, Button
import os
#import ideone_DcdVWE


def attempt():
	ideone_DcdVWE.drawpiechart()
	#os.startfile(r'C:\Users\Nolan\ProjectGit\Project2\ideone_DcdVWE.py')


class California:
    def __init__(self, master):
		
		
        self.master = master
        master.title("California Presidential Candidate Contribution")
		

        self.label = Label(master, text="Select a corresponding zip code")
        self.label.pack()

        self.zip900 = Button(master, text="900xx", command=attempt, bd=4, height=2, width = 400, font=10)
        self.zip900.pack()

        self.zip902 = Button(master, text="902xx", command=attempt, bd=4, height=2, width= 400, font=10)
        self.zip902.pack()
		
		
		

    

root = Tk()
root.geometry("250x500")
my_gui = California(root)
root.mainloop()
