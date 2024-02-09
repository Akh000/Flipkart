import configparser

config = configparser.RawConfigParser()
file = "D:\\Python\\Flipkart\\Configuration\\config.ini"
config.read(file)


class Readconfig:

    @staticmethod
    def getUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def getUrl():
        url = config.get('common data', 'url')
        return url
