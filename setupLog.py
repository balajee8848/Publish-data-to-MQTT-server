import logging

class setupLog:
    def basicConfiguration():
        logging.basicConfig(filename='logFile.log',
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s',
                            filemode='w')

        return