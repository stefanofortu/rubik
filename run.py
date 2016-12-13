import subprocess
from cube import Cube

def executeSolver(arg):
	try:
		#subprocess.call()
		p = subprocess.Popen(['./solver/cubex', arg], stdout=subprocess.PIPE)
		(output, err) = p.communicate()
	except:
		print "binary not present"
	return output


def parseAnswer(movesList):
	pass




result=executeSolver("random")
#print result
#f=Face()
#f.printFace()
c=Cube()
c.printCube()
parseAnswer("random")