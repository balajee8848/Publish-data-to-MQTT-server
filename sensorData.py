from datetime import datetime
import random

class sensor_Data:
    @staticmethod
    def fetch(min, max):
        """ for now we are generating temperature data randomly """
        # fetching the current time
        time = datetime.now().strftime("%H:%M:%S")

        # updating temperature value as random numbers between 32 and 37
        data = str(random.randrange(min, max)) + " C"

        temp = {}
        temp.update({'currTime':str(time)})
        temp.update({'temperature':str(data)})

        return temp