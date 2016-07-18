from django.http import HttpResponse
import serial
import json


def sendPrice(request, value, price):
    if request.method == 'GET':
        try:
            prod = str(value)
            pr = str(price)
            blanks = "    "
            result = value + blanks + pr
            port = "COM2"
            baud = 9600
            ser = serial.Serial(port, baud, timeout=1)
            if ser.isOpen():
                ser.write(result.encode('ascii') + '\r\n')
                ser.close()
                return HttpResponse(json.dumps({'ack': '1'}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'ack': '0'}), content_type="application/json", status=400)
        except Exception as e:
            return HttpResponse(json.dumps(e.args), content_type="application/json", status=400)
