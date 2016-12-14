import subprocess
from cube import Cube
from face import Face

def executeSolver(arg):
	try:
		p = subprocess.Popen(['./solver/cubex', arg], stdout=subprocess.PIPE)
		(output, err) = p.communicate()
	except:
		print "binary not present"
	return output

def parseAnswer(movesList):
	pass

def getInputFace():
	faceNum=1;
	valid=False;
	while (valid == False ):
		print "Insert face # " + str(faceNum) + " : ",
		inputStr=raw_input();
		print inputStr;
		if len(inputStr) != 9:
			print "Insert correct number of elements"
			continue;
		numCorrectChars=0;
		for i in range(0,9):
			if inputStr[i] in allowed_char:
				numCorrectChars +=1;
		if numCorrectChars!=9:
			print "Insert valid letters"
			valid=False
			continue;
		else:
			valid=True;
	return str

#f=Face("yyyyyyyyy")
#f.printFace()
#f.CharToNum()
#f.printFace()

result=executeSolver("random")
c=Cube()
#c.getCubeFromUser()
c.printCube()
print ""
c.CharToNum()
print ""
c.printCube()
c.verifyFaces()
#getInputFace()
#exit()
#print result



#parseAnswer("random")