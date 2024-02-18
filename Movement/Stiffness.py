from naoqi import ALProxy

class StiffnessController:

    def __init__(self, robot_ip, robot_port):
        self.robot_ip = robot_ip
        self.robot_port = robot_port
        self.motionProxy = ALProxy("ALMotion", self.robot_ip, self.robot_port)

    def StiffnessOn(self):

        pName = "Body"
        pStiffnessLists = 1.0
        pTimeLists = 1.0
        self.motionProxy.stiffnessInterpolation(pName, pStiffnessLists, pTimeLists)