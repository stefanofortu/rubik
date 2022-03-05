# from nxtMotors.nxtMotorFunctions import GPIOinitialization, GPIOcleanup, nxtMotorRotation
from Classes.MotorHandlerServer import MotorHandlerServer
from Classes.MotorHandlerClient import MotorHandlerClient
from Classes.MotorMovement import MotorMovement
import time


def execute_user_input(userInput):
    motorMovement = None
    if userInput.lower() == "i":  # per initialization only
        print("INIT To Be Implemented")
        # nxtMotorRotation(1, direction=-1, rotationSteps=50,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "s":  # da ROTATE A START : "Start" : "S"
        print("GO --> START To Be Implemented")
        # nxtMotorRotation(1, direction=-1, rotationSteps=310,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "g":  # da START A ROTATE : "Go" : "G"
        print("START --> GO To Be Implemented")
        # nxtMotorRotation(1, direction=+1, rotationSteps=300,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "u":  # from ROTATE to UP : "Up" : "U"
        motorMovement = MotorMovement(name="goUp", direction=0)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "ARM", 'movement': "ARM_goUp",
                         'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # nxtMotorRotation(1, direction=-1, rotationSteps=200,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "d":  # da UP a ROTATE : "Down" : "D"
        motorMovement = MotorMovement(name="goDown", direction=0)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "ARM", 'movement': "ARM_goDown",
                         'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}

        # nxtMotorRotation(1, direction=+1, rotationSteps=200,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "f":  # da ROTATE A ROTATE : "Rotation" : "R"
        motorMovement = MotorMovement(name="ARM_flipCube", direction=0)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "ARM", 'movement': "ARM_flipCube",
                         'direction': 0, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # nxtMotorRotation(1, direction=+1, rotationSteps=150,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        # time.sleep(0.25)
        # nxtMotorRotation(1, direction=-1, rotationSteps=300,
        #                 PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                 input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
        # time.sleep(0.1)
        # nxtMotorRotation(1, direction=+1, rotationSteps=125,
        #                  PWMPin=Mot2_PWM_Pin, InvPin=Mot2_Inv_Pin, enablePin=Mot2_Enable_Pin,
        #                input1=Mot2_decoderIN1_Pin, input2=Mot2_decoderIN2_Pin)
    elif userInput.lower() == "1":  # +90 degree
        motorMovement = MotorMovement(name="BASE_change", direction=+90)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_change",
                         'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "change",
        #                 'direction': +90, 'movementNumWithinStep': 0, 'totalMovementWithinStep': 0}
        # nxtMotorRotation(1, direction=+1, rotationSteps=537,
        #                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        # time.sleep(1)
        # nxtMotorRotation(1, direction=-1, rotationSteps=12,
        #                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "2":  # +180 degree
        motorMovement = MotorMovement(name="BASE_change", direction=-90)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_change",
                         'direction': -90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE",
        #                 'movement': "change", 'direction': -90, 'movementNumWithinStep': 0,
        #                 'totalMovementWithinStep': 0}

    # nxtMotorRotation(1, direction=+1, rotationSteps=1020,
    # PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    # input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

    # elif userInput.lower() == "3":  # +270 degree
    #    nxtMotorRotation(1, direction=+1, rotationSteps=1560,
    #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    # elif userInput.lower() == "4":  # +360 degree
    #    nxtMotorRotation(1, direction=+1, rotationSteps=2100,
    #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "3":
        motorMovement = MotorMovement(name="BASE_change", direction=+10)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_change",
                         'direction': 10, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE",
        #                 'movement': "change", 'direction': +10, 'movementNumWithinStep': 0,
        #                 'totalMovementWithinStep': 0}
    #    nxtMotorRotation(1, direction=+1, rotationSteps=5,
    #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "4":
        motorMovement = MotorMovement(name="BASE_change", direction=-10)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_change",
                         'direction': -10, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE",
        #                 'movement': "change", 'direction': -10, 'movementNumWithinStep': 0,
        #                 'totalMovementWithinStep': 0}
    #   nxtMotorRotation(1, direction=-1, rotationSteps=5,
    #                   PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                   input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "7":  # +90 degree
        motorMovement = MotorMovement(name="BASE_rotation", direction=+90)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_rotation",
                         'direction': +90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "change",
        #                 'direction': +90, 'movementNumWithinStep': 0, 'totalMovementWithinStep': 0}
        # nxtMotorRotation(1, direction=+1, rotationSteps=537,
        #                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
        # time.sleep(1)
        # nxtMotorRotation(1, direction=-1, rotationSteps=12,
        #                 PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
        #                 input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "8":  # +180 degree
        motorMovement = MotorMovement(name="BASE_rotation", direction=-90)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_rotation",
                         'direction': -90, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE",
        #                 'movement': "change", 'direction': -90, 'movementNumWithinStep': 0,
        #                 'totalMovementWithinStep': 0}

    # nxtMotorRotation(1, direction=+1, rotationSteps=1020,
    # PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    # input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)

    # elif userInput.lower() == "3":  # +270 degree
    #    nxtMotorRotation(1, direction=+1, rotationSteps=1560,
    #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    # elif userInput.lower() == "4":  # +360 degree
    #    nxtMotorRotation(1, direction=+1, rotationSteps=2100,
    #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "9":
        motorMovement = MotorMovement(name="BASE_rotation", direction=+10)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_rotation",
                         'direction': +10, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE",
        #                 'movement': "change", 'direction': +10, 'movementNumWithinStep': 0,
        #                 'totalMovementWithinStep': 0}
    #    nxtMotorRotation(1, direction=+1, rotationSteps=5,
    #                     PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                     input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    elif userInput.lower() == "0":
        motorMovement = MotorMovement(name="BASE_rotation", direction=-10)
        motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE", 'movement': "BASE_rotation",
                         'direction': -10, 'movementNumWithinStep': 1, 'totalMovementWithinStep': 1}
        # motorMovement = {'moveName': "", 'moveNumber': 0, 'motor': "BASE",
        #                 'movement': "change", 'direction': -10, 'movementNumWithinStep': 0,
        #                 'totalMovementWithinStep': 0}
    #   nxtMotorRotation(1, direction=-1, rotationSteps=5,
    #                   PWMPin=Mot1_PWM_Pin, InvPin=Mot1_Inv_Pin, enablePin=Mot1_Enable_Pin,
    #                   input1=Mot1_decoderIN1_Pin, input2=Mot1_decoderIN2_Pin)
    else:
        print("Choice not valid. Try again")

    return motorMovement


def main():
    simulateMotors = True
    run_server_locally = False

    #motor_handler = MotorHandlerServer(simulateMotors=simulateMotors)
    motor_handler = MotorHandlerClient(run_server_locally=run_server_locally,
                                       simulateMotors=simulateMotors)

    print("[1]:+9O(Change) [2]:+180(Change) [3]:+10(Change) [4]:-10(Change)")
    print("[7]:+9O(Rotate) [8]:+180(Rotate) [9]:+10(Rotate) [0]:-10(Rotate)")
    print("[I]nit  [S]tart  [G]o  [U]p  [D]own  [F]lip  [Q]uit")
    while True:
        user_input = input("Select one option: ")
        if user_input.lower() != "q":
            motor_movement = execute_user_input(user_input)
            if motor_movement:
                motor_handler.executeMovement(motor_movement)
        else:
            break


if __name__ == "__main__":
    main()
