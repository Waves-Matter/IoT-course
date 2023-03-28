import time
import board
import math
from analogio import AnalogIn

analog_in = AnalogIn(board.A2)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536
    
def get_rez(voltage):
    return ( 1500 / ( (3.3 / voltage) - 1 ) )

def Average(lst):
    return sum(lst) / len(lst)


Temperature_array = []
number = 0


while True:
    voltage = get_voltage(analog_in)
    
    ref = 3300
    
    A1 = 3.354016 * 0.001
    B1 = 2.569850 * 0.0001
    C1 = 2.620131 * 0.000001
    D1 = 6.383091 * 0.00000001
    
    rez = get_rez(voltage)

    T = 1 / (A1 + B1 * math.log(rez / ref) + C1 * ((math.log(rez / ref) ** 2)) + D1 * ((math.log(rez / ref) ** 3)) )
    T_K = T - 273.15
    
    Temperature_array.append(T_K)
    number = number + 1
    
    if number>20:
        Temperature_array.pop(0)
        number = number - 1
    
    T_A = Average(Temperature_array)
    
    #print("Resistance: " + str(rez))
    #print("Temperature: " + str(round(T_A, 2)))
    
    print("(" + str(round(T_A, 2)) + ")")
    time.sleep(0.1)
 
