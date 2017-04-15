from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import requests
import urllib2
from datetime import date
import json
from django.http import JsonResponse
import paho.mqtt.client as mqtt
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File


# Create your views here.


def staffindex(request):
    return render(request,'stafflogin.html',context={})


def staffregister(request):
    return render(request,'staffregister.html',context={})


def dash(requset):
    if requset.user.is_authenticated():
        responce = render(requset,'dashboard.html',context={})
    else:
        responce = redirect('/stafflogin')
    return responce


def getflightstatus(request,airport,airline_code,airline_no):
    flight_data = {}
    flight_data['airport'] =  airport
    flight_data['adi'] = "1"
    flight_data['otherAirport'] = ""
    flight_data['airlineCode'] = airline_code
    flight_data['FlightNo'] = ""
    flight_data['OperationDate'] = (date.today()).strftime("%d-%b-%Y")
    resp = requests.post("http://airsewa.gov.in/api/Web/AKS_GetFlightStatus", data= flight_data)
    return HttpResponse(resp.text)



@csrf_exempt
def sos(request):
    if request.is_ajax():
        topic = request.POST.get("topic")
        message = request.POST.get("message")

        def on_connect(self,client,userdata,flags,rc):
            print("Connected with result code " + str(rc))

        def on_message(client, userdata, msg):
            print(msg.topic+" "+str(msg.payload))

        client = mqtt.Client()
        client.publish(topic,payload=message)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("139.59.79.221", 1883, 60)
        client.publish(topic,message)
        return HttpResponse("OK")
    else:
        return HttpResponse("Not ajax")


def airportservice(requset,airport):
    data = {}
    data['airport'] = airport
    resp = requests.post("http://airsewa.gov.in/api/Web/GetAirportServiceInfo_Web", data=data)
    return HttpResponse(resp.text)

def olaservice(request,lat,long,cat):
    url = "http://sandbox-t.olacabs.com/v1/products?pickup_lat="+lat+"&pickup_lng="+long
    r = requests.get(url,headers={"X-APP-TOKEN": "17a3091837974c4b8c6999626992f2dc"})
    return HttpResponse(r.text)

@csrf_exempt
def getUser(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        userObj = authenticate(username= username,password= password)
        if userObj is not None:
            login(request,userObj)
            responce = HttpResponse("OK")
        else:
            responce = HttpResponse("Something wrong with user credentials")
    else:
        responce = HttpResponse("Not Ajax")
    return  responce


def stafflogout(request):
    logout(request)
    return redirect('/stafflogin')

def faqlist(request):
    r = requests.post("http://airsewa.gov.in/api/faq/faqlist", data={"code": 1})
    return HttpResponse(r.text)

@csrf_exempt
def notifyuser(request):
    message = request.POST.get("message")
    def on_connect(self,client,userdata,flags,rc):
        print("Connected with result code " + str(rc))
    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("139.59.79.221", 1883, 60)
    client.publish("del/update",message)
    return HttpResponse("OK")

