import Adafruit_BBIO.GPIO as GPIO
import simplejson
import requests
import config
input = "P8_12"
def main():
	last_state = 0
	GPIO.setup(input,GPIO.IN)
	url = 'https://api.sendhub.com/v1/messages/?username=%s&api_key=%s' %(config.username,config.api_key)
	payload = {
		"contacts" : config.contacts,
		"text": "status change"
	}
	headers = {"content-type" : "application/json"}
	while True:
		curr_state = GPIO.input(input)
		if curr_state != last_state:
			print "status change"
			if curr_state == 1:
				payload["text"] = config.message_pushed
			else :
				payload["text"] = config.message_released
			print requests.post(url,data=simplejson.dumps(payload),headers=headers)
		last_state = curr_state

if __name__ == "__main__":
	main()
