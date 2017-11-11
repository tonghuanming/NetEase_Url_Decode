# -*- coding:utf-8 -*-
from bottle import Bottle, request, run
from bottle import template, static_file, redirect
from bae.core.wsgi import WSGIApplication
from netEaseapi import get_url
import re

app = Bottle()
pl_url = 'http://music.163.com/api/playlist/detail?id=%s'


@app.route('/tpl/<filename:re:.*\.css|.*\.jpg>')
def css(filename):
    return static_file(filename, root='./views/')


@app.route('/music', method=['GET', 'POST'])
def decode_music():
    if request.method == 'GET':
        music = ''
    else:
        m_url = request.POST.get('music_url')
        if m_url.find('playlist') is not -1:
            m_id = re.findall(r'\d+', m_url)[1]
            m_list = pl_url % m_id
            redirect(m_list)
        if m_url.find('song') is not -1:
            m_id = re.findall(r'\d+', m_url)[1]
            music = get_url(m_id)
            redirect(music)
    return template('index', music=music)


# if __name__ == '__main__':
#     run(app, host='127.0.0.1', port=8080, reloader=True)
application = WSGIApplication(app)
