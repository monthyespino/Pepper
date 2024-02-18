from naoqi import ALProxy
from Movement.Stiffness import StiffnessController
from .Connections.Sync import PepperConnection
import motion, almath


def main():

    params_file = "params.json"
    connection = PepperConnection(params_file)
    stiffness = StiffnessController(connection.ip, connection.port)

    try:
        MotionPx = connection.get_proxy("ALMotion")
    except Exception as e:
        print("Could not create proxy to ALMotion")
        print("ERROR:", e)

    try:
        PosturePx = connection.get_proxy("ALRobotPosture")
    except Exception as e:
        print("Could not create proxy to ALRobotPosture")
        print("ERROR:", e)
    
    stiffness.StiffnessOn(MotionPx)

    PosturePx.goToPosture("StandInit", 0.5)

    effector = "LArm"
    space = motion.FRAME_ROBOT
    axisMask = almath.AXIS_MASK_ALL
    isAbsolute = False

    currentPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    dx = 0.03
    dy = 0.03
    dz = 0.0
    dwx = 0.0
    dwy = 0.0
    dwz = 0.0
    targetPos = [dx, dy, dz, dwx, dwy,dwz]

    path = [targetPos, currentPos]
    times = [2.0, 4.0]

    MotionPx.positionInterpolation(effector, space, path, axisMask, times, isAbsolute)

