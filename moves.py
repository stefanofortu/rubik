from cube import Cube
from face import Face


def executeMove(cube,move):
	if move=="RD":
		print(cube.faceList['top'].face)
		cube.printCube()