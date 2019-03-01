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


def create_database():
    conn = sqlite3.connect('bishopfox.db')
    c = conn.cursor()

    # Create table
    c.execute(SQL_CREATE_NMAP_RESULTS_TABLE)

    # Save (commit) the changes
    conn.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    conn.close()


def insert_nmap_result(nmap_result):
    conn = sqlite3.connect('bishopfox.db')
    c = conn.cursor()
    c.execute(SQL_INSERT_RECORD, nmap_result)
    conn.commit()
    conn.close()


def get_nmap_results():
    conn = sqlite3.connect('bishopfox.db')
    c = conn.cursor()
    c.execute("SELECT * from nmap_results")
    results = c.fetchall()
    conn.close()
    return results
