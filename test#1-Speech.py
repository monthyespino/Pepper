from naoqi import ALProxy #? Library Connection 
import os, json

path = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(path, "params.json"), 'r') as fp:
    params = json.load(fp)

params = params["params"]
ip = params["robot_ip"]
port = params["robot_port"]

#! ALTextToSpeech Function:
tts = ALProxy("ALTextToSpeech", ip, port)
tts.say("hello")