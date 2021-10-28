from flaskr.utils.config import Config

class ConfigSapiensWs:
    def __init__(self):
        self.url = Config.get('SAPIENS_WS_URL')