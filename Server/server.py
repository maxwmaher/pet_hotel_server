import flask
import psycopg2
from flask import request, jsonify, make_response

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello from Max and Declan's Awesome Python Server!</h1>"


@app.route('/api/pets/all', methods=['GET'])
def api_all():
    connection = psycopg2.connect(user="maxmaher",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
    cursor = connection.cursor()
    postgreSQL_select_Query = "SELECT * FROM pets"
    cursor.execute(postgreSQL_select_Query)
    pets = cursor.fetchall()
    return jsonify(pets)


app.run()
