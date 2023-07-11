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


class MotorMovementSimulator:
    def __init__(self):
        self.step_number = 0
        self.isStepValid()
        self.movement_list = []

    def load_moves(self, moves_list):
        if not isinstance(moves_list, list):
            raise TypeError
        for mv in moves_list:
            self.movement_list.append(mv)

       # if not isinstance(self.step, str):
        #    raise TypeError
        #if not isinstance(self.stepNumber, int):
        #    raise TypeError

    def append(self, movement):
        if isinstance(movement, MotorMovement):
            self.movement_list.append(movement)
        else:
            raise TypeError

