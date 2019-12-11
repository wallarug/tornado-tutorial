#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Hello, World! from Tornado Documentation
# https://www.tornadoweb.org/en/stable/
# 
#
import tornado.ioloop
import tornado.web

## Handler - A class or function that responds to a request from a web browser.
##   This is used when someone goes to the website and serves the request.
##
##  Valid methods for this class are the HTTP protocol standards
##  GET     - retrieve data from server (idempotent)
##  POST    - send data to server
##  PUT     - send data to server (updates, idempotent)
##  DELETE  - deletes resource
##
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


## Set up a basic webserver
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

## Run this when the file is openned.
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
