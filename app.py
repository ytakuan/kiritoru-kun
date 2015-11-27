# -*- coding: utf-8 -*-

import Image
import random

from bottle import route, run, template, request, static_file

host = ""
port = ""
images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

def make_image_path(image_name):
    return "./static/images/" + image_name

@route('/static/<filepath:path>')
def static(filepath):
    return static_file(filepath, root="./static")


@route('/', method='GET')
def index():
    # ランダムで対象を設定
    index = random.randint(0,4)
    image_path = make_image_path(images[index])
    return template('index.tpl', image=image_path, index=index)

@route('/crop', method='POST')
def crop():
    x = int(request.forms.get('x'))
    y = int(request.forms.get('y'))
    w = int(request.forms.get('w'))
    h = int(request.forms.get('h'))
    index = int(request.forms.get('index'))

    try:
        # ファイルを取得してトリミング
        image_path = make_image_path(images[index])
        img = Image.open(image_path)
        img = img.crop( (x, y, x+w, y+h) )

        # ファイル名はとりあえずランダムで
        cropped_filename = "tmp_" + str(random.randint(1,10000)) + ".jpg"
        cropped_image_path = make_image_path(cropped_filename)
        img.save(cropped_image_path, "JPEG")
    except IOError:
        print "Error"
   
    return template('crop.tpl', image=cropped_image_path)

run(host=host, port=port, debug=True, reloader=True)
