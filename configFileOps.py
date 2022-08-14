import configparser

class configFile:
    @staticmethod
    def getProp(section, option):
        # creating object
        configFile = configparser.ConfigParser()
        configFile.read('config.ini')

        # check whether valid section and option values are given in confg file
        if (configFile.has_section(section) == False):
            print("Section not found in config file - ", section)
            exit()
        if (configFile.has_option(section, option) == False):
            print("Option not found in config file -  ", option)
            exit()

        return (configFile[section][option])

    @staticmethod
    def isPresent():
        # creating object
        configFile = configparser.ConfigParser()

        # check whether config file is there or not
        if configFile.read("config.ini") == []:
            print("Config file not found")
            exit()

        return;