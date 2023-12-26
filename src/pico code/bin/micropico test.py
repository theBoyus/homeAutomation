from machine import Pin, ADC
from time import sleep


led = Pin("LED", Pin.OUT)
led.toggle()
lone_sense = ADC(Pin(27))
bigger_sense = ADC(Pin(28))
button = Pin(20, Pin.IN)

try:
    while True:
        if button.value():
            pass
        else:
            smol = lone_sense.read_u16()
            bigg = bigger_sense.read_u16()
            sleep(1)
            if smol > 64000:
                print("SMOL SAYS IT'S FUCKING BRIGHT OUT")
            if bigg < 500:
                print("BIGG SAYS IT'S FUCKING BRIGHT OUT")

except KeyboardInterrupt:
    print("Stopped")
