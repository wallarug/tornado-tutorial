#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Hello, World! from Tornado Documentation
# https://www.tornadoweb.org/en/stable/
# 
#
import tornado.ioloop
import tornado.web

## Variables for Application
PORT = 8888


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


## This example shows all the RequestHandler methods that can be overwriten.
##  It is only recommended to overwrite these if necessary.
class ConsoleHandler(tornado.web.RequestHandler):
    def initialize(self):
        pass

    def prepare(self):
        #pass
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def on_finish(self):
        pass

    def get(self):
        self.write("> ")

    def post(self):
        pass

    def put(self):
        pass


## Routing Table and Application Object
##  This is a routing table with a redirect and two other resources.
##  NOTE:  routes called in order.
app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/console", ConsoleHandler),
        (r"/google", tornado.web.RedirectHandler, dict(url="https://www.google.com.au")),
        ])

## Run this when the file is openned.
if __name__ == "__main__":
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
