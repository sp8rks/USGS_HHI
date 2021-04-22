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

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42
plt.rcParams.update({'font.size' : 14})

import seaborn as sns


#path = r'data/'
filename = r'Normalized_Prices.xlsx'
df = pd.read_excel(filename, skiprows=[1])
#x = df['Year']
element = df['Element']
price1998 = df['1998 Dollars']
element_list=['PTG','Pt','He','Be','Nb','Sb','W','Al','N','K','S','Ti','Mn','Fe','Ni','Cu'
              ,'Zn','Ag','Cd','Au','V','Cr','Se','Br','Zr','Mo','Pd','Sn','Ba','Re','I','P'
              ,'Pb','Li','Bi','Ca','Hg','Co','B','Ga','As','Sr','Te','Ta','Th','Y', 'Yb', 'Sc'
              ,'Tm', 'Tb', 'Sm', 'Pr', 'Lu', 'Nd', 'La', 'Ho', 'Gd', 'Eu', 'Er', 'Dy', 'Ce']

df=df.set_index("Element")
     


Df_dictionary = {}
for elem in element_list:
    df_elem = df[df.index == elem]
    Df_dictionary[elem] = df_elem



#plot1
fig = plt.figure(1, figsize=[10,6])
gs = gridspec.GridSpec(4,6)
gs.update(wspace=0.7, hspace=.25)

#categories
#1: REEs  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#when defining subplot remember it's rows,columns format instead of x,y
xtr_subsplot = fig.add_subplot(gs[0:2,0:2])
color_high = sns.cubehelix_palette(16, start=2)
plt.semilogy(Df_dictionary["Y"]["Year"],Df_dictionary["Y"]["1998 Dollars"], label='Y 99.99%',linestyle='-', marker='None', color=color_high[0], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Yb"]["Year"],Df_dictionary["Yb"]["1998 Dollars"], label='Yb 99%',linestyle='-', marker='None', color=color_high[1], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Sc"]["Year"],Df_dictionary["Sc"]["1998 Dollars"], label='Sc 99.99%',linestyle='-', marker='None', color=color_high[2], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Tm"]["Year"],Df_dictionary["Tm"]["1998 Dollars"], label='Tm 99.9%',linestyle='-', marker='None', color=color_high[3], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Tb"]["Year"],Df_dictionary["Tb"]["1998 Dollars"], label='Tb 99.9%',linestyle='-', marker='None', color=color_high[4], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Sm"]["Year"],Df_dictionary["Sm"]["1998 Dollars"], label='Sm 96-99.9%',linestyle='-', marker='None', color=color_high[5], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Pr"]["Year"],Df_dictionary["Pr"]["1998 Dollars"], label='Pr 96%',linestyle='-', marker='None', color=color_high[6], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Lu"]["Year"],Df_dictionary["Lu"]["1998 Dollars"], label='Lu 99.99%',linestyle='-', marker='None', color=color_high[7], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Nd"]["Year"],Df_dictionary["Nd"]["1998 Dollars"], label='Nd 95%',linestyle='-', marker='None', color=color_high[8], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["La"]["Year"],Df_dictionary["La"]["1998 Dollars"], label='La 99.99%',linestyle='-', marker='None', color=color_high[9], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ho"]["Year"],Df_dictionary["Ho"]["1998 Dollars"], label='Ho 99.9%',linestyle='-', marker='None', color=color_high[10], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Gd"]["Year"],Df_dictionary["Gd"]["1998 Dollars"], label='Gd 99.99%',linestyle='-', marker='None', color=color_high[11], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Eu"]["Year"],Df_dictionary["Eu"]["1998 Dollars"], label='Eu 99.99%',linestyle='-', marker='None', color=color_high[12], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Er"]["Year"],Df_dictionary["Er"]["1998 Dollars"], label='Er 96%',linestyle='-', marker='None', color=color_high[13], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Dy"]["Year"],Df_dictionary["Dy"]["1998 Dollars"], label='Dy 99%',linestyle='-', marker='None', color=color_high[14], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ce"]["Year"],Df_dictionary["Ce"]["1998 Dollars"], label='Ce 99.5%',linestyle='-', marker='None', color=color_high[15], markerfacecolor='none', markersize=10)

#plt.legend(bbox_to_anchor=(1.19, 1.015), fontsize=9)


plt.xlim([1996,2016])
plt.ylim([0.001,100000])


