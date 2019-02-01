import numpy as np 
import os
import csv
import pandas as pd 

class Fly():

	cols = ["Ion N","Events","X","Y","Z","Vt","Azm","Elv","B","Bx","By","Bz","KE", "KE Error"]

	def __init__(self, fn):
		self.fn = fn
		self.df = pd.read_csv(fn, header=6, usecols=self.get_cols())
		self.df.rename(index=str, columns={"Ion N": "Num", "KE Error": "Err"}, inplace=True)

	@classmethod
	def get_cols(cls):
		return cls.cols

if __name__ == '__main__':
	fn = '../../1mm_plates/20190131_300mm_1.txt'
	f = Fly(fn)
	

