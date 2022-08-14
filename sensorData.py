from datetime import datetime
import random

class sensorData:
    @staticmethod
    def fetch():
        """ for now we are generating temperature data randomly """
        # fetching the current time
        time = datetime.now().strftime("%H:%M:%S")

        # updating temperature value as random numbers between 32 and 37
        data = str(random.randrange(32, 37)) + " C"

        temp = {}
        temp.update({'currTime':str(time)})
        temp.update({'temperature':str(data)})

        return temp