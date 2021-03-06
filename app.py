#python_flask_opencv_video_streaming
#Author: Md. Nadimozzaman Pappo
#Company: GoonFol
#Inspired By: https://blog.miguelgrinberg.com/post/video-streaming-with-flask
#Source: https://github.com/goonfol/python_flask_opencv_video_streaming

from flask import Flask, render_template, Response
from camera import VideoCamera
import requests
from gevent.wsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def index():
    url = 'http://admin:Apekkhik@007@192.168.1.108/cgi-bin/configManager.cgi?action=getConfig&name=Encode'
    config = requests.get(url).content
    return render_template('index.html', config=config)


@app.route('/getinfo')
def getinfo():
    url = 'http://admin:Apekkhik@007@192.168.1.108/cgi-bin/configManager.cgi?action=getConfig&name=Encode'
    result = requests.get(url).content
    print(result)
    return result


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()

    app.run(host='0.0.0.0', port=1111, threaded=True, debug=True)
