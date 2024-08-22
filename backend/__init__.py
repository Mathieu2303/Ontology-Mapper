from flask import Flask, request, jsonify
#from flask_cors import CORS
from config import CRITERIA_CONFIG 
import services

def create_app():
    print("Starting backend app")

    app = Flask(__name__)

    @app.route("/api/getcategory", methods=["GET"])
    def getDescription():
        descriptionsList = services.getAllDescriptions()
        return jsonify(descriptionsList)
        
           
        
    @app.route("/api/aiquery", methods=["POST"])
    def mrnQuery():
        body = request.get_json()
        response = services.mrnQuery(body)
       # print("reponse: ", response)
        return jsonify(response)

    return app
