from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
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
