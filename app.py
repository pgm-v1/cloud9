# -*- coding:utf-8 -*-

import os
from bottle import route, run, template, error

@route("/")
def index():
        return template('index')

@error(404)
def error404(error):
    return "Not Found!"

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
