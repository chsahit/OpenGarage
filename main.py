import Adafruit_BBIO.GPIO as GPIO
input = "P8_12"
def main():
	last_state = 0
	GPIO.setup(input,GPIO.IN)
	while True:
		curr_state = GPIO.input(input)
		if curr_state != last_state:
			print "status change"
		last_state = curr_state

if __name__ == "__main__":
	main()
