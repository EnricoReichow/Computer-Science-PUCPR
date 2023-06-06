"""
MicroPython IoT Weather Station Example for Wokwi.com

To view the data:

1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "wokwi-weather" then click "Subscribe"

Now click on the DHT22 sensor in the simulation,
change the temperature/humidity, and you should see
the message appear on the MQTT Broker, in the "Messages" pane.

Copyright (C) 2022, Uri Shaked

https://wokwi.com/arduino/projects/322577683855704658
"""

import network
import time
from machine import Pin
import dht
import ujson
from umqtt.simple import MQTTClient
from machine import I2C
import ssd1306

# MQTT Server Parameters
MQTT_CLIENT_ID = "micropython-weather-demo"
MQTT_BROKER    = "broker.mqttdashboard.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC     = "wokwi-weather"

sensor = dht.DHT22(Pin(15))

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

buzzer = PWM(Pin(27))
buzzer.freq(500)
buzzer.duty(0)

print("Conectando no WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print("Conectado!")

print("Conectando no MQTT server... ", end="")
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()

print("Conectado!")

prev_weather = ""
while True:
  # print("Measuring weather conditions... ", end="")
  # mensagem no oled de umidade e temperatura
  # fazer um if que se a a umidade tiver abaixo do esperado tocar a buzina e colocar "Regando no Oled"
  sensor.measure() 
  message = ujson.dumps({
    "Umidade": sensor.temperature(),
    "Temperatura": sensor.humidity(),
  })
         
  if sensor.temperature() >= 30 or sensor.humidity() <= 45:
    oled.fill(0)
    oled.text("Regando...", 0, 35)
    oled.show()
  else:
    oled.fill(0)    
    oled.text("Umidade: " + str(sensor.humidity()), 0, 15)
    oled.text("Temperatura: " + str(sensor.temperature()), 0, 45)
    oled.show()

  if message != prev_weather:
    print("Updated!")
    time.sleep(1)
    print("Reportando para MQTT: ".format(MQTT_TOPIC, message))
    client.publish(MQTT_TOPIC, message)
    prev_weather = message
  else:
    print("")
  time.sleep(1)
