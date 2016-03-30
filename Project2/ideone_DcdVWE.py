import csv
import matplotlib.pyplot as plt

#Declaring lists for different amounts
party_list = []
donation_list = []
rep_list = []
dem_list = []


#Reading CSV file
with open('902xx.csv', 'rb') as testing:
    reader = csv.reader(testing)
    for row in reader:
        party_list.append(row[0])
        donation_list.append(row[6])
        
#Removing the first line "Contribution Amount"        
party_list.remove('cand_nm')
donation_list.remove('contb_receipt_amt')   

list_length = len(donation_list)
print list_length

#assigning dem and rep donations in separate lists
for x in range(0, list_length):
    if party_list[x] == 'Democrat':
        dem_list.append(donation_list[x])
    elif party_list[x] == 'Clinton, Hillary Rodham':
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
    elif party_list[x] == 'Republican':
        rep_list.append(donation_list[x])

        
print dem_list
print rep_list        

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



print dem_amount
print rep_amount

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
