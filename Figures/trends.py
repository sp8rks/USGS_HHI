# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:21:25 2019

@author: tsparks
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 16:05:07 2018

@author: tsparks
"""

import pandas
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42
plt.rcParams.update({'font.size' : 14})

import seaborn as sns


#path = r'data/'
filename = r'hhi.csv'
df = pandas.read_csv(filename, skiprows=[1])
x = df['year']
#high
PTG = df['PTG']
Pt = df['Pt']
He = df['He']
Be = df['Be']
Nb = df['Nb']
Sb = df['Sb']
W = df['W']
REE = df['REE']
#low
Al = df['Al']
N = df['N']
K = df['K']
S = df['S']
Ti = df['Ti']
Mn = df['Mn']
Fe = df['Fe']
Ni = df['Ni']
Cu = df['Cu']
Zn = df['Zn']
Ag = df['Ag']
Cd = df['Cd']
Au = df['Au']
#moderate
V = df['V']
Cr = df['Cr']
Se = df['Se']
Br = df['Br']
Zr = df['Zr']
Mo = df['Mo']
Pd = df['Pd']
Sn = df['Sn']
Ba = df['Ba']
Re = df['Re']
I = df['I']
#slow rise
P = df['P']
Pb = df['Pb']
Li = df['Li']
#spike
Bi = df['Bi']
Ca = df['Ca']
Hg = df['Hg']
Co = df['Co']
B = df['B']
Ga = df['Ga']
#volatile
As = df['As']
Sr = df['Sr']
Te = df['Te']
Ta = df['Ta']
Th = df['Th']

#colors dark yellow to purple, https://meyerweb.com/eric/tools/color-blend/#660066:FFCC33:10:hex
color_high_1='#660066'
color_high_2='#741361'
color_high_3='#82255D'
color_high_4='#903858'
color_high_5='#9E4A53'
color_high_6='#AC5D4F'
color_high_7='#B96F4A'
color_high_8='#C78246'
color_high_9='#D59441'
color_high_10='#E3A73C'
color_high_11='#F1B938'
color_high_12='#FFCC33'



#colors blue to orange https://meyerweb.com/eric/tools/color-blend/#3F5CAA:F8991D:10:hex
color_low_1='#3F5CAA'
color_low_2='#50629D'
color_low_3='#616790'
color_low_4='#716D84'
color_low_5='#827277'
color_low_6='#93786A'
color_low_7='#A47D5D'
color_low_8='#B58350'
color_low_9='#C68843'
color_low_10='#D68E37'
color_low_11='#E7932A'
color_low_12='#F8991D'



#high plot
fig = plt.figure(1, figsize=(8, 6))
gs = gridspec.GridSpec(4,6)
gs.update(wspace=0.15, hspace=.15)
#plot the 2X3 grid 
#when defining subplot remember it's rows,columns format instead of x,y
xtr_subsplot = fig.add_subplot(gs[0:2,0:2])
color_high = sns.cubehelix_palette(8, start=2)
plt.plot(x, PTG, linestyle='-', marker='None', color=color_high[0], markerfacecolor='none', markersize=10)
plt.plot(x, Pt, linestyle='-', marker='None', color=color_high[1], markerfacecolor='none', markersize=10)
plt.plot(x, He, linestyle='-', marker='None', color=color_high[2], markerfacecolor='none', markersize=10)
plt.plot(x, Be, linestyle='-', marker='None', color=color_high[3], markerfacecolor='none', markersize=10)
plt.plot(x, Nb, linestyle='-', marker='None', color=color_high[4], markerfacecolor='none', markersize=10)
plt.plot(x, Sb, linestyle='-', marker='None', color=color_high[5], markerfacecolor='none', markersize=10)
plt.plot(x, W, linestyle='-', marker='None', color=color_high[6], markerfacecolor='none', markersize=10)
plt.plot(x, REE, linestyle='-', marker='None', color=color_high[7], markerfacecolor='none', markersize=10)
plt.xlim([1996,2016])
plt.ylim([0,10000])

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=False, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1998,2016,8)
yticks = np.arange(0,10001,5000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)
#plt.legend()
#plt.xlabel('year')  # label the x axis
#plt.ylabel('HHI (a.u.)')  # label the y axis
plt.text(1987,-1600,'HHI (a.u.)',rotation=90)  # label the y axis


#plot low
xtr_subsplot = fig.add_subplot(gs[0:2,4:6])
color_low = sns.cubehelix_palette(13, start=1)
plt.plot(x, Al, linestyle='-', marker='None', color=color_low[0], markerfacecolor='none', markersize=10)
plt.plot(x, N, linestyle='-', marker='None', color=color_low[1], markerfacecolor='none', markersize=10)
plt.plot(x, K, linestyle='-', marker='None', color=color_low[2], markerfacecolor='none', markersize=10)
plt.plot(x, S, linestyle='-', marker='None', color=color_low[3], markerfacecolor='none', markersize=10)
plt.plot(x, Ti, linestyle='-', marker='None', color=color_low[4], markerfacecolor='none', markersize=10)
plt.plot(x, Mn, linestyle='-', marker='None', color=color_low[5], markerfacecolor='none', markersize=10)
plt.plot(x, Fe, linestyle='-', marker='None', color=color_low[6], markerfacecolor='none', markersize=10)
plt.plot(x, Ni, linestyle='-', marker='None', color=color_low[7], markerfacecolor='none', markersize=10)
plt.plot(x, Cu, linestyle='-', marker='None', color=color_low[8], markerfacecolor='none', markersize=10)
plt.plot(x, Zn, linestyle='-', marker='None', color=color_low[9], markerfacecolor='none', markersize=10)
plt.plot(x, Ag, linestyle='-', marker='None', color=color_low[10], markerfacecolor='none', markersize=10)
plt.plot(x, Cd, linestyle='-', marker='None', color=color_low[11], markerfacecolor='none', markersize=10)
plt.plot(x, Au, linestyle='-', marker='None', color=color_low[12], markerfacecolor='none', markersize=10)

plt.xlim([1996,2016])
plt.ylim([0,10000])

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=False, labeltop=False, labelright=False, labelleft=False)    
xticks = np.arange(1998,2016,8)
yticks = np.arange(0,10001,5000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)
#plt.legend()
#plt.xlabel('year')  # label the x axis
#plt.ylabel('HHI (a.u.)')  # label the y axis
#plt.xlabel('year')  # label the x axis
#plt.ylabel('intensity (arbitrary units)')  # label the y axis


#plot moderate
xtr_subsplot = fig.add_subplot(gs[0:2,2:4])
color_med = sns.cubehelix_palette(11, start=0)
plt.plot(x, V, linestyle='-', marker='None', color=color_med[0], markerfacecolor='none', markersize=10)
plt.plot(x, Cr, linestyle='-', marker='None', color=color_med[1], markerfacecolor='none', markersize=10)
plt.plot(x, Se, linestyle='-', marker='None', color=color_med[2], markerfacecolor='none', markersize=10)
plt.plot(x, Br, linestyle='-', marker='None', color=color_med[3], markerfacecolor='none', markersize=10)
plt.plot(x, Zr, linestyle='-', marker='None', color=color_med[4], markerfacecolor='none', markersize=10)
plt.plot(x, Mo, linestyle='-', marker='None', color=color_med[5], markerfacecolor='none', markersize=10)
plt.plot(x, Pd, linestyle='-', marker='None', color=color_med[6], markerfacecolor='none', markersize=10)
plt.plot(x, Sn, linestyle='-', marker='None', color=color_med[7], markerfacecolor='none', markersize=10)
plt.plot(x, I, linestyle='-', marker='None', color=color_med[8], markerfacecolor='none', markersize=10)
plt.plot(x, Ba, linestyle='-', marker='None', color=color_med[9], markerfacecolor='none', markersize=10)
plt.plot(x, Re, linestyle='-', marker='None', color=color_med[10], markerfacecolor='none', markersize=10)

plt.xlim([1996,2016])
plt.ylim([0,10000])

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=False, labeltop=False, labelright=False, labelleft=False)    
xticks = np.arange(1998,2016,8)
yticks = np.arange(0,10001,5000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)
#plt.legend()
#plt.xlabel('year')  # label the x axis
#plt.ylabel('HHI (a.u.)')  # label the y axis
#plt.xlabel('year')  # label the x axis
#plt.ylabel('intensity (arbitrary units)')  # label the y axis


#plot slow rise
xtr_subsplot = fig.add_subplot(gs[2:4,0:2])
color_rise = sns.dark_palette("orange", input="xkcd")
plt.plot(x, P, linestyle='-', marker='None', color=color_rise[0], markerfacecolor='none', markersize=10)
plt.plot(x, Pb, linestyle='-', marker='None', color=color_rise[1], markerfacecolor='none', markersize=10)
plt.plot(x, Li, linestyle='-', marker='None', color=color_rise[2], markerfacecolor='none', markersize=10)

plt.xlim([1996,2016])
plt.ylim([0,10000])

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1998,2016,8)
yticks = np.arange(0,10001,5000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)
#plt.legend()
#plt.xlabel('year')  # label the x axis
#plt.ylabel('HHI (a.u.)')  # label the y axis
#plt.xlabel('year')  # label the x axis

#plot spike
xtr_subsplot = fig.add_subplot(gs[2:4,2:4])
color_spike = sns.dark_palette("muted purple", input="xkcd")
plt.plot(x, Bi, linestyle='-', marker='None', color=color_spike[0], markerfacecolor='none', markersize=10)
plt.plot(x, Ca, linestyle='-', marker='None', color=color_spike[1], markerfacecolor='none', markersize=10)
plt.plot(x, Hg, linestyle='-', marker='None', color=color_spike[2], markerfacecolor='none', markersize=10)
plt.plot(x, Co, linestyle='-', marker='None', color=color_spike[3], markerfacecolor='none', markersize=10)
plt.plot(x, B, linestyle='-', marker='None', color=color_spike[4], markerfacecolor='none', markersize=10)
plt.plot(x, Ga, linestyle='-', marker='None', color=color_spike[5], markerfacecolor='none', markersize=10)

plt.xlim([1996,2016])
plt.ylim([0,10000])
plt.xlabel('year')  # label the x axis

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)    
xticks = np.arange(1998,2016,8)
yticks = np.arange(0,10001,5000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)
#plt.legend()
#plt.xlabel('year')  # label the x axis
#plt.ylabel('HHI (a.u.)')  # label the y axis
#plt.ylabel('intensity (arbitrary units)')  # label the y axis

#plot volatile
xtr_subsplot = fig.add_subplot(gs[2:4,4:6])
color_volatile = sns.dark_palette((210, 90, 60), input="husl")
plt.plot(x, As, linestyle='-', marker='None', color=color_volatile[0], markerfacecolor='none', markersize=10)
plt.plot(x, Sr, linestyle='-', marker='None', color=color_volatile[1], markerfacecolor='none', markersize=10)
plt.plot(x, Ta, linestyle='-', marker='None', color=color_volatile[2], markerfacecolor='none', markersize=10)
plt.plot(x, Te, linestyle='-', marker='None', color=color_volatile[3], markerfacecolor='none', markersize=10)
plt.plot(x, Th, linestyle='-', marker='None', color=color_volatile[4], markerfacecolor='none', markersize=10)


plt.xlim([1996,2016])
plt.ylim([0,10000])

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=False)    
xticks = np.arange(1998,2016,8)
yticks = np.arange(0,10001,5000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
plt.yticks(yticks)
#plt.legend()
#plt.xlabel('year')  # label the x axis
#plt.ylabel('HHI (a.u.)')  # label the y axis
#plt.xlabel('year')  # label the x axis
#plt.ylabel('intensity (arbitrary units)')  # label the y axis





#plt.legend()  # add the legend (will default to 'best' location)


#plt.savefig('trends.pdf', dpi=300,bbox_inches="tight")
plt.savefig('trends.png', dpi=300,bbox_inches="tight")