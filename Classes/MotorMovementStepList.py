from Classes import MotorMovement


#######################################################
# DOC: How every motor movement is described:
# 'moveName': STRING
# 'moveNumber': INTEGER
# 'motor': STRING : "ARM" or "BASE"
# 'movement': STRING :  "ARM_flipCube", "ARM_goUp", "ARM_goDown" , ARM_start , ARM_go
#                       "BASE_change", "BASE_rotation"
# 'direction': INTEGER that belong to set (0, +90, -90, +10 , -10)
# 'movementNumWithinStep': INTEGER > 0
# 'totalMovementWithinStep': INTEGER > 0
# IMPROVEMENT:
# {moveName: STRING, moveNumber: INT, step_number: [ARRAY OF DICT{movement: STRING, direction:INTEGER}]}


class MotorMovementStepList:
    def __init__(self, step, stepNumber):
        self.step = step
        self.step_number = stepNumber
        self.isStepValid()
        self.movement_list = []

    def isStepValid(self):
        if not isinstance(self.step, str):
            raise TypeError
        if not isinstance(self.stepNumber, int):
            raise TypeError

    def append(self, movement):
        if isinstance(movement, MotorMovement):
            self.movement_list.append(movement)
        else:
            raise TypeError

