from Classes.MotorMovement import MotorMovement

moves_dict = {"UR": "Top_Right", "UL": "Top_Left", "LU": "Left_Up", "LD": "Left_Down",
              "FC": "Front_Clockwise", "FA": "Front_Counterclockwise", "RU": "Right_Up", "RD": "Right_Down",
              "DL": "Bottom_Left", "DR": "Bottom_Right", "BC": "Rear_Clockwise", "BA": "Rear_Counterclockwise"}

#side_dict = {'U': "Top", 'D': "Bottom", 'L': "Left", 'R': "Right", 'F': "Front", 'B': "Rear"}
#direction_dict = {'L': "Left", 'R': "Right", 'U': "Up", 'D': "Down", 'C': "Clockwise", 'A': "Counterclockwise"}


#def stringMoveConverter(m):
#    mv = side_dict[m[0]] + "_" + direction_dict[m[1]]
#    return mv


class CubeMove:
    def __init__(self, name):
        if name in moves_dict.values():
            self.name = name
        elif name in moves_dict.keys():
            self.name = moves_dict[name]
        else:
            print("input value not valid")
            raise ValueError
        self.is_move_valid()
        self.motor_movements_list = self.move_to_movementes()

    def is_move_valid(self):
        if not isinstance(self.name, str):
            raise TypeError

        if self.name not in moves_dict.values():
            raise ValueError

    def __str__(self):
        return "Move: %s " % (self.name)

    def __repr__(self):
        return "<Move name:%s >" % (self.name)

    def move_to_movementes(self):
        motorMovement = []
        if self.name == "Top_Left":  # TopLeft":
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("BASE_change", +90))
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            return motorMovement
        elif self.name == "Top_Right":  # "TopRight"
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("BASE_change", -90))
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            return motorMovement
        elif self.name == "Left_Up":  # "LeftUp":
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("BASE_change", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': -90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 5})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 5})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 5})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 5})
            return motorMovement
        elif self.name == "Left_Down":  # "LeftDown":
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("BASE_change", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': +90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 5})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 5})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 5})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 5})
            return motorMovement
        elif self.name == "Front_Clockwise":  # "FrontClockWise":
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("BASE_change", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': +90, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
            # #rotate around y-axis +90° - rotation with Arm motor
            # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #                      'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
            # #rotate around y-axis +90° - rotation with Arm motor
            # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #                      'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 5})
            # rotate around y-axis -180° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
            # rotate around z-axis +90° - rotation Right with Base motor
            # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "flipCube",
            #                      'direction': +90, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
            return motorMovement
        elif self.name == "Front_Counterclockwise":
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': +90, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("BASE_change", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': -90, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
            # rotate around y-axis -180° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
            # rotate around z-axis +90° - rotation Right with Base motor
            # motorMovement.append({'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "flipCube",
            #                      'direction': +90, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
             #   {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
             #    'direction': 0, 'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
            return motorMovement
        elif self.name == "Right_Up":
            # rotate around z-axis -180° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 11})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 11})
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("BASE_change", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': +90, 'movementNumWithinStep': 6, 'totalMovementWithinStep': 11})
            ## rotate around z-axis -180° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 7, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #    'direction': -90, 'movementNumWithinStep': 8, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 9, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 10, 'totalMovementWithinStep': 11})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
            return motorMovement
        elif self.name == "Right_Down":
            # rotate around z-axis -180° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 11})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': +90, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 11})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("BASE_change", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': -90, 'movementNumWithinStep': 6, 'totalMovementWithinStep': 11})
            # rotate around z-axis -180° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 7, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 8, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 9, 'totalMovementWithinStep': 11})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 10, 'totalMovementWithinStep': 11})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': +90, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 11})
            return motorMovement
        elif self.name == "Rear_Clockwise":  # "RearClockWise":
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': +90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': -90, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
            # rotate around y-axis -180° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
            # rotate around z-axis +90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': +90, 'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
            return motorMovement
        elif self.name == "Rear_Counterclockwise":  # "RearCounterClockWise":
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': +90, 'movementNumWithinStep': 2, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 3, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 4, 'totalMovementWithinStep': 13})
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("BASE_change", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': +90, 'movementNumWithinStep': 5, 'totalMovementWithinStep': 13})
            # rotate around y-axis -180° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 6, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 7, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': -90, 'movementNumWithinStep': 8, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 9, 'totalMovementWithinStep': 13})
            # rotate around y-axis +90° - rotation with Arm motor
            motorMovement.append(MotorMovement("ARM_flipCube", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "flipCube",
            #     'direction': 0, 'movementNumWithinStep': 10, 'totalMovementWithinStep': 13})
            # rotate around z-axis +90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("ARM_goUp", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goUp",
            #     'direction': 0, 'movementNumWithinStep': 11, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("BASE_rotation", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "rotation",
            #     'direction': +90, 'movementNumWithinStep': 12, 'totalMovementWithinStep': 13})
            motorMovement.append(MotorMovement("ARM_goDown", 0))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "ARM", 'movement': "goDown",
            #     'direction': 0, 'movementNumWithinStep': 13, 'totalMovementWithinStep': 13})
            return motorMovement
        elif self.name == "Bottom_Left":  # "BottomLeft":
            # rotate around z-axis -90° - rotation Left with Base motor
            motorMovement.append(MotorMovement("BASE_change", -90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': -90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1})
            return motorMovement
        elif self.name == "Bottom_Right":  # "BottomRight":
            # rotate around z-axis +90° - rotation Right with Base motor
            motorMovement.append(MotorMovement("BASE_change", +90))
            #motorMovement.append(
            #    {'moveName': moveName, 'moveNumber': moveNumber, 'motor': "BASE", 'movement': "change",
            #     'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1})
            return motorMovement
        else:
            print("move not found")
            print(moveName)
            return -1
