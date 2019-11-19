#Figure out the degrees between an hour and a minute hand of a given time
#Known issues:
#Does not account for movement of hour hand throughout the hour
#Positive angle means minute hand has not yet passed hour hand
#Negative angle means minute hand has passed hour hand
#If you wanted just angle, not +/-, could take absolute -- abs() -- of number
hourHand = input("What hour is it? ")
minuteHand = input("What minute is it? ")
hourHandInt = int(hourHand)
minuteHandInt = int(minuteHand)
hourHandAngle = 0
minuteHandAngle = 0

if hourHandInt == 12:
    hourHandAngle = 0
else:
    hourHandAngle = hourHandInt*(360/12)
if minuteHandInt == 0:
    minuteHandAngle = 0
else:
    minuteHandAngle = minuteHandInt*(360/60)
print("The angle between the hour hand and minute hand at " + hourHand + ":" + minuteHand + " is " + str(hourHandAngle-minuteHandAngle))