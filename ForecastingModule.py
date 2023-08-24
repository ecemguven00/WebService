import flask 
from flask import Blueprint, request, abort, Response
import logging
import sys
import json
sys.path.append("../")
from Prediction import predictionService

predictionService=predictionService()

view=Blueprint("Forecasting",__name__,url_prefix="/api/v1")

@view.route('/predictions',methods=['POST'])
def call_form():
    try:

        data = request.get_json()  # JSON formatındaki veriyi al
        image_base64 = data.get('image', '')  # JSON içindeki 'image' alanını al
        #data=request.get_json()['name']
        #predicted_data=predictionService.predict(data)
    except Exception as e :
        logging.error(e)
        abort(400)
    result=json.dumps({'prediction' : str("ecem")})
    logging.info("PredictionResult :  {}".format(result))
    return Response(result,mimetype="application/json")