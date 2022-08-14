import configparser

class configFile:
    @staticmethod
    def getProp(section, key):
        #creating object
        config = configparser.ConfigParser()

        #reading config
        config.read("config.ini")

        return(config[section][key])
