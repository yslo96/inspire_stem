from machine import Pin,I2C,ADC
import ssd1306

light_pin = Pin (26)
adc = ADC(light_pin)
light_intensity = adc.read_u16()
light = "light:" + str(light_intensity)

oled_width = 128
oled_height = 64

oled = ssd1306.SSD1306_12C(oled_width, oled_height, i2c)
 
oled.text(light, 10, 10)
oled.show()