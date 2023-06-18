import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import json


class Analyzer():
    def __init__(self, product_id):
        self.product_id = product_id
        self.opinions = pd.read_json(f"./opinions/{self.product_id}.json")
        self.max_score  =5

        if not os.path.exists("./charts"):
            os.mkdir("./charts")

        self.recommendations = self.opinions["recommendation"].value_counts(dropna=False).reindex([True, False, np.nan], fill_value=0)
        self.recco = self.recommendations.to_list()
        

        self.opinions["stars"] = (self.opinions["score"]*self.max_score).round(1)

        self.stars = self.opinions.stars.value_counts().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
        self.score = self.stars.to_list()

        with open('./charts/data.json', 'w') as jf:
            json.dump([self.recco, self.score],jf, indent=4, ensure_ascii=False)





    # def making_graphs(self):
    #     self.recommendations.plot.pie(label="", 
    #                     labels = ["Recommend", "Not recommend", "neutural"],
    #                     title="Recommentations:",  
    #                     colors=['#22DE00', '#E25A5A', '#CDCCE3'], 
    #                     fontsize=9,
    #                     autopct= lambda p: '{:.1f}%'.format(round(p)) if p > 0 else '')


    #     plt.savefig(f"./charts/{self.product_id}_pie.png")
    #     plt.close()


    #     self.stars.plot.bar(color= "lightblue")
    #     plt.ylim(0, max(self.stars)+10)
    #     plt.title("Star count distribution")
    #     plt.xlabel("number of stars")
    #     plt.ylabel("Number of opinions")
    #     plt.xticks(rotation = 0)
    #     plt.grid(True, "major", "y")
    #     for index, value in enumerate(self.stars):
    #         plt.text(index, value+1.5, str(value), ha = 'center')
    #     plt.savefig(f"./charts/{self.product_id}_bar.png")
    #     plt.close()