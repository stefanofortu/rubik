import subprocess
from cube import Cube
from face import Face
from solver import Solver


def executeSolver():
	try:
		p = subprocess.Popen(['/home/stefano/Desktop/rubik/solver/cubex', "random"], stdout=subprocess.PIPE)
		(output, err) = p.communicate()
	except:
		print "binary not present"
		exit();
	return output


s=Solver()
movesList=executeSolver();
###
#  -> deconmmenta questo.
#s.getUserInput()
###
s.solve(movesList)

#strCube=c.stringify()
#print strCube

# print ""
# c.CharToNum()
# print ""
# c.printCube()
# c.verifyFaces()
# getInputFace()
# exit()

