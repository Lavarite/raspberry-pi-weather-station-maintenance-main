import time

# Checks right module is installed (could be either of these 2 options)
try:
	from smbus2 import SMBus
except ImportError:
	from smbus import SMBus
from bme280 import BME280

def main():
	# Initalise the BME280
	bus = SMBus(1)
	bme280 = BME280(i2c_dev=bus)
	for i in range(3): # Takes a couple of readings to 'warm up' (otherwise invalid readings collected)
		# Collects readings and applies appropraite callibration
		temperature = bme280.get_temperature() - 3
		pressure = bme280.get_pressure() + 10
		humidity = bme280.get_humidity() + 10
		time.sleep(1)

	return temperature, pressure, humidity
	