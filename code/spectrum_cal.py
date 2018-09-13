#Open the files
import math
from numpy import array
import pyqtgraph as pg
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit

def gaus(x, a, b, c):
    return a * np.exp(-(x-b)**2/(2*c**2))
def lin(x, a, b):
    return a*x+b

#Load the data

am241 = []
ba133 = []
cs137 = []
co60 = []
eu152 = []
with open('/home/jake/Documents/lab0/lab0_spectral_data.txt', 'r') as f:
    content = f.readlines()[1:]
    for x in content:
        row = x.split()
        am241.append(int(row[0]))
        ba133.append(int(row[1]))
        cs137.append(int(row[2]))
        co60.append(int(row[3]))
        eu152.append(int(row[4]))

#Record known line energies
amline = [59.5]
baline = [80,276,302,356,383]
csline = [661.7]
coline = [1174,1332]
euline = [121]

#Turn lists into numpy arrays, append channel numbers
am_data = np.array(am241)
am_data = np.column_stack((am_data, np.linspace(1, 8192, num=8192),np.zeros(8192)))
ba_data = np.array(ba133)
ba_data = np.column_stack((ba_data, np.linspace(1, 8192, num=8192),np.zeros(8192)))
cs_data = np.array(cs137)
cs_data = np.column_stack((cs_data, np.linspace(1, 8192, num=8192),np.zeros(8192)))
co_data = np.array(co60)
co_data = np.column_stack((co_data, np.linspace(1, 8192, num=8192),np.zeros(8192)))
eu_data = np.array(eu152)
eu_data = np.column_stack((eu_data, np.linspace(1, 8192, num=8192),np.zeros(8192)))

#Use SciPy fit to fit gaussians to the peaks

#Start with Am
#plt.plot(am_data[200:220,1],am_data[200:220,0])

xdata = am_data[200:220,1]
ydata = am_data[200:220,0]

popt, pcov = curve_fit(gaus, xdata, ydata, bounds=(0, [50000., 220., 100.]))
xtest = np.linspace(200,215,num=100)

#plt.plot(xtest,gaus(xtest,popt[0],popt[1],popt[2]))
#plt.show()

am_pk_loc = popt[1]

#Switch to Cs
#plt.plot(cs_data[2340:2380,1],cs_data[2340:2380,0])


xdatacs = cs_data[2240:2380,1]
ydatacs = cs_data[2240:2380,0]

poptcs, pcovcs = curve_fit(gaus, xdatacs, ydatacs, bounds=(((1000,2300,0), (60000., 2400., 3))))
#plt.plot(xdatacs, gaus(xdatacs,poptcs[0],poptcs[1],poptcs[2]))
xtestcs = np.linspace(2340,2380, num=100)
cs_pk_loc = poptcs[1]
#plt.show()


#Perform 2-point calibration
chn = (popt[1],poptcs[1])
ene = (amline[0],csline[0])
fit = np.polyfit(chn,ene,1)
fit_fn = np.poly1d(fit)

#Apply to data
for n in range(0,8191):
    am_data[n,2] = fit_fn(am_data[n,1])
    cs_data[n,2] = fit_fn(cs_data[n,1])
    ba_data[n,2] = fit_fn(ba_data[n,1])
    co_data[n,2] = fit_fn(co_data[n,1])

#Plot
cs, = plt.semilogy(cs_data[0:3300,2],cs_data[0:3300,0], label='Cs-137')
am, = plt.semilogy(am_data[0:3300,2],am_data[0:3300,0], label='Am-241')
#am, = plt.plot(am_data[0:3300,2],am_data[0:3300,0], label='Am-241')
plt.legend(handles=[cs, am])
plt.xlabel('gamma ray energy, keV')
plt.ylabel('Counts per energy bin')
#plt.show()

plt.savefig('images/cs_ba.png')
plt.figure()
ba, = plt.semilogy(ba_data[0:3300,2],ba_data[0:3300,0], label='Ba-133', color = 'red')
plt.xlabel('gamma ray energy, keV')
plt.ylabel('Counts per energy bin')
plt.axvline(baline[0])
plt.axvline(baline[1])
plt.axvline(baline[2])
plt.axvline(baline[3])
plt.axvline(baline[4])
plt.savefig('images/Ba_data_check.png')


#mkdir folder in thing
