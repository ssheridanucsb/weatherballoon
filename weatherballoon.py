from sense_hat import SenseHat
import time
import csv

fedora = SenseHat()
#main code for recording atmospheric conditions

fields = ['humidity', 'temp', 'temp_from_humidity', 'temp_from_pressure', 'pressure',
'orientation_pitch', 'orientation_roll', 'orientation_yaw', 'compass', 'gyro_pitch',
'gyro_roll', 'gyro_yaw', 'accelerometer_pitch', 'accelerometer_roll', 'accelerometer_yaw']

with open("atmosphere.csv", 'w') as atm:
    data_writer = csv.DictWriter(atm,  fieldnames=fields)
    data_writer.writeheader()

while(True):

    #enviornmental sensors
    humidity = fedora.get_humidity()
    temp = fedora.get_temperature()
    temp_from_humidity = fedora.get_temperature_from_humidity()
    temp_from_pressure = fedora.get_temperature_from_pressure()
    pressure = fedora.get_pressure()
    #get orientation
    orientation = fedora.get_orientation()
    orientation_pitch = orientation.get('pitch')
    orientation_roll = orientation.get('roll')
    orientation_yaw = orientation.get('yaw')

    #get compass
    compass = fedora.get_compass()

    #get gyroscope
    gyro = fedora.get_gyroscope()
    gyro_pitch = gyro.get('pitch')
    gyro_roll = gyro.get('roll')
    gyro_yaw = gyro.get('yaw')

    #get accelerometer
    accelerometer = fedora.get_accelerometer()
    accelerometer_pitch = accelerometer.get('pitch')
    accelerometer_roll = accelerometer.get('roll')
    accelerometer_yaw = accelerometer.get('yaw')

    #write to csv
    with open("atmosphere.csv", 'a') as atm:
        data_writer = csv.DictWriter(atm,  fieldnames=fields)
        data_writer.writerow({'humidity':humidity, 'temp':temp, 'temp_from_humidity':temp_from_humidity,
        'temp_from_pressure':temp_from_pressure, 'pressure':pressure,
        'orientation_pitch':orientation_pitch, 'orientation_roll':orientation_roll,
        'orientation_yaw':orientation_yaw, 'compass':compass, 'gyro_pitch':gyro_pitch,
        'gyro_roll':gyro_roll, 'gyro_yaw':gyro_yaw, 'accelerometer_pitch':accelerometer_pitch,
        'accelerometer_roll':accelerometer_roll, 'accelerometer_yaw':accelerometer_yaw})

    time.sleep(1)
