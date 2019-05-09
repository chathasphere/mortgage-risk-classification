import os
import pandas as pd
import numpy as np

####filepaths
#interest_15 = "data/primary15yr.txt"
#interest_30 = "data/primary30yr.txt"
#state_hbi = "data/state_hbi.csv"
#state_uer = "data/state_uer.csv"
#uer = "UnemploymentHistory.txt"


def clean_interest(df):
	df.index = map(lambda x: x[-4:] + x[:2], df["Date"])
	df.index = df.index.astype(int)
	df.drop('Date', axis=1, inplace=True)
	return df

def clean_hpi(df):
	df['Date'] = df['Date'].apply(lambda x: x[3:] + x[:2])
	df['Date'] = df['Date'].astype(int, copy=False)
	df.set_index('Date', inplace = True)
	return df

def calculate_hpa(hpi):

