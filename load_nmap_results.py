"""Module that handles extracting nmap results from nmap xml file."""
import sqlite3
import xml.etree.ElementTree as element_tree
import argparse

SQL_INSERT_RECORD = """
INSERT INTO extract_results(
    ip_address,
    ip_type,
    hostname,
    port_id,
    port_protocol,
    state,
    reason,
    reason_ttl,
    service_name,
    service_method,
    service_conf
)
VALUES(:ip_address,
       :ip_type,
       :hostname,
       :port_id,
       :port_protocol,
       :state,
       :reason,
       :reason_ttl,
       :service_name,
       :service_method,
       :service_conf)
"""


def insert_nmap_result(nmap_result, db_connection):
    """Insert nmap result records into database."""
    db_connection.execute(SQL_INSERT_RECORD, nmap_result)


def parse_nmap_xml_file(xml_file, db_connection):
    """Parse nmap xml file.

    1. First we need to parse the file and find all the hosts we ran against
    2. Find the IP address associated with the host
    3. Find the hostname associated with the host
    4. Find all the ports we ran the scan against
    5. For each port we found
       a. Create an empty dictionary which will serve as database record
       b. Map IP address details to dictionary
       c. Map hostname details to dictionary
       d. Map port, state and service details to dictionary
    6. Insert new record into db
    """
    root = element_tree.parse(xml_file)
    hosts = root.findall("host")
    for host in hosts:
        address = host.find('address')
        hostname = host.find('hostnames/hostname')
        ports = host.findall('ports/port')
        for port in ports:
            nmap_store = {}
            map_ip_address_info(address, nmap_store),
            map_hostname_info(hostname, nmap_store),
            map_port_info(port, nmap_store)
            insert_nmap_result(nmap_store, db_connection)


def map_ip_address_info(address, nmap_store):
    """Map IP address details to database record."""
    nmap_store["ip_address"] = address.get("addr")
    nmap_store["ip_type"] = address.get('addrtype')
    return nmap_store


def map_hostname_info(hostname, nmap_store):
    """Map hostname if there is one to database record."""
    if hostname is not None:
        nmap_store["hostname"] = hostname.get('name')
        return nmap_store
    nmap_store["hostname"] = None
    return nmap_store


def map_port_info(port, nmap_store):
    """Map port, state and service details to database record."""
    nmap_store["port_id"] = port.get("portid")
    nmap_store["port_protocol"] = port.get("protocol")
    map_state_info(port, nmap_store)
    map_service_info(port, nmap_store)
    return nmap_store


def map_state_info(port, nmap_store):
    """Map state details found in port element to database record."""
    state = port.find("state")
    nmap_store["state"] = state.get("state")
    nmap_store["reason"] = state.get("reason")
    nmap_store["reason_ttl"] = state.get("reason_ttl")


def map_service_info(port, nmap_store):
    """Map service details found in port element to database record."""
    service = port.find("service")
    nmap_store["service_name"] = service.get("name")
    nmap_store["service_method"] = service.get("method")
    nmap_store["service_conf"] = service.get("conf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--nmap-file', required=True,
                        help="Path to nmap xml extract")
    parser.add_argument('--db-file', required=True,
                        help="Path to database file")

    args = vars(parser.parse_args())
    db_connection = connection = sqlite3.connect(args["db_file"])
    with db_connection as db_conn:
        parse_nmap_xml_file(args["nmap_file"], db_connection)
