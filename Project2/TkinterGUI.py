from tkinter import Tk, Label, Button
import csv
import matplotlib.pyplot as plt

def attempt():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\902xx.csv', 'r') as testing:
		reader = csv.reader(testing)
		for row in reader:
			party_list.append(row[0])
			donation_list.append(row[6])
			
	#Removing the first line "Contribution Amount"        
	party_list.remove('cand_nm')
	donation_list.remove('contb_receipt_amt')   

	list_length = len(donation_list)
	print(list_length)

	#assigning dem and rep donations in seprate lists
	for x in range(0, list_length):
		if party_list[x] == 'Democrat':
			dem_list.append(donation_list[x])
		else:
			rep_list.append(donation_list[x])

			
	print(dem_list)
	print(rep_list)       

	#converting string elements into ints
	dem_list = map(float, dem_list)
	rep_list = map(float, rep_list)

	#finding the sum of all the elements in a list
	dem_amount = sum(dem_list)
	rep_amount = sum(rep_list)


	values=[dem_amount, rep_amount]

	def make_autopct(values):
		def my_autopct(pct):
			total = sum(values)
			val = int(round(pct*total/100.0))
			return '{p:.2f}%  (${v:d}.00)'.format(p=pct,v=val)
		return my_autopct



	print(dem_amount)
	print(rep_amount)

	#Setting up the lists necessary for a pie chart
	parties_list = ['Democrat', 'Republican']
	money_list = [dem_amount, rep_amount]
	cols = ['b', 'r']

	#placing parameters to create pie chart
	plt.pie(money_list, 
			labels = parties_list, 
			colors = cols, 
			shadow = False, 
			startangle = 90,
			autopct = make_autopct(values)
		
			)
	plt.title('Testing Party Donations')
	plt.show()



class California:
    def __init__(self, master):
		
		
        self.master = master
        master.title("California Presidential Candidate Contribution")
		

        self.label = Label(master, text="Select a corresponding zip code")
        self.label.pack()

        self.zip900 = Button(master, text="900xx",command=attempt, bd=4, height=2, width = 400, font=10)
        self.zip900.pack()

        self.zip902 = Button(master, text="902xx", bd=4, height=2, width= 400, font=10)
        self.zip902.pack()
		
		
		

    

root = Tk()
root.geometry("500x500")
my_gui = California(root)
root.mainloop()
