# USGS_HHI
This repository contains HHI and price data by year and by country for elemental production worldwide taken from USGS mineral commodity yearbooks. 

This data was originally published in the article Brennan Theler, Steven K. Kauwe, and Taylor D. Sparks "Materials Abundance, Price, and Availability Data from the Years 1998 to 2015." _Integrating Materials & Manufacutring Innovation_ **9**, 144–150 (2020) found at https://doi.org/10.1007/s40192-020-00173-5.

The datasets include 18 .CSV fles named ‘#### Data.CSV’ where #### is a year ranging from 1998 to 2015. Each of these fles features 7 columns (‘Element’, ‘HHI Contribution’, ‘HHI’, ‘Country Production’, ‘Market Share’, ‘Total World Production’). The rows then show the seven columns of information for each element arranged alphabetically.

The dataset includes a ‘Notes by Element.CSV’ fle which includes 6 columns (‘Red=No Price data, Yellow= only partially included on price sheet, Green=on both sheets’, ‘Element’, ‘Notes’, ‘production’, ‘Are Production fgures unavailable?’, ‘Other’) with general notes and information taken from the USGS data such as the units for production, e.g., kg vs metric tons. 

The dataset includes a ‘Summary- HHI.CSV’ fle which contains 22 columns (‘Element’, ‘Unnamed: 1’, ‘HHI-1998’, ‘HHI-1999’, ‘HHI-2000’, ‘HHI-2001’, ‘HHI2002’, ‘HHI-2003’, ‘HHI-2004’, ‘HHI-2005’, ‘HHI-2006’, ‘HHI-2007’, ‘HHI-2008’, ‘HHI-2009’, ‘HHI-2010’, ‘HHI2011’, ‘HHI-2012’, ‘HHI-2013’, ‘HHI-2014’, ‘HHI-2015’) summarizing the HHI for each element for each year in the range provided. 

The dataset contains a ‘Summary-Market Share (%).CSV’ fle with 21 columns (‘Element’, ‘Notes’, ‘Country’, ‘1998’, ‘1999’, ‘2000’, ‘2001’, ‘2002’, ‘2003’, ‘2004’, ‘2005’, ‘2006’, ‘2007’, ‘2008’, ‘2009’, ‘2010’, ‘2011’, ‘2012’, ‘2013’, ‘2014’, ‘2015) which summarizes the market share by element on a per country basis for each year in the range provided. 

Finally, the data include a ‘prices.CSV’ fle with 10 columns (‘Element’, ‘Year’, ‘Dollars’, ‘Change in Absolute Dollars’, ‘Change in Absolute Dollars (%)’, ‘Price Index’, ‘1998 Dollars’, ‘Change in 1998 Dollars’, ‘Change in 1998 Dollars (%)’, and ‘Notes’).

A folder entitled "Figures" contains some visualizations of the data over time as well as some python scripts to generate these figures. 
