# Introducing a reference system for the whole system.
# The system reference system has origin on
# The origin system is placed on the left front corner of the entire system
# placed horizontally with the horizontal nxt motor on the other side, not visible
# X axis - along the horizontal direction - from left front corner to right front corner
#    rotation: +90 : counterclockwise direction (cube seen from top view)
#    rotation: -90 : clockwise direction        (cube seen from top view)
# Y axis - along the depth - across the horizontal direction - from left front corner to left rear corner
# Z axis - along the vertical direction - from left front corner to Up
from Classes.MotorMovement import MotorMovement


def movesConverter(moves):
    if len(moves) == 0:
        print(moves)
        print("Numero di mosse insufficienti")
        return -1
    else:
        movementList = []
        for i, m in enumerate(moves, start=1):
            movementList.extend(singleMoveConverter(m, i))
        print(movementList)
        return movementList
        # optimizedMovementList = motorMovesOptimizer(movementList)
        # ###################### Ritorna lista ottimizzata #######################
        # print("norm : ", len(movementList))
        # print("opt : ", len(optimizedMovementList))
        # print(optimizedMovementList)
        # return optimizedMovementList


def singleMoveConverter(moveName, moveNumber=0):
    motorMovement = []
    if moveName == "Top_Left":  # TopLeft":
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM",
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 5})
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=+90),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM",
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 5})
        return motorMovement
    elif moveName == "Top_Right":  # "TopRight"
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 5})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=-90),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 5})
        return motorMovement
    elif moveName == "Left_Up":  # "LeftUp":
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=-90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 5})
        return motorMovement
    elif moveName == "Left_Down":  # "LeftDown":
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=+90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube", direction=0),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 5})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 5})
        return motorMovement
    elif moveName == "Front_Clockwise":  # "FrontClockWise":
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp", direction=0),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=+90),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
        # #rotate around y-axis +90° - rotation with Arm motor
        # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
        #                      'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
        # #rotate around y-axis +90° - rotation with Arm motor
        # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
        #                      'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
        # rotate around y-axis -180° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
        # rotate around z-axis +90° - rotation Right with Base motor
        # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "flipCube",
        #                      'direction': +90, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
        return motorMovement
    elif moveName == "Front_Counterclockwise":
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=-90),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
        # rotate around y-axis -180° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
        # rotate around z-axis +90° - rotation Right with Base motor
        # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "flipCube",
        #                      'direction': +90, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
        return motorMovement
    elif moveName == "Right_Up":
        # rotate around z-axis -180° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 11})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 11})
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=+90),
             'movementNumWithinStep': 6, 'totalMovementWithinStep': 11})
        # rotate around z-axis -180° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 7, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 8, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 9, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 10, 'totalMovementWithinStep': 11})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
        return motorMovement
    elif moveName == "Right_Down":
        # rotate around z-axis -180° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 11})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 11})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=-90),
             'movementNumWithinStep': 6, 'totalMovementWithinStep': 11})
        # rotate around z-axis -180° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 7, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
'movementNumWithinStep': 8, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 9, 'totalMovementWithinStep': 11})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 10, 'totalMovementWithinStep': 11})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
        return motorMovement
    elif moveName == "Rear_Clockwise":  # "RearClockWise":
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=+90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=-90),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
        # rotate around y-axis -180° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
        # rotate around z-axis +90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=+90),
             'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
        return motorMovement
    elif moveName == "Rear_Counterclockwise":  # "RearCounterClockWise":
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=+90),
             'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=+90),
             'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
        # rotate around y-axis -180° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=-90),
             'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
        # rotate around y-axis +90° - rotation with Arm motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_flipCube"),
             'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
        # rotate around z-axis +90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goUp"),
             'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_rotation", direction=+90),
             'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="ARM_goDown"),
             'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
        return motorMovement
    elif moveName == "Bottom_Left":  # "BottomLeft":
        # rotate around z-axis -90° - rotation Left with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=-90),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 1})
        return motorMovement
    elif moveName == "Bottom_Right":  # "BottomRight":
        # rotate around z-axis +90° - rotation Right with Base motor
        motorMovement.append(
            {'moveName': moveName, 'moveNumber': moveNumber,
             'movement': MotorMovement(name="BASE_change", direction=+90),
             'movementNumWithinStep': 1, 'totalMovementWithinStep': 1})
        return motorMovement
    else:
        print("move not found")
        print(moveName)
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
        optimizedList.append((axle, optimizedAngle))

    return optimizedList


def getNextArmPosition(currentArmPosition, movement):
    nextArmPosition = ""
    print("getNextArmPosition() da implementare")
    return nextArmPosition
    if movement['motor'] == "ARM":
        if movement['movement'] == "goUp":
            if currentArmPosition == "DOWN":
                nextArmPosition = "UP"
        elif movement['movement'] == "goDown":
            if currentArmPosition == "UP":
                nextArmPosition = "DOWN"
        elif movement['movement'] == "flipCube":
            pass
        else:
            print("getNextArmPosition() : movement not valid")
            return -1

    return nextArmPosition
