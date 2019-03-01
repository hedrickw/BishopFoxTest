import tornado.ioloop
import tornado.web
from nmap_import import NMapImportHandler


def make_app():
    return tornado.web.Application([
        (r"/import", NMapImportHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
