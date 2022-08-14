import json

class convertToJson:
    @staticmethod
    def get(dataFromSensor):
        # creating the payload
        payload = '{"time":"' + dataFromSensor['currTime'] + '", "temperature":"' + dataFromSensor['temperature'] + '"}'
        #converting string to dict
        payload = json.loads(str(payload))
        #converting dict to json
        payload = json.dumps(payload, indent=4)

        return(payload)