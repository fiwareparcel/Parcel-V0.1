import csv
import hashlib
import os
from datetime import datetime, date, time

maximumSeconds = 5
minimumPower = -50 #Here define the power
maximumPower = 0

macIndex = 0
dateIndex = 1
powerIndex = 2

#h = 0
macsFile = '/home/pi/parcel/arc/filteredmacs.csv'
#lastInsert = datetime.now()

def readNewMacs():
	result = {}
	with open(macsFile) as csvFile:
		reader = csv.reader(csvFile)
		for row in reader:
			if row:
				try:
					result[row[0]] = row[0].replace(" ", "") + "," + row[1].replace(" ", "") + "," + row[2].replace(" ", "")
				except:
					print "Parcel"			


	return result


def endOfTheDay(currentDate):
	result = True
	if currentDate.day == datetime.now().day:
		result = False

	return result


def secondsFrom(date1, date2):
	dateDiff = abs(date1 - date2)
	return dateDiff.seconds


def isGoodEnough(date1, date2, power):
	result = False
	diff = secondsFrom(date1, date2)
	if diff > maximumSeconds and power < maximumPower and power > minimumPower:
		result = True

	return result


while True:
	print "Entro al DEBUG"

	oldMacs = {}
	freshMacs = {}
	deviceCounter = 0
	currentDate = datetime.now()

	#h = hashlib.md5(open(macsFile, 'rb').read()).hexdigest()

	while not endOfTheDay(currentDate):
		#print "No se acaba el dia"

		newMacs = readNewMacs()
		for key in newMacs:

			itemData = newMacs[key].split(",")
			# The mac is old enough, we know it
			if itemData[macIndex] in oldMacs:
				continue

			# A new mac, lets save it
			if itemData[macIndex] not in freshMacs:
				insertDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				freshMacs[key] = itemData[macIndex] + "," + insertDate + "," + itemData[powerIndex]
				lastInsert = datetime.now()
				continue

			# Otherwise, lets see if this mac is old enough
			previousRegister = freshMacs[key].split(",")
			previousRegisterDate = datetime.strptime(previousRegister[dateIndex], "%Y-%m-%d %H:%M:%S")
			currentDate = datetime.now()

			try:
				if isGoodEnough(previousRegisterDate, currentDate, int(itemData[powerIndex])):
					deviceCounter = deviceCounter + 1
					del freshMacs[key]
					oldMacs[key] = key
	
					print "mac registrada " + key
					print "Total de registrados " + str(deviceCounter) 
					os.system('curl -X GET "http://177.244.230.137:8002/iot/d?i=dev_1&d=source_data|'+str(deviceCounter)+'&k=apikey2" -i')
			except:
				print "parcel"

	
	#Needs to send the deviceCounter
	#Using the FIWARE API

'''
r = readNewMacs()
for ri in r:
	print r[ri]
'''

