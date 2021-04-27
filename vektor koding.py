import math
import numpy as np

def koordinat():      #lager et random koordinat
    longnitue = (str(randint(0,90)) + "," + str(randint(1000,1000000)))
    latitude = (str(randint(0,180)) + "," + str(randint(1000,1000000)))
    return longnitue+'  '+latitude

           # lat_a = gps.location.lat()  #trenger bare dette en gang, siden vi i slutten av gpssteering definerer vi p_b som den nye p_a
           # lng_a = gps.location.lng()

p_c = np.array([69.931771, 52.321540])  # punktet vi skal til. vi mestemmer koordinatene på forrhånd.
p_a = np.array([13.481113, 18.850666]) #punktet vi var på sist (posisjonsvektor)
p_b = np.array([21.358110, 19.730161])            #p_b=(gps.location.lng()), gps.location.lat()) #punktet vi er på nå. (posisjonsvektor)


def magnitude(vector):
    return math.sqrt(sum(pow(element, 2) for element in vector))


def gpssteering():
    #a_c = np.subtract(p_c,p_a)  #gir oss vektoren AC
    a_b = np.subtract(p_b,p_a)  #gir oss AB  ((så ma vi finne vinkelen mellom AB Og bC for å finne vinkelen båten må snu fra B til C
    b_c = np.subtract(p_c,p_b)
    angle = math.degrees(math.acos(np.dot(b_c,a_b)/((magnitude(b_c))*(magnitude(a_b)))))
    print(angle)

gpssteering()
