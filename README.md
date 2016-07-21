# teste_junior

Hello user,

You can run this project executing the main.py file running it in a terminal window (already inside of its
directory):

    python3 main.py

When the system ask you for a file you can put yours, or a default file called rovers.txt . This file
already if filled with this example:

    5 5
    1 2 N
    LMLMLMLMM
    3 3 E
    MMRMMRMRRM

Errors you can get:

	- "Command: X is not valid (ignored)" 
	
	You put a different command in your file (not L, M or R)
	
	- "Rover not moved: action result out of plateau boundaries" 
	  
    Some rover is or is trying to go out of the plateau boundaries
	
	-  "Bound error. Please, review the bounds in the file"
	
    The boundaries could not be loaded in the application because they have a wrong format
	
	- "Rover definition error. Please, review the location of the rover X in the file"
	
    Some rover has a bad location definition 

Unit tests can be found inside the rover_test.py . You can run this file using the command line:
    
    python3 rover_test.py 

Depending on the function being called you will get a different result. 

Any question please contact: aryadneccomp@gmail.com
