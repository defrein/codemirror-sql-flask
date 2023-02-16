# YEah
from flask_mysqldb import MySQL
from flask import Flask, render_template, url_for, request
import pandas as pd

# init app
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'data_mhs'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

# Fxn to Execute Query


def sql_executor(raw_query):
    c = mysql.connection.cursor()
    c.execute(raw_query)
    data = c.fetchall()
    return data


# routes


@app.route('/')
def index():
    results = pd.DataFrame([])
    return render_template('index.html', results=results)


@app.route('/process_query', methods=['GET', 'POST'])
def process_query():
    if request.method == 'POST':
        raw_query = request.form['raw_query']
        initial_results = sql_executor(raw_query)
        results = pd.DataFrame(initial_results)
    return render_template('index.html', raw_query=raw_query, results=results)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

# hello
