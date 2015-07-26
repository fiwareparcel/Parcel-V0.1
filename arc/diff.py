import hashlib
ant=0
while True:
        while ant!=(hashlib.md5(open('/home/pi/parcel/arc/1-01.csv','rb').read()).hexdigest()):
                ant=(hashlib.md5(open('/home/pi/parcel/arc/1-01.csv','rb').read()).hexdigest())
                print "Hubo cambios"

