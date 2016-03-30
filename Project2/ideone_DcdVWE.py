#import csv
import matplotlib.pyplot as plt

#Declaring lists for different amounts
party_list = []
donation_list = []
rep_list = []
dem_list = []


	

#Reading CSV file
with open(r'C:\Users\Nolan\ProjectGit\Project2\902xx.csv', 'rb') as testing:
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
print(rep_list )       

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
