from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
from flask import make_response
import data
import json
import serving_logic

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True

identity = data.fetch_identity()

@app.route('/')
def something():
    response=make_response("I'm made of Redmatter.  My name is "+str(identity), 200)
    response.headers['Access-Control-Allow-Origin']= '*'
    return response

@app.route('/', methods=['POST'])
def redmatter():
    jsoninput=json.loads(request.data)

    jsonresponse = serving_logic.handle_redmatter_request(jsoninput)

    jsonresponse=json.dumps(jsonresponse)
    response=make_response(str(jsonresponse), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin']= '*'
    return response

def serve():
    app.run(host='0.0.0.0')
