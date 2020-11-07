from flask import Flask, render_template
import Adafruit_DHT as ad
from time import sleep
from threading import Thread

app = Flask(__name__)
PIN = 4
humidity = temperature = None


@app.route('/')
def hello_world():
    render_template("home.html", humidity=humidity, temperature=temperature)


def sensor():
    global humidity, temperature
    while True:
        humidity, temperature = ad.read(ad.DHT11, PIN)
        sleep(60)


if __name__ == '__main__':
    sensor_thread = Thread(target=sensor)
    sensor_thread.start()
    app.run()
