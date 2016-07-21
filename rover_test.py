"""
Author: Aryadne Guardieiro Pereira Rezende
Date: 21/07/2016
Function: This file contains unit tets for functions of Rover object 
Contact: aryadneccomp@gmail.com
"""

from rover import Rover 

#test the Rover object creating two rovers and printing their values
def test_object(r):
	r.print_rover()
	r2 = Rover(3,3,'E')
	r2.print_rover()

#turn 4 times clockwise to test right turnning 
def test_turn_right(r):
	r.print_rover()	
	r.new_position('R')
	r.print_rover()	
	r.new_position('R')
	r.print_rover()
	r.new_position('R')
	r.print_rover()
	r.new_position('R')
	r.print_rover()

#turn 4 times counterclockwise to test left turnning 
def test_turn_lef(r):
	r.print_rover()	
	r.new_position('L')
	r.print_rover()	
	r.new_position('L')
	r.print_rover()
	r.new_position('L')
	r.print_rover()
	r.new_position('L')
	r.print_rover()

def test_move_forward(r):
	r.print_rover()	
	r.new_position('M')
	r.print_rover()	
	r.new_position('R')
	r.print_rover()
	r.new_position('M')
	r.print_rover()
	r.new_position('L')
	r.print_rover()
	r.new_position('M')
	r.print_rover()

#creat a rover and move it, executing the three kinds of moviment 
def test_rover_motion(r):
	r.print_rover()	
	r.new_position('L')
	r.print_rover()	
	r.new_position('R')
	r.print_rover()
	r.new_position('M')
	r.print_rover()

def test_move_back(r):
	r.print_rover()	
	r.new_position('M')
	r.print_rover()	
	r.new_position('R')
	r.print_rover()
	r.new_position('R')
	r.print_rover()
	r.new_position('M')
	r.print_rover()

def test_execute_commands(r):
	#r.execute_commands('MMMLMMM')
	r.execute_commands('RLRLRLRLMMMRLRL')
	r.print_rover()

Rover.set_boundaries(5,5)
r = Rover(1,1,'E')
#test_object(r)
#test_rover_motion(r)
#test_move_forward(r)
#test_turn_lef(r)
#test_turn_right(r)
#test_move_back(r)
test_execute_commands(r)

