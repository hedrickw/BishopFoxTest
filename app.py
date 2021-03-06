"""Module that runs application for uploading nmap result files and viewing the parsed results."""
from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from load_nmap_results import parse_nmap_xml_file, insert_nmap_result

app = Flask(__name__)
app.config.from_json("config.json")
db = SQLAlchemy(app)


class ExtractResults(db.Model):
    """Class Reperesenting database table that stores parsed nmap results."""

    __table_args__ = (
        db.UniqueConstraint('ip_address', 'port_id', name='unique_ip_address_to_port'),
    )

    result_id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(255))
    ip_type = db.Column(db.String(255))
    hostname = db.Column(db.String(255))
    port_id = db.Column(db.String(255))
    port_protocol = db.Column(db.String(255))
    state = db.Column(db.String(255))
    reason = db.Column(db.String(255))
    reason_ttl = db.Column(db.String(255))
    service_name = db.Column(db.String(255))
    service_method = db.Column(db.String(255))
    service_conf = db.Column(db.String(255))
    start_time = db.Column(db.DateTime)
    stop_time = db.Column(db.DateTime)


@app.route('/')
def homepage():
    """Return homepage of the application."""
    return render_template('homepage.html')


@app.route('/results')
def results():
    """Return nmap file results."""
    ip_address = request.args.get("ip_search")
    if ip_address:
        results = ExtractResults.query.filter(
            ExtractResults.ip_address.like(f'{ip_address}%'))
    else:
        results = ExtractResults.query.all()
    return render_template('results.html', results=results)


@app.route('/file_upload', methods=['GET'])
def get():
    """Return page that allows user to upload a nmap results file."""
    return render_template('load_file.html')


@app.route('/submit_file', methods=['POST'])
def post():
    """From a nmap file uploaded, parse the file and redirect to results page."""
    if not request.files:
        raise Exception("No file uploaded")

    file = request.files["extract_file"]
    if file.mimetype not in ('text/xml'):
        raise Exception("File uploaded must be an xml file")

    with db.engine.connect() as db_conn:
        db_conn.execute("DELETE FROM extract_results")
        results = parse_nmap_xml_file(file.stream)
        insert_nmap_result(results, db_conn)
    return redirect(url_for('results'))


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True)
