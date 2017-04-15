import requests
import time
f = open('prev.txt','w')
f.write(" ")

while True:
	s = open('prev.txt','r')
	t = s.read()
	r = requests.post("http://airsewa.gov.in/api/Web/AKS_GetFlightStatus",data={"airport":"DEL","otherAirport":"","adi":"1","airlineCode":"SG","OperationDate":"02-Apr-2017","FlightNo":""})
	r = r.text
	if t == r:
		print "Koi nai"
	else:
		print "changed"
		f = open("prev.txt","w")
		f.write(r)
		requests.post("http://139.59.79.221:8000/notifyuser/",data={"message":r})
	time.sleep(5000)


