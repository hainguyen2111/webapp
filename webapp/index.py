from flask import render_template
from webapp import app
import utils


@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html', catgories=cates)

@app.route("/products")
def products_list():
    products = utils.load_products()
    return render_template('products.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)