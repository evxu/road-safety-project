import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np

def pieplot_year(column, index, labels, year = '2014', title = '2014', figsize = (5,5), data = 'data2/Accidents_'):
	df = pd.read_csv(data + year + '.csv',low_memory=False)
	plt.figure(figsize = figsize)
	s = df[column].value_counts()
	s = s.reindex(index)
	s.plot.pie(labels = labels)
	plt.title(title)

    
def pieplot_years(column, index, labels, data = 'data2/Accidents_'):
	years = ['2009', '2010', '2011', '2012', '2013', '2014']
	nfig = 1
	plt.figure(figsize = (15,10))
	for year in years:
	    df = pd.read_csv(data + year + '.csv',low_memory=False)
	    s = df[column].value_counts()
	    s = s.reindex(index)
	    plt.subplot(2,3,nfig)
	    s.plot.pie(labels = labels)
	    plt.title(year, fontsize = 22)
	    nfig += 1

def pieplot_df(column, index, labels, data, title = '2014', figsize = (5,5)):
	df = data
	plt.figure(figsize = figsize)
	s = df[column].value_counts()
	s = s.reindex(index)
	s.plot.pie(labels = labels)
	plt.title(title)
	plt.show()