#
plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=False, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1996,2016,8)
#yticks = np.arange(6e5,1e6,1e5)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
#plt.yticks(yticks)
#plt.ylabel('price (1998 Dollars)')  # label the y axis
plt.text(1987,10e-8,'price (1998 Dollars)',rotation=90)  # label the y axis

#
##plot 2
xtr_subsplot = fig.add_subplot(gs[0:2,2:4])
color_low = sns.cubehelix_palette(4, start=1)
#2 >1000  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.semilogy(Df_dictionary["Au"]["Year"],Df_dictionary["Au"]["1998 Dollars"], label='Au',linestyle='-', marker='None', color=color_low[0], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Pt"]["Year"],Df_dictionary["Pt"]["1998 Dollars"], label='Pt',linestyle='-', marker='None', color=color_low[1], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Pd"]["Year"],Df_dictionary["Pd"]["1998 Dollars"], label='Pd',linestyle='-', marker='None', color=color_low[2], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Re"]["Year"],Df_dictionary["Re"]["1998 Dollars"], label='Re',linestyle='-', marker='None', color=color_low[3], markerfacecolor='none', markersize=10)


plt.xlim([1996,2016])
plt.ylim([4000,100000])
plt.ylim([0.001,100000])


plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=False, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1996,2016,8)
#yticks = np.arange(5000,50001,10000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
#plt.yticks(yticks)
#
#
##plot 3
xtr_subsplot = fig.add_subplot(gs[0:2,4:6])
color_med = sns.cubehelix_palette(16, start=0)

#3  10-1000 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.semilogy(Df_dictionary["Ga"]["Year"],Df_dictionary["Ga"]["1998 Dollars"], label='Ga 99.99999%',linestyle='-', marker='None', color=color_med[0], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ag"]["Year"],Df_dictionary["Ag"]["1998 Dollars"], label='Ag ingot',linestyle='-', marker='None', color=color_med[1], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Be"]["Year"],Df_dictionary["Be"]["1998 Dollars"], label='BeO',linestyle='-', marker='None', color=color_med[2], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["V"]["Year"],Df_dictionary["V"]["1998 Dollars"], label='V2O5',linestyle='-', marker='None', color=color_med[3], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Co"]["Year"],Df_dictionary["Co"]["1998 Dollars"], label='Co US spot cathode',linestyle='-', marker='None', color=color_med[4], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ni"]["Year"],Df_dictionary["Ni"]["1998 Dollars"], label='Pure Ni',linestyle='-', marker='None', color=color_med[5], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Nb"]["Year"],Df_dictionary["Nb"]["1998 Dollars"], label='Ferroniobium',linestyle='-', marker='None', color=color_med[6], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Mo"]["Year"],Df_dictionary["Mo"]["1998 Dollars"], label='Mo',linestyle='-', marker='None', color=color_med[7], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Sn"]["Year"],Df_dictionary["Sn"]["1998 Dollars"], label='Sn',linestyle='-', marker='None', color=color_med[8], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Te"]["Year"],Df_dictionary["Te"]["1998 Dollars"], label='Te',linestyle='-', marker='None', color=color_med[9], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["I"]["Year"],Df_dictionary["I"]["1998 Dollars"], label='I',linestyle='-', marker='None', color=color_med[10], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ta"]["Year"],Df_dictionary["Ta"]["1998 Dollars"], label='Ta ore',linestyle='-', marker='None', color=color_med[11], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["W"]["Year"],Df_dictionary["W"]["1998 Dollars"], label='Annonium paratungstate',linestyle='-', marker='None', color=color_med[12], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Hg"]["Year"],Df_dictionary["Hg"]["1998 Dollars"], label='Hg',linestyle='-', marker='None', color=color_med[13], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Bi"]["Year"],Df_dictionary["Bi"]["1998 Dollars"], label='Bi',linestyle='-', marker='None', color=color_med[14], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Th"]["Year"],Df_dictionary["Th"]["1998 Dollars"], label='ThO2',linestyle='-', marker='None', color=color_med[15], markerfacecolor='none', markersize=10)


plt.xlim([1996,2016])
plt.ylim([100,10000])
plt.ylim([0.001,100000])



plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1996,2016,8)
#yticks = np.arange(0,10001,2000)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
#plt.yticks(yticks)
#
#
#plot 4
xtr_subsplot = fig.add_subplot(gs[2:4,0:2])
color_rise = sns.cubehelix_palette(16, start=1.7)


