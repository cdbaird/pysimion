import pandas as pd 
import numpy as np 
import os


class Particle():
	def __init__(self, df, zero_origin=True):
		self.df = df
		self.id = df['Num'].values[0]
		self.xyz = np.array(df[['X', 'Y', 'Z']])
		self.energy = df.iloc[0]['KE'] / 1e6 # to MeV
		self.get_splat()
		self.get_z_intercept()
		self.calc_gradient()

	def calc_gradient(self, cols=['X', 'Y', 'Z']):
		if self.z_intercept is None:
			self.calc_gradient_alt()
		
		else:
			p2 = self.splat
			p1 = self.z_intercept
			diff = (p2 - p1)
			grad = np.array([(diff[0] / diff[2]), (diff[1] / diff[2])]) * 1000
			self.gradient = grad

	def calc_gradient_alt(self):
		self.gradient = np.nan

	def get_splat(self):
		s = np.array(self.df.loc[self.df['Events'] == 18,
							['X', 'Y', 'Z']]).ravel()
		self.splat = s

	def get_z_intercept(self):
		z = np.array(self.df.loc[self.df['Events'] == 4098,
							['X', 'Y', 'Z']]).ravel()
		if len(z) == 0:
			z = None
		self.z_intercept = z


if __name__ == '__main__':
	from fly_parser import Fly 
	from test_df import test_df
	f = Fly(test_df)
	print(f.get_splats())
