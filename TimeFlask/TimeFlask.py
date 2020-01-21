from urllib import parse
from flask import Flask
from datetime import datetime
import argparse
import requests

app = Flask(__name__)

@app.route('/')
def time():
	now = datetime.now()
	current_time = now.strftime("Current Time: %H:%M:%S, %D")
	serverlogs = open("Logger.txt","a+")
	serverlogs.write(current_time + "<br>")
	serverlogs.close()
	return current_time

@app.route('/Logger.txt')
def logs():	
	serverlogs = open("Logger.txt")
	logs = serverlogs.read()
	serverlogs.close()
	return logs

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--listen", default="0.0.0.0",)
	parser.add_argument("-p", "--port", type=int, default=8000,)
	args = parser.parse_args()
	
	app.run(host=args.listen, port=args.port)