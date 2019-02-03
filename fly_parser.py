import numpy as np 
import os
import csv
import pandas as pd 

from .particle import Particle

class Fly():

	cols = ["Ion N","Events","X","Y","Z","Vt","Azm","Elv","B","Bx","By","Bz","KE", "KE Error"]
	dtypes = {"Ion N" : str,
			"Events" : str,
			"X" : 'float64',
			"Y" : 'float64',
			"Z" : 'float64',
			"Vt" : 'float64',
			"Azm" : 'float64',
			"Elv" : 'float64',
			"B" : 'float64',
			"Bx" : 'float64',
			"By" : 'float64',
			"Bz" : 'float64',
			"KE" : 'float64',
			"KE Error" : 'float64'}


	def __init__(self, fn, zero_origin=True):
		self.fn = fn
		self.df = pd.read_csv(fn, header=6, 
						usecols=self.get_cols(), 
						dtype=self.get_dtypes())

		self.df.rename(index=str,
						columns={"Ion N": "Num", "KE Error": "Err"},
						inplace=True)

		self.df.dropna(inplace=True)

		self.df['Num'] = pd.to_numeric(self.df['Num'], 
						downcast='integer')

		self.df['Events'] = pd.to_numeric(self.df['Events'], 
						downcast='integer')

		self.__assign_particles()

	def __assign_particles(self):
		part_ids = np.unique(self.df['Num'])
		particles = np.empty(len(part_ids), dtype=object)
		for i, n in enumerate(part_ids):
			temp = self.df.loc[(self.df['Num'] == n), :]
			particles[i] = Particle(temp)

		self.particles = particles

	def get_splats(self):
		s = []
		for p in self.particles:
			s.append(p.splat)

		s = np.array(s)
		return s

	def get_ke(self):
		ke = []
		for p in self.particles:
			ke.append(p.energy)

		ke = np.array(ke)
		return ke

	def get_traj(self):
		xyz = []
		for p in self.particles:
			xyz.append(p.xyz)

		xyz = np.array(xyz)
		return xyz

	@classmethod
	def get_cols(cls):
		return cls.cols

	@classmethod
	def get_dtypes(cls):
		return cls.dtypes

if __name__ == '__main__':
	fn = './files/test_df.txt'
	f = Fly(fn)
	print(f.df.dtypes)

