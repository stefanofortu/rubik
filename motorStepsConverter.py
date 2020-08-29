from cube import Cube
from face import Face


# Introducing a reference system for the whole system.
# The system reference system has origin on
# The origin system is placed on the left front corner of the entire system
# placed horizontally with the horizontal nxt motor on the other side, not visible
# X axis - along the horizontal direction - from left front corner to right front corner
# Y axis - along the depth - across the horizontal direction - from left front corner to left rear corner
# Z axis - along the vertical direction - from left front corner to Up

def movesConverter(moves):
    if len(moves) == 0:
        print(moves)
        print("Numero di mosse insufficienti")
        return -1
    else:
        movementList = []
        for m in moves:
            movementList.extend(singleMoveConverter(m))

        optimizedMovementList = motorMovesOptimizer(movementList)
        # ###################### Ritorna lista ottimizzata #######################
        print("norm : ", len(movementList))
        print("opt : ", len(optimizedMovementList))
        print(optimizedMovementList)
        return optimizedMovementList


def singleMoveConverter(move):
    motorMovement = []
    if move == "Top_Left":  # TopLeft":
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", +90))  # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        return motorMovement
    elif move == "Top_Right":  # "TopRight"
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        return motorMovement
    elif move == "Left_Up":  # "LeftUp":
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        return motorMovement
    elif move == "Left_Down":  # "LeftDown":
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", +90))  # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        return motorMovement
    elif move == "Front_Clockwise":  # "FrontClockWise":
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Right with Base motor
        return motorMovement
    elif move == "Front_Counterclockwise":
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Right with Base motor
        return motorMovement
    elif move == "Right_Up":
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", +90))  # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        return motorMovement
    elif move == "Right_Down":
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        return motorMovement
    elif move == "Rear_Clockwise":  # "RearClockWise":
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        return motorMovement
    elif move == "Rear_Counterclockwise":  # "RearCounterClockWise":
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("y", +90))  # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        return motorMovement
    elif move == "Bottom_Left":  # "BottomLeft":
        motorMovement.append(("z", -90))  # rotate around z-axis -90° - rotation Left with Base motor
        return motorMovement
    elif move == "Bottom_Right":  # "BottomRight":
        motorMovement.append(("z", +90))  # rotate around z-axis +90° - rotation Right with Base motor
        return motorMovement
    else:
        print("move not found")
        return -1


def motorMovesOptimizer(moveList):
    chunkList = [[moveList[0]]]
    for m in moveList:
        if chunkList[-1][-1][0] == m[0]:
            chunkList[-1].extend([m])
        else:
            chunkList.append([m])

    optimizedList = []
    for chunk in chunkList:
        axle = chunk[0][0]
        totalAngle = 0
        for c in chunk:
            totalAngle += c[1]
        optimizedAngle = totalAngle % 360
        optimizedList. append((axle, optimizedAngle))

    return optimizedList
