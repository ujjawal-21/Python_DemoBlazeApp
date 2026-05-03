import configparser

config = configparser.RawConfigParser()
config.read("Configuration\\config.ini")

class ReadConfig:
    
    @staticmethod 
    def getAppURL():
        url = config.get('app info', 'app_url')
        return url
    
    @staticmethod 
    def getUsername():
        username = config.get('app info', 'app_username')
        return username
    
    @staticmethod 
    def getPassword():
        password = config.get('app info', 'app_password')
        return password