#4 0.1-10  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.semilogy(Df_dictionary["Cr"]["Year"],Df_dictionary["Cr"]["1998 Dollars"], label='Chromite',linestyle='-', marker='None', color=color_rise[0], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Fe"]["Year"],Df_dictionary["Fe"]["1998 Dollars"], label='Fe ore',linestyle='-', marker='None', color=color_rise[1], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Se"]["Year"],Df_dictionary["Se"]["1998 Dollars"], label='Se',linestyle='-', marker='None', color=color_rise[2], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Li"]["Year"],Df_dictionary["Li"]["1998 Dollars"], label='Li2CO3',linestyle='-', marker='None', color=color_rise[3], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["B"]["Year"],Df_dictionary["B"]["1998 Dollars"], label='Chilean ulexite',linestyle='-', marker='None', color=color_rise[4], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["N"]["Year"],Df_dictionary["N"]["1998 Dollars"], label='Anhydrous Ammonia',linestyle='-', marker='None', color=color_rise[5], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Al"]["Year"],Df_dictionary["Al"]["1998 Dollars"], label='Al',linestyle='-', marker='None', color=color_rise[6], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["K"]["Year"],Df_dictionary["K"]["1998 Dollars"], label='Muriate',linestyle='-', marker='None', color=color_rise[7], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Mn"]["Year"],Df_dictionary["Mn"]["1998 Dollars"], label='Mn ore',linestyle='-', marker='None', color=color_rise[8], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Cu"]["Year"],Df_dictionary["Cu"]["1998 Dollars"], label='Cu',linestyle='-', marker='None', color=color_rise[9], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Zn"]["Year"],Df_dictionary["Zn"]["1998 Dollars"], label='Zn',linestyle='-', marker='None', color=color_rise[10], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["As"]["Year"],Df_dictionary["As"]["1998 Dollars"], label='As2O3',linestyle='-', marker='None', color=color_rise[11], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Zr"]["Year"],Df_dictionary["Zr"]["1998 Dollars"], label='Zr',linestyle='-', marker='None', color=color_rise[12], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Cd"]["Year"],Df_dictionary["Cd"]["1998 Dollars"], label='Cd 99.95%',linestyle='-', marker='None', color=color_rise[13], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Sb"]["Year"],Df_dictionary["Sb"]["1998 Dollars"], label='Sb',linestyle='-', marker='None', color=color_rise[14], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Pb"]["Year"],Df_dictionary["Pb"]["1998 Dollars"], label='Pb',linestyle='-', marker='None', color=color_rise[15], markerfacecolor='none', markersize=10)


plt.xlim([1996,2016])
plt.ylim([1,1000])
plt.ylim([0.001,100000])



plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1996,2016,8)
#yticks = np.arange(0,401,100)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
#plt.yticks(yticks)

#
##plot 5
xtr_subsplot = fig.add_subplot(gs[2:4,2:4])
color_spike = sns.cubehelix_palette(5, start=0.6)

#5 <0.1  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.semilogy(Df_dictionary["Ca"]["Year"],Df_dictionary["Ca"]["1998 Dollars"], label='Crushed stone',linestyle='-', marker='None', color=color_spike[0], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["P"]["Year"],Df_dictionary["P"]["1998 Dollars"], label='Phosphate rock',linestyle='-', marker='None', color=color_spike[1], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["S"]["Year"],Df_dictionary["S"]["1998 Dollars"], label='S',linestyle='-', marker='None', color=color_spike[2], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ti"]["Year"],Df_dictionary["Ti"]["1998 Dollars"], label='Ilmenite',linestyle='-', marker='None', color=color_spike[3], markerfacecolor='none', markersize=10)
plt.semilogy(Df_dictionary["Ba"]["Year"],Df_dictionary["Ba"]["1998 Dollars"], label='Barite',linestyle='-', marker='None', color=color_spike[4], markerfacecolor='none', markersize=10)



plt.xlim([1996,2016])
plt.ylim([0.1,100])
plt.ylim([0.001,100000])



plt.xlabel('year')  # label the x axis

plt.tick_params(direction='in',right=True, top=True, left=True, bottom=True)
plt.tick_params(labelbottom=True, labeltop=False, labelright=False, labelleft=True)    
xticks = np.arange(1996,2016,8)
#yticks = np.arange(0,61,20)
plt.minorticks_on()
plt.tick_params(direction='in',which='minor', length=5, bottom=True, top=True, left=True, right=True)
plt.tick_params(direction='in',which='major', length=10, bottom=True, top=True, left=True, right=True)
plt.xticks(xticks)
#plt.yticks(yticks)

#
#plt.savefig('price.pdf', dpi=300,bbox_inches="tight")
plt.savefig('price.png', dpi=300,bbox_inches="tight")