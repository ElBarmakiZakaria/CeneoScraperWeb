from app import app
from flask import render_template, url_for, redirect, request, flash
from app import scraper as sc
from app import analyzer as an
import json


@app.route('/')
def home():
    return render_template("base.html")




@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':

        product_id = request.form.get("search")

       
        product = sc.Scraper(product_id)
        product_opinions = product.product_opinions()
        an.Analyzer(product_id)

 


        if product_opinions == "0":
            flash('THERE IS NO PRODUCT LIKE THIS.', category='error')
            return redirect(url_for('home'))
        elif product_opinions == '1':
            flash('THE PRODUCT HAS NO OPINIONS!', category='error')
            return redirect(url_for('home'))
        else:
            return render_template("productpage.html", product_id=product_id, product_opinions=product_opinions)


        
@app.route('/productdata', methods=['GET'])
def data():
    with open('./charts/data.json', 'r') as file:
        data = json.load(file)
    
    return data

