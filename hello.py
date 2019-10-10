from flask import Flask
from flask import request
from flask import *
import jaydebeapi as jdbc
import cx_Oracle


app = Flask(__name__)

@app.route('/')
def login():
   return render_template("Login.html")
   # return render_template("hyd.html")


@app.route('/hello/<name>')
def hello_world_new(name):
   return "Hello World" + name

@app.route('/hyd', methods=['GET','POST'])
def hyd():
   if(request.method=='POST'):
      user = request.form['user']
      passw = request.form['passw']
      if(user=='a' and passw=='a'):
         return render_template('hyd.html')
         # print("Outh!!")
         # return("AAAA")
      else:
         return("Login Failed!!")

@app.route('/hyd_data', methods=['GET','POST'])
def hyd_data():
   if(request.method=='POST'):
      table = request.form.get('table')
      rows = request.form.get("rows")
      data = database_re(table,rows)
      return render_template('hyd_data.html', data=data)

         # return render_template('hyd.html')
         # print("Outh!!")

def database_re(table,rows):


# connection = cx_Oracle.connect("orcl", 'B1259', "jdbc:oracle:thin:@192.168.63.144:1521:orcl", encoding="UTF-8")

   conn_str = u'B1259/B1259@192.168.63.144:1521/orcl'
   connection = cx_Oracle.connect(conn_str)

   cur = connection.cursor()
   cur.execute("SELECT * from " + table)
   col = cur.fetchall()
   cur.close()
   connection.close()
   return col



if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)

    # app.run()