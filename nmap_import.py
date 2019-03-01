import tornado.web
from tornado import gen
import xml.etree.ElementTree as ET
from db import insert_nmap_result
from db import create_database
from db import get_nmap_results
import json

class NMapImportHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):

        self.write(json.dumps(get_nmap_results()))

    @gen.coroutine
    def post(self):
        create_database()
        body = self.request.files["data"][0]["body"]
        root = ET.fromstring(body)

        hosts = root.findall("host")
        for host in hosts:
            address = host.find('address')
            hostname = host.find('hostnames/hostname')
            times = host.find('times')
            ports = host.findall('ports/port')
            for port in ports:
                nmap_blobs = {}
                nmap_blobs["ip_address"] = address.get("addr")
                nmap_blobs["ip_type"] = address.get('addrtype')
                if hostname is not None:
                    nmap_blobs["hostname"] = hostname.get('name')
                else:
                    nmap_blobs["hostname"] = None
                nmap_blobs["port_id"] = port.get("portid")
                nmap_blobs["port_protocol"] = port.get("protocol")
                state = port.find("state")
                nmap_blobs["state"] = state.get("state")
                nmap_blobs["reason"] = state.get("reason")
                nmap_blobs["reason_ttl"] = state.get("reason_ttl")
                service = port.find("service")
                nmap_blobs["service_name"] = service.get("name")
                nmap_blobs["service_method"] = service.get("method")
                nmap_blobs["service_conf"] = service.get("conf")
                insert_nmap_result(nmap_blobs)


def assign_address_info(address):
    pass


def assign_hostname_info(hostname):
    pass


def assign_ports_info(ports):
    pass


def assign_times(times):
    pass
