from machine import Pin,i2C
import ssd1306

# ESP32 Pin assignment
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

oled_width = 128
oled_height = 64

oled = ssd1306.SSD1306_12C(oled_width, oled_height, i2c)
          
oled.text('temp:20,hum:65', 10, 10)
oled.show()