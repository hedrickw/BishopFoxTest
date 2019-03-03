# BishopFox Project

Simple web application that allows a single nmap result file to be uploaded, parsed and show in a web view

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

OS Supported
```
Mac OS 
Ubuntu 16.04
```
Python Version Supported
```
python3.6
```
### Installing

Clone repo to local computer

```
git clone https://github.com/hedrickw/BishopFoxTest.git
```

Change directory to BishopFoxTest
```
cd BishopFoxTest
```

Install python modules needed for the application defined in the requirements file

```
python3.6 -m pip install -r requirements.txt --user
```

## Running the application
Start up application by running app.py
```
python3.6 app.py
```

Open browser of your choice go to url listed below

```
http://localhost:5000
```

## Built With

* Flask - The web framework used
* sqlite - Database system used
* Flask-SqlAlchemy - ORM framework used - http://flask-sqlalchemy.pocoo.org/2.3/

# Authors

* **Wesley Hedrick** 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## File Format Choice Reasoning
I chose the XML file format due to its ease of use with the python language. There was no extra work required to figure out how to parse the file since the structure of the file was already predefined.

## Assumptions
1. Number of hostnames per host is less than two
2. Every upload removes the previous records uploaded
3. All calls could be synchronous
4. Port running on does not need to be configurable 
