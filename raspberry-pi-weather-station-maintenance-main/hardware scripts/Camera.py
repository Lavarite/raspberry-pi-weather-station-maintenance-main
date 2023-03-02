from picamera import PiCamera
from time import sleep


def main():
    SERVER_URL = 'http://172.20.47.242:80/data'
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/tmp/picture.jpg')
    camera.stop_preview()
