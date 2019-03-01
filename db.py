import sqlite3


SQL_CREATE_NMAP_RESULTS_TABLE = """
CREATE TABLE nmap_results
(
    ip_address text,
    ip_type text,
    hostname text,
    port_id text,
    port_protocol text,
    state text,
    reason text,
    reason_ttl text,
    service_name text,
    service_method text,
    service_conf text,
    UNIQUE(ip_address,port_id)
)
"""

SQL_INSERT_RECORD = """
INSERT INTO nmap_results(
    ip_address,ip_type,hostname,port_id,port_protocol,state,reason,reason_ttl,service_name,service_method,service_conf
)
VALUES(:ip_address,:ip_type,:hostname,:port_id,:port_protocol,:state,:reason,:reason_ttl,:service_name,:service_method,:service_conf)
"""

SQL_DELETE_RECORDS = """
DELETE FROM nmap_results;
"""


def create_database():
    connection = sqlite3.connect('bishopfox.db')
    return connection


def spin_up_tables(db_connection):
    # Create table
    with db_connection:
        db_connection.execute(SQL_CREATE_NMAP_RESULTS_TABLE)


def insert_nmap_result(nmap_result, db_connection):
    with db_connection:
        db_connection.execute(SQL_INSERT_RECORD, nmap_result)


def get_nmap_results(db_connection):
    with db_connection:
        cursor = db_connection.cursor()
        cursor.execute("SELECT * from nmap_results")
        results = cursor.fetchall()
    return results


def delete_records(db_connection):
    with db_connection:
        db_connection.execute(SQL_DELETE_RECORDS)
