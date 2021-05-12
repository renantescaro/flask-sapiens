from flaskr.utils.config import Config

class ConfigSapiensWs:
    def __init__(self):
        self.url = Config.get('sapiens_ws_url')