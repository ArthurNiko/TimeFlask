from urllib import parse
from flask import Flask
from datetime import datetime
import argparse
import requests

app = Flask(__name__)


@app.route('/')
def time():
	response = requests.get('http://timeservice:8000/Logger.txt')
	return response.text

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--listen", default="0.0.0.0",)
	parser.add_argument("-p", "--port", type=int, default=8001,)
	args = parser.parse_args()
	
	app.run(host=args.listen, port=args.port)