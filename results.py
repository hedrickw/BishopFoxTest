import tornado.web
from tornado import gen
from db import get_nmap_results
import json


class ResultsHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.write(json.dumps(get_nmap_results(self.application.db_connection)))
