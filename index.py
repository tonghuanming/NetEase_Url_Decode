# -*- coding:utf-8 -*-
from bottle import Bottle, request, view
from bae.core.wsgi import WSGIApplication
from netEaseapi import get_url

app = Bottle()


@app.route('/music', method=['GET', 'POST'])
@view('index')
def decode_music():
    if request.method == 'GET':
        text = 'Input Music Url'
    else:
        m_url = request.POST.get('music_url')
        text = get_url(m_url)
    info = {'text': text}
    return info


application = WSGIApplication(app)
