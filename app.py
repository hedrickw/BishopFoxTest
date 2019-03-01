import tornado.ioloop
import tornado.web
from nmap_import import NMapImportHandler
from results import ResultsHandler
from db import create_database
from db import spin_up_tables
import argparse


def make_app():
    return tornado.web.Application([
        (r"/import_extract", NMapImportHandler),
        (r"/results", ResultsHandler)
    ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=8080, type=int,
                        help="Port to run app on")
    parser.add_argument('--create-tables', default=False, type=bool,
                        help="Flag for creating the database")

    args = vars(parser.parse_args())
    app = make_app()
    app.db_connection = create_database()
    if args["create_tables"]:
        spin_up_tables(app["db_connection"])
    app.listen(args["port"])
    tornado.ioloop.IOLoop.current().start()
