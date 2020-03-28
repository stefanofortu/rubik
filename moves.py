from cube import Cube
from face import Face


# Introducing a reference system for the whole system.
# The system reference system has origin on
# The origin system is placed on the left front corner of the entire system
# placed horizontally with the horizontal nxt motor on the other side, not visible
# X axis - along the horizontal direction - from left front corner to right front corner
# Y axis - along the depth - across the horizontal direction - from left front corner to left rear corner
# Z axis - along the vertical direction - from left front corner to Up

def execute_move(move):
    if move == "Top_Left":  # TopLeft":
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis +90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        print("executing :" + move)
    elif move == "Top_Right":  # "TopRight"
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        print("executing :" + move)
    elif move == "Left_Up":  # "LeftUp":
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        print("executing :" + move)
    elif move == "Left_Down":  # "LeftDown":
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis +90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        print("executing :" + move)
    elif move == "Front_Clockwise":  # "FrontClockWise":
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Right with Base motor
        print("executing :" + move)
    elif move == "Front_Counterclockwise":
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Right with Base motor
        print("executing :" + move)
    elif move == "Right_Up":
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis +90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        print("executing :" + move)
    elif move == "Right_Down":
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        print("executing :" + move)
    elif move == "Rear_Clockwise":  # "RearClockWise":
        # rotate around z-axis -90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
        print("executing :" + move)
    elif move == "Rear_Counterclockwise":  # "RearCounterClockWise":
        # rotate around z-axis -90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis +90° - rotation Right with Base motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around y-axis +90° - rotation with Arm motor
        # rotate around z-axis -90° - rotation Left with Base motor
    elif move == "Bottom_Left":  # "BottomLeft":
        # rotate around z-axis -90° - rotation Left with Base motor
        print("executing :" + move)
    elif move == "Bottom_Right":  # "BottomRight":
        # rotate around z-axis +90° - rotation Right with Base motor
        print("executing :" + move)
    else:
        print("move not found")