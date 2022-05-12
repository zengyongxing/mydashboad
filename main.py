import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    # tornado.ioloop.IOLoop.current().start()
    print("Server listen on 8888:")    

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        pass
    finally:
        tornado.ioloop.IOLoop.instance().stop()
        tornado.ioloop.IOLoop.instance().close(True)
    print("Server shut down, exiting...")    