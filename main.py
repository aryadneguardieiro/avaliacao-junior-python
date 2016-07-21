"""
Author: Aryadne Guardieiro Pereira Rezende
Date: 21/07/2016
Function: This file contains the main method to execute motion activites of the rover object

Input example:
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM
END

Output example:
1 3 N
5 1 E

Contact: aryadneccomp@gmail.com
"""
from rover import Rover 


def main():
	file_name = input("Insert the file name (default: rovers.txt)\n")
	f = open(file_name,'r')
	lines = f.read().splitlines()
	bound = lines[0].split()
	if(len(bound) != 2):
		print("Bound error. Please, review the bounds in the file\n")
		return -3
	Rover.set_boundaries(int(bound[0]),int(bound[1]))
	i = 1 
	
	while (i < (len(lines) -1)):
		rv = lines[i].split()
		if(len(rv)!=3):
			print("Rover definition error. Please, review the location of the rover %s in the file\n"%(i))
			return -4
		r = Rover(int(rv[0]), int(rv[1]),rv[2])
		r.execute_commands(lines[i+1])
		i = i + 2
		r.print_rover()
	f.close()


if __name__ == "__main__":
	main()




