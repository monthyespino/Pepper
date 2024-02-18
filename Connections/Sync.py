from naoqi import ALProxy
import os, json

class PepperConnection():

    def __init__(self, params_file):
        self.params_file = params_file
        self.ip, self.port = self.load_params()

    def load_params(self):
        with open(self.params_file, 'r') as fp:
            params = json.load(fp)
        return params["robot_ip"], params["robot_port"]
    
    def get_proxy(self, proxy_mode):
        return ALProxy(proxy_mode, self.ip, self.port)
    