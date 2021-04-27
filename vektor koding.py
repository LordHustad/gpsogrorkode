import math
import numpy as np

def koordinat():      #lager et random koordinat
    longnitue = (str(randint(0,90)) + "," + str(randint(1000,1000000)))
    latitude = (str(randint(0,180)) + "," + str(randint(1000,1000000)))
    return longnitue+'  '+latitude

           # lat_a = gps.location.lat()  #trenger bare dette en gang, siden vi i slutten av gpssteering definerer vi p_b som den nye p_a
           # lng_a = gps.location.lng()



p_c = vmath.Vector2(69.931771, 52.321540)  # punktet vi skal til. vi mestemmer koordinatene på forrhånd.
p_a = vmath.Vector2(13.481113, 18.850666) #punktet vi var på sist (posisjonsvektor)
p_b = vmath.Vector2(21.358110, 19.730161)            #p_b=(gps.location.lng()), gps.location.lat()) #punktet vi er på nå. (posisjonsvektor)

def gpssteering():
    #a_c = (p_c-p_a)  #gir oss vektoren AC
    a_b = (p_b-p_a)  #gir oss AB  ((så ma vi finne vinkelen mellom AB Og bC for å finne vinkelen båten må snu fra B til C
    b_c = (p_c-p_b)
    angle = float(math.acos((b_c*a_b)/((abs(b_c))*(abs(a_b))))
    return (str(angle))    #bruker den til å gi et rortuslag med servoen.

                   # if angle>180
                   #     float(angle)-180
                    #    p_p= p_a #lager nytt punkt. dette må skje til slutt
gpssteering()
