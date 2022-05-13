#!/usr/bin/env Python
# coding=utf-8
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")