"""
Author: Aryadne Guardieiro Pereira Rezende
Date: 21/07/2016
Function: This file contains the rover class and its action methods 
Contact: aryadneccomp@gmail.com
"""

class Rover:

	boundaries = (0,0) #static variable to keep the plateu bounds 
	
	def __init__(self, x,y,orientation):
		self.x = x
		self.y = y
		self.ori = orientation

	@staticmethod
	def set_boundaries(x, y):
		if(x > 0 and y > 0):
			Rover.boundaries=(x,y)

	#This function will evaluate the boundaries before change the rover's position.
	#It will not check a map to find the others rovers location, once it assumes
	#that the rover has sensors caple to avoid crashes 
	def new_position(self, instruction):
		
		if(instruction=='L'):
			self.ori = self.turn_left()
		
		elif(instruction=='R'):
			self.ori = self.turn_right()
		
		elif(instruction=='M'):
			x,y = self.move_forward()
			
			if(not self.inside_boundaries(x,y)):
				return -2 #if it moves it will be outside the plateu
			else:
				self.x = x
				self.y = y
		
		else:
			return -1 #invalid option
		
		return 0 #success

	#move one unit forward based on the rover's heading
	def move_forward(self):
		x = self.x
		y = self.y 
		
		if(self.ori=='N'):
			y = y + 1

		if(self.ori=='E'):
			x = x + 1

		if(self.ori=='S'):
			y = y - 1

		if (self.ori=='W'):
			x = x - 1

		return(x,y)

	#turn the rover 90 degrees clockwise
	def turn_right(self):
		if(self.ori=='N'):
			return'E'
		
		if(self.ori=='E'):
			return 'S'
		
		if(self.ori=='S'):
			return 'W'
		
		if(self.ori=='W'):
			return 'N'		

	#turn the rover 90 degrees counterclockwise
	def turn_left(self):
		if(self.ori=='N'):
			return 'W'
		
		if(self.ori=='W'):
			return 'S'
		
		if(self.ori=='S'):
			return 'E'
		
		if(self.ori=='E'):
			return 'N'

	#check if the rover is in the plateau
	def inside_boundaries(self,n_x,n_y):
		boundary_x, boundary_y = self.boundaries
		
		if(n_x <= boundary_x) and (n_x >=0):
			if(n_y <= boundary_y) and (n_y >=0):
				return True
		
		else:
			return False

	def execute_commands(self, command_list):
		for c in command_list:
			v = self.new_position(c)
			if(v!=0):
				if(v == -1):
					print("Command: %s is not valid (ignored)" % (c))

				if(v == -2):
					print("Rover not moved: action result out of plateau boundaries")
				return v

	def print_rover(self):
		#print("X: %s, Y: %s, Orientation: %s, Boundaries %s" % (self.x,self.y, self.ori, self.boundaries))
		print("%s %s %s" % (self.x, self.y, self.ori))


