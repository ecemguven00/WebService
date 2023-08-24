from flask import Flask, Blueprint
from waitress import serve
from datetime import datetime
import logging

from ForecastingModule import view as forecasting_view

if __name__ == '__main__':
    PATH = '.\logs\\'  
    LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
    FILE_NAME = '{:%Y-%m-%d_%H-%M-%S}.log'.format(datetime.now())

    logging.basicConfig(level=logging.INFO, filename=PATH + FILE_NAME, filemode='w', format=LOG_FORMAT, datefmt=DATE_FORMAT)

    app = Flask(__name__, static_folder=None)

    app.register_blueprint(forecasting_view)

    serve(app, host='0.0.0.0', port=5000, threads=10, connection_limit=250)