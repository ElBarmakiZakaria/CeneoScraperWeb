import os
from bs4 import BeautifulSoup
import json
import requests
import numpy as np
from translate import Translator



class Scraper():

    all_opinions = []

    from_lang = "pl"
    to_lang = "en"
    translator = Translator(to_lang, from_lang)

    selectors = {
        "opinion_id" : [None, "data-entry-id"],
        "author" : ["span.user-post__author-name"],
        "recommendation": ["span.user-post__author-recomendation > em"],
        "score": ["span.user-post__score-count"],
        "description": [ "div.user-post__text"],
        "pros": ["div.review-feature__col:has( > div.review-feature__title--positives)> div.review-feature__item", None, True],
        "cons": ["div.review-feature__col:has( > div.review-feature__title--negatives)> div.review-feature__item", None, True],
        "like": ["span[id^=votes-yes]"],
        "dislike": ["span[id^=votes-no]"],
        "publish_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
        "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"]


    }  

    def __init__(self, product_id):
        self.product_id = product_id
        self.product_url = f"https://www.ceneo.pl/{product_id}#tab=reviews"


    def get_element(self, dom, sel = None, attribute = None, return_list= False):
        try:
            if return_list:
                return ", ".join([tag.text.strip() for tag in dom.select(sel)])
            if attribute:
                if sel:
                    return dom.select_one(sel)[attribute].strip()
                
                return dom[attribute]
            
            return dom.select_one(sel).text.strip()
        except (AttributeError, TypeError):
            return None


    def clear_text(self, text):
        return ' '.join(text.replace(r"\s", " ").split())



    def product_opinions(self):
        Scraper.all_opinions = []
        url = self.product_url
        exist = False
        while url:
            response = requests.get(url)

            if response.status_code == requests.codes.ok:
                exist = True
                page_dom = BeautifulSoup(response.text, "html.parser")
                opinions = page_dom.select("div.js_product-review")
            
                if len(opinions)>0:
                    print(f"There are opinions.")
                    

                    for opinion in opinions:

                        single_opinion = {}
                        for key, value in Scraper.selectors.items():
                            single_opinion[key] = self.get_element(opinion, *value)

                        single_opinion["recommendation"] = True if single_opinion["recommendation"] == "Polecam" else False if single_opinion["recommendation"] == "Nie polecam" else None
                        single_opinion["score"] = np.divide(*[float(score.replace(",", ".")) for score in single_opinion["score"].split("/")])
                        single_opinion["like"] = int(single_opinion["like"])
                        single_opinion["dislike"] = int(single_opinion["dislike"])
                        single_opinion["description"] = self.clear_text(single_opinion["description"])
                        single_opinion["description_en"] = Scraper.translator.translate(single_opinion["description"][:500])
                        single_opinion["pros_en"] = Scraper.translator.translate(single_opinion["pros"][:500])
                        single_opinion["cons_en"] = Scraper.translator.translate(single_opinion["cons"][:500])

                        

                        Scraper.all_opinions.append(single_opinion)
                    
                    next_page = self.get_element(page_dom, "a.pagination__next", "href")
                    url = f"https://ceneo.pl/{next_page}"

                    print(url)

                else:
                    print(f"There are no opinions.")
                    url = None
                    

            else:
                print("The product does not exist")
                url = None
        


        if len(Scraper.all_opinions) > 0:
            if not os.path.exists("./opinions"):
                os.mkdir("./opinions")
            with open(f"./opinions/{self.product_id}.json", "w", encoding="UTF-8") as jf:
                json.dump(Scraper.all_opinions,jf, indent=4, ensure_ascii=False)

            # an.Analyzer(self.product_id)

            return Scraper.all_opinions[0:4]
        
        else:
            if exist:
                return '1'
            else:
                return '0'



            





