from flask import Flask, request, jsonify,make_response
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from sqlalchemy import true
import sys
from time import strftime,localtime
sys.path.insert(1, '/server2')
import logic

app = Flask(__name__)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
cors = CORS(app)


@app.route("/receiver", methods=["POST"])
def postME():
   json_file = request.form
   response=logic.logic_response(json_file)
   response.mimetype="text/plain"
   json_file=json_file.to_dict()
   
   json_file['time']=strftime("%a, %d %b %Y %X", localtime())
   temp= response.get_data(str)
   json_file['response']=temp
   db.collection('user_input').document().set(json_file)

   return response

if __name__ == "__main__": 
   app.run(debug=true)