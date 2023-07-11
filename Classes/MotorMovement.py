class MotorMovement:

    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.isMovementValid()

    def isMovementValid(self):
        if not isinstance(self.name, str):
            raise TypeError

        if not isinstance(self.direction, int):
            raise TypeError

        if self.name in ["BASE_change", "BASE_rotation"]:
            if self.direction not in [+90, -90, +10, -10]:
                raise ValueError
        elif self.name in ["ARM_flipCube", "ARM_goUp", "ARM_goDown", "ARM_start", "ARM_go"]:
            if self.direction != 0:
                print("direction != 0 for this move")
                raise ValueError
        else:
            raise ValueError

    def __str__(self):
        return "Movement: %s with direction %d" % (self.name, self.direction)

    def __repr__(self):
        return "<Movement name:%s direction:%s>" % (self.name, self.direction)
