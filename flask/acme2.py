from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/acmeflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return self.name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(50),nullable=False )
    ref = db.Column(db.String(10), unique=True, nullable=False)
    price = db.Column(db.Numeric(6,2), nullable=False)
    category = db.relationship('Category')

    def __repr__(self):
        return self.name

# db.create_all()


@app.route('/')
def test():
    return "Homepage"

@app.route('/products')
def listProducts():
    categories = Category.query.order_by(Category.name).all()
    for category in categories:
        category.product = Product.query.filter_by(id_category=category.id).order_by(Product.name).all()
    return render_template('listProducts.html', categories=categories)

@app.route('/products/<int:id>')
def showProducts(id):
    # product = Product.query.filter_by(id=id).first()
    product = Product.query.get(id)
    # return f"Détails du produit {id}"
    # return render_template('showProduct.html', product=product)

    if not product:
        return redirect(url_for('noProduct'))
    else:
        return render_template('showProduct.html', product=product)

@app.route('/products/noProduct')
def noProduct():
     return render_template('noProduct.html')


@app.route('/products/edit/<id>',  methods=['GET', 'POST'])
@app.route('/products/edit/',  defaults={'id': None}, methods=['GET', 'POST'])
def editProduct(id):
   return "Formulaire d'édition"