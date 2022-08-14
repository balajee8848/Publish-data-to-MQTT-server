import configparser

class configFile:
    @staticmethod
    def getProp(confFileObj, section, option):
        # check whether valid section and option values are given in confg file
        if (confFileObj.has_section(section) == False):
            print("Section not found in config file - ", section)
            exit()
        if (confFileObj.has_option(section, option) == False):
            print("Option not found in config file -  ", option)
            exit()

        return (confFileObj[section][option])

    @staticmethod
    def isPresent():
        # creating object
        configFile = configparser.ConfigParser()

        # check whether config file is there or not
        if configFile.read("config.ini") == []:
            print("Config file not found")
            exit()

        return configFile