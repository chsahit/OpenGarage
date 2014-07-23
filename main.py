import Adafruit_BBIO.GPIO as GPIO
import simplejson
import requests
input = "P8_12"
def main():
	last_state = 0
	GPIO.setup(input,GPIO.IN)
	url = 'https://api.sendhub.com/v1/messages/?username=9088874698&api_key=2b2b92905ca9711e267610e98ed71da3c2b96359'
	payload = {
		"contacts" : ["+19088874698","+19086194012"],
		"text": "status change"
	}
	headers = {"content-type" : "application/json"}
	while True:
		curr_state = GPIO.input(input)
		if curr_state != last_state:
			print "status change"
			if curr_state == 1:
				payload["text"] = "garage opened"
			else :
				payload["text"] = "garage closed"
			requests.post(url,data=simplejson.dumps(payload),headers=headers)
		last_state = curr_state

if __name__ == "__main__":
	main()
