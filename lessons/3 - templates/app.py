#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Hello, World! from Tornado Documentation
# https://www.tornadoweb.org/en/stable/
# 
#
import tornado.ioloop
import tornado.web
import asyncio

from os.path import join, realpath, dirname
import json



## Variables for Application
PORT = 8888
DEBUG = True

## Paths
APP_PATH = dirname(realpath(__file__))
TEMPLATE_PATH = join(APP_PATH, 'templates')
STATIC_PATH = join(APP_PATH, 'static')

if DEBUG == True:
    print("Application Path: ", APP_PATH)
    print("Template Path: ", TEMPLATE_PATH)
    print("Static Path: ", STATIC_PATH)

## Handler
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("example.html", title="Sample", items=items)


## WebController Application Class
##   This is used to make changing settings easier and high-levels of customising the settings
##    that make the application run.
class WebApp(tornado.web.Application):
    def __init__(self):
        ## Set up all the application customised settings here for the webserver.  This is
        ##  easier than having seperate variables to pass in.

        ## Settings
        settings = {
            "template_path": TEMPLATE_PATH,
            "static_path": STATIC_PATH,
            "static_url_prefix" : "/static/",
            "debug": True,
            "autoreload" : True        
        }

        ## Handlers
        handlers = [
            #(r"/static/(.*)", web.StaticFileHandler, {"path": self.static_file_path}),
            (r"/", MainHandler),
        ]

        ## Initialise the Application
        super().__init__(handlers, **settings)

    def start(self, port=8888):
        ''' Start the tornado webserver. '''
        asyncio.set_event_loop(asyncio.new_event_loop())
        print(port)
        self.port = int(port)
        self.listen(self.port)
        tornado.ioloop.IOLoop.instance().start()     
        


## Run this when the file is openned.
if __name__ == "__main__":
    app = WebApp()
    app.start(PORT)
