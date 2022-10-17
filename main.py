from flask import Flask, Response, render_template, jsonify, send_file, url_for
import cv2
import os
import sys
import random


PEOPLE_FOLDER = os.path.join('static', 'imgs')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER



def get_img():
    
    ## get the img dir (also could preform on a server)
    ## fix the path string
    ## join the path name we wish to
    ## as of right now works with a random choice

    img_list = os.listdir('./static/imgs')
    img_list.pop()
    img_list_f = fix_paths(img_list)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'],random.choice(img_list_f))
    return full_filename

def fix_paths(paths):

    # fix path problem #
    for path in paths:
        path.replace(path[0] , "")
    return paths


# @app.route('/')
# @app.route('/index')
# def app_index():
#     ##### Detect Object in a Stack ######
#     # Main app #
#     image = get_img()
#     print(image, file=sys.stderr)
#     return render_template('ui.html', url_for())

# def gen():
#     while True:
#         yield(b'--frame\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(gen(), minetype='multipart/x-mixed-replace; boundrey=frame')

@app.route('/')
def index():
    # msg = str(a.Location[:])
    return render_template('ui.html', msg = 'Welcome to RS-APP')


def gen():
    while True:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' +  b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')






if __name__ == "__main__":
    app.run(debug=True, host= '0.0.0.0', port= 5000)