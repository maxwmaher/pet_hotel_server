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
    postgreSQL_select_Query = 'SELECT "pets"."id", "pets"."name", "breed", "color", "checked_in", "owners"."name" FROM pets JOIN "owners" ON"owners".id = "pets".owner_id;'
    cursor.execute(postgreSQL_select_Query)
    pets = cursor.fetchall()
    return jsonify(pets)

@app.route('/api/owners/all', methods=['GET'])
def api_all_owners():
    connection = psycopg2.connect(user="maxmaher",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
    cursor = connection.cursor()
    postgreSQL_select_Query = 'SELECT "owners"."id", "owners"."name", count("pets".owner_id) FROM "owners" JOIN "pets" ON "pets"."owner_id" = "owners"."id" GROUP BY "owners"."id";'
    cursor.execute(postgreSQL_select_Query)
    pets = cursor.fetchall()
    return jsonify(pets)


@app.route('/api/owners/add', methods=['POST'])
def api_add_owner():
    name = request.form['name']
    try:
        connection = psycopg2.connect(user="maxmaher",
                                    password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="pet_hotel")
        cursor = connection.cursor()
        print(name, "Owner name")
        insertQuery = "INSERT INTO owners (name) VALUES (%s);"
        cursor.execute(insertQuery, (name,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Owner inserted")
        result = {'status': 'CREATED'}
        return make_response(jsonify(result), 201)
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("failed to insert owner", error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


@app.route('/api/pets/add', methods=['POST'])
def api_post_pet():
    print('Getting this far')
    owner_id = request.form['owner_id']
    print('Owner ID is', owner_id)
    name = request.form['name']
    print('Name is', name)
    breed = request.form['breed']
    color = request.form['color']
    checked_in = request.form['checked_in']

    print(owner_id, name, breed, color, checked_in)
    try:
        connection = psycopg2.connect(user="maxmaher",
                                      password="123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="pet_hotel")
        cursor = connection.cursor()
        print(owner_id)
        query = "INSERT INTO pets (owner_id, name, breed, color, checked_in) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (owner_id, name, breed, color, checked_in,))
        connection.commit()
        count = cursor.rowcount
        print(count, "pet added")
        result = {'status': 'CREATED'}
        return make_response(jsonify(result), 201)
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert book", error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

@app.route('/api/pets/delete', methods=['DELETE'])
def api_pet_delete():
    id = request.form['id']
    print(id)
    try:
        connection = psycopg2.connect(user="dmjbernardin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="pet_hotel")

        cursor = connection.cursor()
        print(id)
        insertQuery = "DELETE FROM pets WHERE id = %s;"
        cursor.execute(insertQuery, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "deleted")
        result = {'status': 'DELETED'}
        return make_response(jsonify(result), 200)
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to DELETE", error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


@app.route('/api/owner/delete', methods=['DELETE'])
def api_owners_delete():
    id = request.form['id']
    print(id)
    try:
        connection = psycopg2.connect(user="dmjbernardin",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="pet_hotel")

        cursor = connection.cursor()
        print(id)
        insertQuery = "DELETE FROM owners WHERE id = %s;"
        cursor.execute(insertQuery, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "deleted")
        result = {'status': 'DELETED'}
        return make_response(jsonify(result), 200)
    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to DELETE", error)
            result = {'status': 'ERROR'}
            return make_response(jsonify(result), 500)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

app.run(debug=True)
