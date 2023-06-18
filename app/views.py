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
        an.Analyzer('105113892')

    #     product_opinions = [
    # {
    #     "opinion_id": "16899538",
    #     "author": "b...z",
    #     "recommendation": "true",
    #     "score": 0.9,
    #     "description": "Jestem zadowolony Wygodne antyramy, pleksi lżejsza niż szkło. Komfortowe mocowanie zarówno w pionie jak i poziomie Dla mnie super",
    #     "pros": "jakość, styl, wygląd",
    #     "cons": "",
    #     "like": 0,
    #     "dislike": 0,
    #     "publish_date": "2022-12-19 09:24:33",
    #     "purchase_date": "2022-12-08 15:55:30",
    #     "description_en": "I am satisfied Comfortable antirams, plexiglass lighter than glass. Comfortable mounting both vertically and horizontally For me super",
    #     "pros_en": "quality, style, appearance",
    #     "cons_en": ""
    # },
    # {
    #     "opinion_id": "17338248",
    #     "author": "a...9",
    #     "recommendation": "true",
    #     "score": 1.0,
    #     "description": "produkty w bardzo dobrym stanie, pierwszorzędnie zapakowane i zabezpieczone",
    #     "pros": "",
    #     "cons": "",
    #     "like": 0,
    #     "dislike": 0,
    #     "publish_date": "2023-03-29 23:23:07",
    #     "purchase_date": "2023-03-13 15:23:08",
    #     "description_en": "products in very good condition, first-class packed and secured",
    #     "pros_en": "",
    #     "cons_en": ""
    # },
    # {
    #     "opinion_id": "17469541",
    #     "author": "Łukasz",
    #     "recommendation": "true",
    #     "score": 1.0,
    #     "description": "Do samej antyramy brak przeciwwskazań. Jedynie wysyłka trochę trwała.",
    #     "pros": "jakość, styl, wygląd",
    #     "cons": "",
    #     "like": 0,
    #     "dislike": 0,
    #     "publish_date": "2023-05-03 20:49:31",
    #     "purchase_date": "2023-04-07 15:25:24",
    #     "description_en": "There are no contraindications to the antrama itself. The shipping took a while.",
    #     "pros_en": "quality, style, appearance",
    #     "cons_en": ""
    # },
    # {
    #     "opinion_id": "16857490",
    #     "author": "a...7",
    #     "recommendation": "true",
    #     "score": 1.0,
    #     "description": "Zgodny z opisem. Dobrze zabezpieczony",
    #     "pros": "",
    #     "cons": "",
    #     "like": 0,
    #     "dislike": 0,
    #     "publish_date": "2022-12-09 13:51:35",
    #     "purchase_date": "2022-11-30 17:41:00",
    #     "description_en": "Complies with description. Well secured",
    #     "pros_en": "",
    #     "cons_en": ""
    # }]


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

