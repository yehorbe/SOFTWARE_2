from flask import Flask, jsonify
import mariadb

app = Flask(__name__)
connection = mariadb.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "150102",
    database = "flight_game",
    autocommit = True
)


def get_airport_info(connection, icao):
    cursor = connection.cursor(dictionary=True)
    sql = "SELECT name, iso_country FROM airport WHERE ident = %s"
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result



@app.route('/airport/<icao>', methods=['GET'])
def airport(icao):
    icao = icao.upper()
    data = get_airport_info(connection, icao)
    response = {
        "ICAO": icao,
        "Name": data['name'],
        "Location": data['iso_country']
    }
    return jsonify(response)

app.run(use_reloader=True, host='127.0.0.1', port=5000)