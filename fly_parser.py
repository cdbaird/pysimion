import numpy as np 
import os
import csv
import pandas as pd 

from particle import Particle

class Fly():

	cols = ["Ion N","Events","X","Y","Z","Vt","Azm","Elv","B","Bx","By","Bz","KE", "KE Error"]

	def __init__(self, fn):
		self.fn = fn
		self.df = pd.read_csv(fn, header=6, usecols=self.get_cols())
		self.df.rename(index=str, columns={"Ion N": "Num", "KE Error": "Err"}, inplace=True)
		self.df.dropna(inplace=True)
		self.df['Num'] = pd.to_numeric(self.df['Num'], downcast='integer')
		self.assign_particles()

	def assign_particles(self):
		part_ids = np.unique(self.df['Num'])
		particles = np.empty(len(part_ids), dtype=object)
		for i, n in enumerate(part_ids):
			temp = self.df.loc[(self.df['Num'] == n), :]
			particles[i] = Particle(temp)

		self.particles = particles

	@classmethod
	def get_cols(cls):
		return cls.cols

if __name__ == '__main__':
	fn = './files/test_df.txt'
	f = Fly(fn)
	print(f.particles[0].splat)
	

