from tkinter import Tk, Label, Button
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def basemap():
	#Actual Map, Projects Values that square  around western US
	m=Basemap(projection='mill',llcrnrlat=31,urcrnrlat=43,\
				llcrnrlon=-130,urcrnrlon=-109,resolution='l')


	#Coast lines			
	m.drawcoastlines()
	#continent filled with light beige using hexidecimal, lake is cyan, layered below county lines
	m.fillcontinents(color='#ffffb3',lake_color='c',zorder=0)
	m.drawcounties(linewidth=2,color='r',zorder=1)
	m.drawstates(color='k')
	#Establishes Outer Border of states for better Asthetic Look
	m.drawmapboundary(fill_color='aqua')
	#Shade relif gives better proccessing and asthetics
	m.shadedrelief()
	plt.title('California Presidential Candidate Support')

	#900xx Area Code 
	NineHundredlat, NineHundredlon= 34.05, -118.25
	xpt, ypt = m (NineHundredlon, NineHundredlat)
	NineHundredlonpt, NineHundredlat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20)
	#902xx Area Code
	NineHundredTwolat, NineHundredTwolon= 33.99, -118.1
	xpt, ypt = m (NineHundredTwolon, NineHundredTwolat)
	NineHundredTwolonpt, NineHundredTwolat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20)
	plt.show()

def zip900():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\900xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip902():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\900xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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

def zip931():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\931xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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

def zip932():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\932xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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

def zip934():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\934xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip935():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\935xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip936():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\936xx,937xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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

def zip940():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\940xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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

def zip946():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\946xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip941():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\941xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip943():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\943xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip944():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\944xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip945():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\945xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip947():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\947xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip949():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\949xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip951():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\951xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip953():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\953xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip954():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\954xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip955():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\955xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip956():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\956xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip957():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\957xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip958():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\958xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip959():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\959xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip960():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\960xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
	
def zip961():
	#Declaring lists for different amounts
	party_list = []
	donation_list = []
	rep_list = []
	dem_list = []


		

	#Reading CSV file
	with open(r'C:\Users\Nolan\ProjectGit\Project2\961xx.csv', 'r') as testing:
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
		#assigning dem and rep donations in separate lists
	for x in range(0, list_length):
		if party_list[x] == 'Clinton, Hillary Rodham':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'O\'Malley, Martin Joseph':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Sanders, Bernard':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Webb, James Henry Jr.':
			dem_list.append(donation_list[x])
		elif party_list[x] == 'Carson, Benjamin S.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Rubio, Marco':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Trump, Donald J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Walker, Scott':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Paul, Rand':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Perry, James R. (Rick)':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Graham, Lindsey O.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Fiorina, Carly':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Cruz, Rafael Edward \'Ted\'':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Bush, Jeb':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Kasich, John R.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Huckabee, Mike':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Pataki, George E.':
			rep_list.append(donation_list[x])  
		elif party_list[x] == 'Jindal, Bobby':
			rep_list.append(donation_list[x]) 
		elif party_list[x] == 'Santorum, Richard J.':
			rep_list.append(donation_list[x])
		elif party_list[x] == 'Christie, Christopher J.':
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
		#master.title("California Presidential Candidate Contribution")
			
		#self.label = Label(master, text="Select a corresponding zip code")
		#self.label.grid(row=2, column=0)\
		
		self.basemap = Button(master, text="Open Map",command=basemap)
		self.basemap.grid(row=2, column=1)
		
		self.zip900 = Button(master, text="900xx",command=zip900)
		self.zip900.grid(row=3, column=1)

		self.zip902 = Button(master, text="902xx", command=zip902)
		self.zip902.grid(row=3, column=2)
		
		self.zip931 = Button(master, text="931xx", command=zip931)
		self.zip931.grid(row=4, column=1)
		
		self.zip932 = Button(master, text="932xx", command=zip932)
		self.zip932.grid(row=4, column=2)
		
		self.zip934 = Button(master, text="934xx", command=zip934)
		self.zip934.grid(row=5, column=1)
		
		self.zip935 = Button(master, text="935xx", command=zip935)
		self.zip935.grid(row=5, column=2)
		
		self.zip936 = Button(master, text="936xx", command=zip936)
		self.zip936.grid(row=6, column=1)
		
		self.zip940 = Button(master, text="940xx", command=zip940)
		self.zip940.grid(row=6, column=2)
		
		self.zip941 = Button(master, text="941xx", command=zip941)
		self.zip941.grid(row=7, column=1)
		
		self.zip943 = Button(master, text="943xx", command=zip943)
		self.zip943.grid(row=7, column=2)
		
		self.zip944 = Button(master, text="944xx", command=zip944)
		self.zip944.grid(row=8, column=1)
		
		self.zip945 = Button(master, text="945xx", command=zip945)
		self.zip945.grid(row=8, column=2)
		
		self.zip946 = Button(master, text="946xx", command=zip946)
		self.zip946.grid(row=9, column=1)
		
		self.zip947 = Button(master, text="947xx", command=zip947)
		self.zip947.grid(row=9, column=2)
		
		self.zip949 = Button(master, text="949xx", command=zip949)
		self.zip949.grid(row=10, column=1)
		
		self.zip951 = Button(master, text="951xx", command=zip951)
		self.zip951.grid(row=10, column=2)
		
		self.zip953 = Button(master, text="953xx", command=zip953)
		self.zip953.grid(row=11, column=1)
		
		self.zip954 = Button(master, text="954xx", command=zip954)
		self.zip954.grid(row=11, column=2)
		
		self.zip955 = Button(master, text="955xx", command=zip955)
		self.zip955.grid(row=12, column=1)
		
		self.zip956 = Button(master, text="956xx", command=zip956)
		self.zip956.grid(row=12, column=2)
		
		self.zip957 = Button(master, text="957xx", command=zip957)
		self.zip957.grid(row=13, column=1)
		
		self.zip958 = Button(master, text="958xx", command=zip958)
		self.zip958.grid(row=13, column=2)
		
		self.zip959 = Button(master, text="959xx", command=zip959)
		self.zip959.grid(row=14, column=1)
		
		self.zip960 = Button(master, text="960xx", command=zip960)
		self.zip960.grid(row=14, column=2)
		
		self.zip961 = Button(master, text="961xx", command=zip961)
		self.zip961.grid(row=15, column=1)
		


root = Tk()

my_gui = California(root)
root.mainloop()


