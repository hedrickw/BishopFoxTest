import tornado.web
from tornado import gen
import xml.etree.ElementTree as element_tree
from db import insert_nmap_result
from db import delete_records


class NMapImportHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def post(self):
        delete_records(self.application.db_connection)
        body = self.request.files["data"][0]["body"]
        root = element_tree.fromstring(body)
        parse_nmap_xml_file(root, self.application.db_connection)
        self.write("Success!")


def parse_nmap_xml_file(root, db_connection):
    hosts = root.findall("host")
    for host in hosts:
        address = host.find('address')
        hostname = host.find('hostnames/hostname')
        # times = host.find('times')
        ports = host.findall('ports/port')
        for port in ports:
            nmap_store = {}
            find_ip_address_info(address, nmap_store),
            find_hostname_info(hostname, nmap_store),
            find_port_info(port, nmap_store)
            try:
                insert_nmap_result(nmap_store, db_connection)
            except Exception as e:
                raise Exception("Error in DB")
                return


def find_ip_address_info(address, nmap_store):
    nmap_store["ip_address"] = address.get("addr")
    nmap_store["ip_type"] = address.get('addrtype')
    return nmap_store


def find_hostname_info(hostname, nmap_store):
    if hostname is not None:
        nmap_store["hostname"] = hostname.get('name')
        return nmap_store
    nmap_store["hostname"] = None
    return nmap_store


def find_port_info(port, nmap_store):
    nmap_store["port_id"] = port.get("portid")
    nmap_store["port_protocol"] = port.get("protocol")
    find_state_info(port, nmap_store)
    find_service_info(port, nmap_store)
    return nmap_store


def find_state_info(port, nmap_store):
    state = port.find("state")
    nmap_store["state"] = state.get("state")
    nmap_store["reason"] = state.get("reason")
    nmap_store["reason_ttl"] = state.get("reason_ttl")


def find_service_info(port, nmap_store):
    service = port.find("service")
    nmap_store["service_name"] = service.get("name")
    nmap_store["service_method"] = service.get("method")
    nmap_store["service_conf"] = service.get("conf")
