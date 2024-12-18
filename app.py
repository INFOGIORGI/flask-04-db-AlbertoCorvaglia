from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
#138.41.20.102
#53306
#w3schools
#ospite
#ospite

'''
Home page
Products visualizza tutti i prodotti nella tabella products
rendere cliccabile category id che porta ad una pagina contente il dettaglio della categoria, serve la tabella category
'''

app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'


mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('index.html',titolo="HomePage")

@app.route("/products")
def products():
    cursor = mysql.connection.cursor()

    query = "SELECT * FROM products"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    return render_template('products.html',titolo="Prodotti",data=data)

@app.route("/category/<int:categoryID>")
def category(categoryID):
    
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    data = cursor.fetchall()


    for t in data:
        if t[0]==categoryID:
            return render_template("category.html",categoryInfo=t)

    return render_template("category.html",categoryInfo=[])

app.run(debug=True)

