# BishopFox Interview Project

Simple web application that allows a single nmap xml result file to be uploaded, parsed and shown in a web view

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

OS Supported
```
Mac OS version 10.14
Ubuntu version 16.04
```
Python Version Supported
```
Python 3.6
```
### Installing

Clone repository to local computer.

```
git clone https://github.com/hedrickw/BishopFoxTest.git
```

Change directory to BishopFoxTest.
```
cd BishopFoxTest
```

Install python modules needed for the application, these are defined in the [requirements.txt](requirements.txt) file.

```
python3.6 -m pip install -r requirements.txt --user
```

## Running the Applications

### Web Application
Start up application by running app.py.
```
python3.6 app.py
```

Open browser of your choice go to url listed below.

```
http://localhost:5000
```
This will the display application home page which can guide you to file upload and results pages.

### File Parser
In BishopFoxTest directory, run load_nmap_results.py
```
python3.6 load_nmap_results.py --nmap-file nmap.results.xml 
```

This will print the parsed file results to stdout.

## Built With

* Flask - The web framework used
* sqlite - Database system used
* Flask-SqlAlchemy - ORM framework used - http://flask-sqlalchemy.pocoo.org/2.3/

# Authors

* **Wesley Hedrick** 


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## File Format Choice Reasoning
I chose the XML file format due to its ease of use with the python language. There is support for parsing xml files and strings in the standard libary of python.

## Assumptions
1. Number of hostnames per host is less than two.
2. Application is allowed to run in debug mode to ignore Cross Site Scripting management.
3. Uploaded records do not need to be saved, records are purged every upload and on application restart.
4. Port 5000 is allowed to be used to run the application.
5. Size of the files uploaded are not very large.
