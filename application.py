import logging
from flask import Flask, jsonify, render_template,request
import requests
import json
import subprocess

from flask import Flask, render_template
import subprocess
# import requests
# import json


# EB looks for an 'application' callable by default.
application = app = Flask(__name__)
myData="ALEX";
@app.route('/', methods=['POST'])
def loadpage():
	content = request.data
	app.logger.info(content)
	data=json.loads(content)["Message"]
	myData=data.split("$$delim1738352016$$")
	status=myData[0]
	lat=myData[1]
	lng=myData[2]
	feeling=myData[3]
	app.logger.info(myData)
	subprocess.call([
    	'curl',
    	'-X',
    	'POST',
    	'-d',
    	'{"status": "' + status + '","lat": ' + lat + ',"lng": ' + lng+ ',"feeling": "' + feeling + '"}',
    	#'search-minihw2-fdw6cbkvqwd3r6yvfvdvwws3yy.us-west-2.es.amazonaws.com/minihw2/tweets'
	#'search-minihw2-eeygwlzb7shc2n3qpk2aii4efy.us-east-1.es.amazonaws.com/minihw2/tweets'
	#'search-hwtwo-ihcx3rthxk64bxa56xznmc4c3i.us-east-1.es.amazonaws.com/hwtwo/tweets'
	'search-hwtwo-ihcx3rthxk64bxa56xznmc4c3i.us-east-1.es.amazonaws.com/hwtwo/tweets'
	])
	app.logger.info(myData)
	#parse through my data to get status, feeling, lat, lng (maybe $$delim1738352016$$ should be deliminator?)
	#ES Post: curl -XPOST search-minihw2-fdw6cbkvqwd3r6yvfvdvwws3yy.us-west-2.es.amazonaws.com/minihw2/tweets -d '{"status": "trump", "lat":90, "lng":90, "feeling":"Sad"}'
	#ES Get: https://search-minihw2-fdw6cbkvqwd3r6yvfvdvwws3yy.us-west-2.es.amazonaws.com/minihw2/_search?q=trump
	#make a post to ES with that 
	app.logger.info(feeling)
	return data

@app.route('/home')
def myLoad():
	return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	#app.run()
	#app.run(host = '0.0.0.0', port = 3000)
	app.run(host='0.0.0.0', debug=True, port=5000)
