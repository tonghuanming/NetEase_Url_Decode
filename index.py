# -*- coding:utf-8 -*-
from bottle import Bottle, request, run
from bottle import template, static_file, redirect
from bae.core.wsgi import WSGIApplication
from netEaseapi import get_url
from urllib import urlretrieve
import re

app = Bottle()


@app.route('/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='./views/')


@app.route('/download/<filename:re:.*\.mp3>')
def css(filename):
    return static_file(filename, root='./music/')


@app.route('/music', method=['GET', 'POST'])
def decode_music():
    if request.method == 'GET':
        music = ''
    else:
        m_url = request.POST.get('music_url')
        m_id = re.findall(r'\d+', m_url)[1]
        music = get_url(m_id)
        urlretrieve(music, './music/temp.mp3')
        redirect('/music/temp.mp3')
    return template('index', music=music)


# if __name__ == '__main__':
#     run(app, host='127.0.0.1', port=8080, reloader=True)
application = WSGIApplication(app)
