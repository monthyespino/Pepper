from naoqi import ALProxy #? Library Connection 

#! ALTextToSpeech Function:
tts = ALProxy("ALTextToSpeech", "127.0.0.1", 59730)
tts.say("hello")