import pandas as pd 
import numpy as np 
import os


class Particle():
	def __init__(self, df):
		self.__df = df
		self.id = df['Num'].values[0]
		self.xyz = np.array(df[['X', 'Y', 'Z']])
		self.energy = df.iloc[0]['KE'] / 1e6 # to MeV
		self.splat = np.array(df.loc[df['Events'] == 18, ['X', 'Y', 'Z']])

if __name__ == '__main__':
	pass
