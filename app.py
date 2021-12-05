from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)
db = yaml.safe_load(open(r'C:\Users\adity\Documents\vijay\flaskBasic\db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['nm']
      curr=mysql.connection.cursor()
      curr.execute("INSERT into reg_table2(name) VALUES(%s)", [result])
      mysql.connection.commit()
      curr.close()
   return render_template("list.html")

if __name__ == '__main__':
   app.run(debug = False)
