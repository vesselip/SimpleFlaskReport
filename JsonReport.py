from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
import json
import os
from json2xml import json2xml_file
from report_generator import create_pdf_file


db = SQLAlchemy()

from models import *
from database import init_db

def create_app():
    app = Flask(__name__)
    #app.config['SECRET_KEY'] = 'F34TF$($e34D'
    #DB_URL = postgresql://user:pass@candidate.suade.org/suade:5432/suade set through environment and config = config.DevelopmentConfig
    #app.config.from_object(os.environ['APP_SETTINGS'])

    @app.route('/', methods=['GET', 'POST'])
    def index():
        errors = []
        results = {}
        if request.method == "POST":
            # get url that the user has entered
            try:
                report_id = request.form['report_id']
                init_db()
                get_data(report_id)
            except:
                errors.append(
                    "Unable to retrieve data."
                )
        return render_template('index.html', errors=errors, results=results)
    return app

#get data for report id
def get_data(report_id):
    data = Reports.query.filter(Reports.id == int(report_id)).first()
    json_data = json.loads(data.type)

    if json_data:
        create_pdf_file(json_data)
        json2xml_file(json_data)

if __name__ == '__main__':
    create_app().run(debug=True)