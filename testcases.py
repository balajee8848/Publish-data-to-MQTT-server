from convertToJson import *
from configFileOps import *
from sensorData import *
import pytest

@pytest.fixture
def sensorData():
    return {"currTime":"12:00:00", "temperature":"32 C"}

#Test case to test whether convertToJson.get() method returns data as json
def test1_convertToJson(sensorData):
    assert convertToJson.get(sensorData) == '{\n    "time": "12:00:00",\n    "temperature": "32 C"\n}'

#Test case to test link is fetched properly or not from config file
def test2_configFileOps():
    temp = configFile.getProp(configFile.isPresent(), 'broker', 'link')

    confFile = configparser.ConfigParser()
    confFile.read("config.ini")

    assert temp == confFile['broker']['link']

#Test case to test portID is fetched properly or not from config file
def test3_configFileOps():
    temp = configFile.getProp(configFile.isPresent(), 'broker', 'portID')

    confFile = configparser.ConfigParser()
    confFile.read("config.ini")

    assert temp == confFile['broker']['portID']

#Test case to test logger level is fetched properly or not from config file
def test4_configFileOps():
    temp = configFile.getProp(configFile.isPresent(), 'logger', 'level')

    confFile = configparser.ConfigParser()
    confFile.read("config.ini")

    assert temp == confFile['logger']['level']

#Test case to verify that system exits when given option is not there in config file
def test5_configFileOps():
    with pytest.raises(SystemExit):
        configFile.getProp(configFile.isPresent(), 'logger', 'leve')

#Test case to verify that system exits when given section is not there in config file
def test6_configFileOps():
    with pytest.raises(SystemExit):
        configFile.getProp(configFile.isPresent(), 'boker', 'link')

@pytest.fixture
def temp():
    return sensor_Data.fetch()

#Test case to verify that sensor_data.fetch() method returns a dictionary
def test7_sensorData(temp):
    assert type(temp) == type({})

#Test case to verify that data from sensor_data.fetch() method has 'currTime' as key
def test8_sensorData(temp):
    assert temp.get('currTime') != None

#Test case to verify that data from sensor_data.fetch() method has 'temperature' as key
def test9_sensorData(temp):
    assert temp.get('temperature') != None