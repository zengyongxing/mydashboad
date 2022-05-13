#!/usr/bin/env Python
# coding=utf-8

from url import url
import tornado.ioloop
import tornado.web
import os


from tornado.options import define, options
define("port", default = 80, help = "web server on this port", type = int)

settings = dict(
    tempalte_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__), "statics")
    )



if __name__ == "__main__":
    options.parse_command_line()

    app = tornado.web.Application(handlers=url,**settings)
    app.listen(options.port)
    # tornado.ioloop.IOLoop.current().start()
    print(f"Server listen on :{options.port}")    

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
    finally:
        tornado.ioloop.IOLoop.instance().stop()
        tornado.ioloop.IOLoop.instance().close(True)
    print("Server shut down, exiting...")    