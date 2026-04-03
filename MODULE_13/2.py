import mariadb
from flask import Flask, jsonify

app = Flask(__name__)
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '150102',
    'database': 'airport_game'
}


def get_airport_info(icao):
    connection = mariadb.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    query = "SELECT name, iso_country FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result



@app.route('/airport/<icao>', methods=['GET'])
def airport(icao):
    icao = icao.upper()
    data = get_airport_info(icao)
    response = {
        "ICAO": icao,
        "Name": data['name'],
        "Location": data['iso_country']
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)