import os
import pandas as pd
import numpy as np

####filepaths
interest_15 = "data/primary15yr.txt"
interest_30 = "data/primary30yr.txt"
state_hbi = "data/state_hbi.csv"
state_uer = "data/state_uer.csv"
uer = "UnemploymentHistory.txt"
###delimiters differ by file :rage:

class Preprocess():

	def __init__(self):
		pass

	def clean_interest(df):
		df.index = map(lambda x: x[-4:] + x[:2], df["Date"])
		df.index = df.index.astype(int)
		df.drop('Date', axis=1, inplace=True)
		return df
