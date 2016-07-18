from django.http import HttpResponse
import serial
import json

def sendPrice(request, value):
    if request.method == 'GET':
        try:
            price = value
            port = "COM2"
            baud = 9600
            ser = serial.Serial(port, baud, timeout=1)
            if ser.isOpen():
             ser.write(price.encode('ascii')+'\r\n')
             ser.close()
             return HttpResponse(json.dumps({'ack':'1'}), content_type="application/json")
            else:
             return HttpResponse(json.dumps({'ack':'0'}), content_type="application/json", status=400)
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)

