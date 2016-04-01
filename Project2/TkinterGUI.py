from tkinter import Tk, Label, Button
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
#Contains the filters for each plot as well as the basemap, functions are used as callbacks for the buttons
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
	# All of these Area Codes contain their coordinate locations, they are renamed to xpt, ypt, and then corresponded to a lable and marker
	#900xx Area Code 
	zip900lat, zip900lon= 34.05, -118.25
	xpt, ypt = m (zip900lon, zip900lat)
	zip900lonpt, zip900lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='900xx')
	#902xx Area Code
	zip902lat, zip902lon= 33.99, -118.1
	xpt, ypt = m (zip902lon, zip902lat)
	zip902lonpt, zip902lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='902xx')
	#931
	zip931lat, zip931lon= 34.49, -119.7
	xpt, ypt = m (zip931lon, zip931lat)
	zip931lonpt, zip931lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='931xx')
	#932xx
	zip932lat, zip932lon= 35.66, -118.1
	xpt, ypt = m (zip932lon, zip932lat)
	zip932lonpt, zip932lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='932xx')
	#934xx
	zip934lat, zip934lon= 34.99, -120.42
	xpt, ypt = m (zip934lon, zip934lat)
	zip934lonpt, zip934lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='934xx')
	#935xx
	zip935lat, zip935lon= 35.59, -117.6
	xpt, ypt = m (zip935lon, zip935lat)
	zip935lonpt, zip935lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='935xx')
	#936xx
	zip936lat, zip936lon= 36.78, -119.82
	xpt, ypt = m (zip936lon, zip936lat)
	zip9xxlonpt, zip936lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='936xx')
	#940xx
	zip940lat, zip940lon= 37.68, -122.4
	xpt, ypt = m (zip940lon, zip940lat)
	zip940lonpt, zip940lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='940xx')
	#941xx
	zip941lat, zip941lon= 37.68, -122.4
	xpt, ypt = m (zip941lon, zip941lat)
	zip941lonpt, zip941lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='941xx')
	#943xx
	zip943lat, zip943lon= 37.42, -122.16
	xpt, ypt = m (zip943lon, zip943lat)
	zip943lonpt, zip943lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='943xx')
	#944xx
	zip944lat, zip944lon= 37.57, -122.36
	xpt, ypt = m (zip944lon, zip944lat)
	zip944lonpt, zip944lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='944xx')
	#945xx
	zip945lat, zip945lon= 37.7, -122.2
	xpt, ypt = m (zip945lon, zip945lat)
	zip945lonpt, zip945lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20,label='945xx')
	#946xx
	zip946lat, zip946lon= 37.7, -122.2
	xpt, ypt = m (zip946lon, zip946lat)
	zip946lonpt, zip946lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='946xx')
	#947xx
	zip947lat, zip947lon= 37.86, -122.2
	xpt, ypt = m (zip947lon, zip947lat)
	zip947lonpt, zip947lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='947xx')
	#949xx
	zip949lat, zip949lon= 37.9, -122.51
	xpt, ypt = m (zip949lon, zip949lat)
	zip949lonpt, zip949lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='949xx')
	#951xx
	zip951lat, zip951lon= 37.34, -121.85
	xpt, ypt = m (zip951lon, zip951lat)
	zip951lonpt, zip951lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='951xx')
	#953xx
	zip953lat, zip953lon= 38.06, -120.39
	xpt, ypt = m (zip953lon, zip953lat)
	zip953lonpt, zip953lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='953xx')
	#954xx
	zip954lat, zip954lon= 39.21, -123.71
	xpt, ypt = m (zip954lon, zip954lat)
	zip954lonpt, zip954lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='954xx')
	#955xx
	zip955lat, zip955lon= 40.79, -124.16
	xpt, ypt = m (zip955lon, zip955lat)
	zip955lonpt, zip955lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='955x')
	#956xx
	zip956lat, zip956lon= 38.42, -120.82
	xpt, ypt = m (zip956lon, zip956lat)
	zip956lonpt, zip956lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='956xx')
	#957xx
	zip957lat, zip957lon= 39.21, -120.78
	xpt, ypt = m (zip957lon, zip957lat)
	zip957lonpt, zip957lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='957xx')
	#958xx
	zip958lat, zip958lon= 38.5, -121.49
	xpt, ypt = m (zip958lon, zip958lat)
	zip958lonpt, zip958lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='958xx')
	#959xx
	zip959lat, zip959lon= 39.42, -121.35
	xpt, ypt = m (zip959lon, zip959lat)
	zip959lonpt, zip959lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='959xx')
	#960xx
	zip960lat, zip960lon= 41.32, -122.81
	xpt, ypt = m (zip960lon, zip960lat)
	zip960lonpt, zip960lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='960xx')
	#961xx
	zip961lat, zip961lon= 40.29, -120.51
	xpt, ypt = m (zip961lon, zip961lat)
	zip961lonpt, zip961lat = m(xpt, ypt, inverse=True)
	m.plot(xpt, ypt, '*', markersize=20, label='961xx')
	
	#Legend Function with location and font sizing
	plt.legend(loc = 'best', numpoints=1, fontsize=8)
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
		master.title("California Presidential Candidate Contribution")
			
		#ALl of the Buttons spaced using the grid function, command calls defs to open plots
		self.basemap = Button(master, text="Open Map",command=basemap)
		self.basemap.grid(row=2, column=1, columnspan=2)
		
		self.zip900 = Button(master, text="900xx",command=zip900, bd=4, width = 16, height=1)
		self.zip900.grid(row=3, column=1)

		self.zip902 = Button(master, text="902xx", command=zip902,  bd=4, width = 16, height=1)
		self.zip902.grid(row=3, column=2)
		
		self.zip931 = Button(master, text="931xx", command=zip931,  bd=4, width = 16, height=1)
		self.zip931.grid(row=4, column=1)
		
		self.zip932 = Button(master, text="932xx", command=zip932,  bd=4, width = 16, height=1)
		self.zip932.grid(row=4, column=2)
		
		self.zip934 = Button(master, text="934xx", command=zip934,  bd=4, width = 16, height=1)
		self.zip934.grid(row=5, column=1)
		
		self.zip935 = Button(master, text="935xx", command=zip935,  bd=4, width = 16, height=1)
		self.zip935.grid(row=5, column=2)
		
		self.zip936 = Button(master, text="936xx", command=zip936,  bd=4, width = 16, height=1)
		self.zip936.grid(row=6, column=1)
		
		self.zip940 = Button(master, text="940xx", command=zip940,  bd=4, width = 16, height=1)
		self.zip940.grid(row=6, column=2)
		
		self.zip941 = Button(master, text="941xx", command=zip941,  bd=4, width = 16, height=1)
		self.zip941.grid(row=7, column=1)
		
		self.zip943 = Button(master, text="943xx", command=zip943,  bd=4, width = 16, height=1)
		self.zip943.grid(row=7, column=2)
		
		self.zip944 = Button(master, text="944xx", command=zip944,  bd=4, width = 16, height=1)
		self.zip944.grid(row=8, column=1)
		
		self.zip945 = Button(master, text="945xx", command=zip945,  bd=4, width = 16, height=1)
		self.zip945.grid(row=8, column=2)
		
		self.zip946 = Button(master, text="946xx", command=zip946,  bd=4, width = 16, height=1)
		self.zip946.grid(row=9, column=1)
		
		self.zip947 = Button(master, text="947xx", command=zip947,  bd=4, width = 16, height=1)
		self.zip947.grid(row=9, column=2)
		
		self.zip949 = Button(master, text="949xx", command=zip949,  bd=4, width = 16, height=1)
		self.zip949.grid(row=10, column=1)
		
		self.zip951 = Button(master, text="951xx", command=zip951,  bd=4, width = 16, height=1)
		self.zip951.grid(row=10, column=2)
		
		self.zip953 = Button(master, text="953xx", command=zip953,  bd=4, width = 16, height=1)
		self.zip953.grid(row=11, column=1)
		
		self.zip954 = Button(master, text="954xx", command=zip954,  bd=4, width = 16, height=1)
		self.zip954.grid(row=11, column=2)
		
		self.zip955 = Button(master, text="955xx", command=zip955,  bd=4, width = 16, height=1)
		self.zip955.grid(row=12, column=1)
		
		self.zip956 = Button(master, text="956xx", command=zip956,  bd=4, width = 16, height=1)
		self.zip956.grid(row=12, column=2)
		
		self.zip957 = Button(master, text="957xx", command=zip957,  bd=4, width = 16, height=1)
		self.zip957.grid(row=13, column=1)
		
		self.zip958 = Button(master, text="958xx", command=zip958,  bd=4, width = 16, height=1)
		self.zip958.grid(row=13, column=2)
		
		self.zip959 = Button(master, text="959xx", command=zip959,  bd=4, width = 16, height=1)
		self.zip959.grid(row=14, column=1)
		
		self.zip960 = Button(master, text="960xx", command=zip960,  bd=4, width = 16, height=1)
		self.zip960.grid(row=14, column=2)
		
		self.zip961 = Button(master, text="961xx", command=zip961,  bd=4, width = 16, height=1)
		self.zip961.grid(row=15, column=1)
		
		
		
		

#Displays the gui
root = Tk()
my_gui = California(root)
root.mainloop()


