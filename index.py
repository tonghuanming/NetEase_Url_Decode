# -*- coding:utf-8 -*-
from bottle import Bottle, request, run
from bottle import template, static_file, redirect
from bae.core.wsgi import WSGIApplication
from netEaseapi import get_url

app = Bottle()


@app.route('/css/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='./views/')


@app.route('/music', method=['GET', 'POST'])
def decode_music():
    if request.method == 'GET':
        text = ''
    else:
        m_url = request.POST.get('music_url')
        text = get_url(m_url)
        redirect(text)
    return template('index', text=text)


# if __name__ == '__main__':
#     run(app, host='127.0.0.1', port=8080, reloader=True)
application = WSGIApplication(app)
