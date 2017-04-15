# -*- coding:utf-8 -*-

import os
from bottle import route, run, template

@route("/")
def index():
        return template('index')

@route("/<names>")
def others(names):
        return template('404', names=names)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
