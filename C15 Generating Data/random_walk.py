# Random walk
from random import choice

class RandomWalk():
	"""A class to generate random walks"""
	
	def __init__(self, num_points=5000):
		"""Initialize attributes of walk"""
		self.num_points = num_points
		
		#All walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]
		
	def get_step(self):
		"""Determine the direction and distance for each step"""
		direction = choice([0.5, -0.5])
		distance = choice([1, 8])
		step = direction * distance
		return step
	
	def fill_walk(self):
		"""Calculate all the points in the walk"""
		
		#Keep taking steps until walk reaches the desired length
		while len(self.x_values) < self.num_points:
			#Decide which direction to go and how far to go in that direction
			x_step = self.get_step()
			y_step = self.get_step()
			
			#Reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue
				
			#Calculate the next x and y values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
			
