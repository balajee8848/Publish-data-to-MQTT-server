import logging

class setupLog:
    def basicConfiguration(tempLevel):
        tempLevel = str(tempLevel)
        if tempLevel.lower() == "debug":
            logging.basicConfig(filename='logFile.log',
                                level=logging.DEBUG,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='w')
        elif tempLevel.lower() == "info":
            logging.basicConfig(filename='logFile.log',
                                level=logging.INFO,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='w')
        elif tempLevel.lower() == "warning":
            logging.basicConfig(filename='logFile.log',
                                level=logging.WARNING,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='w')
        elif tempLevel.lower() == "error":
            logging.basicConfig(filename='logFile.log',
                                level=logging.ERROR,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='w')
        elif tempLevel.lower() == "critical":
            logging.basicConfig(filename='logFile.log',
                                level=logging.CRITICAL,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='w')
        else:
            logging.basicConfig(filename='logFile.log',
                                level=logging.CRITICAL + 1,
                                format='%(asctime)s - %(levelname)s - %(message)s',
                                filemode='w')

        return