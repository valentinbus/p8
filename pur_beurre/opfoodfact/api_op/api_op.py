import requests
import urllib.parse 

from pprint import pprint


SEARCH_URL = 'https://fr.openfoodfacts.org/cgi/search.pl'
CATEGORY_URL = 'https://fr.openfoodfacts.org/categorie/'

class OpenFoodFacts:
    def __init__(self):
        pass

    def search(self, q):
        """
        Give search results
        """
        params = {
            "json": 1,
            "search_terms": q
        }

        request = requests.get(
            url=SEARCH_URL, params=params
        ).json()

        result = list()
        for a in request['products']:
            d = dict()
            d = {
                "product_name": a.get('product_name'),
                "category": a.get('categories_hierarchy')[0][3:],
                "nutriscore": a.get('nutrition_grades_tags')[0],
                "store": a.get('stores'),
                "link": a.get('url')
                }
 
            result.append(d)
        return result
        
    def purpose_replace(self, category, nutriscore):
        """
        Give best nutriscore purpose by category for user
        """
        END_URL = urllib.parse.quote(category)
        URL = CATEGORY_URL+END_URL

        params = {
            "json": 1
        }

        result = list()
        request = requests.get(
            url=URL, params=params 
        ).json()

        for product in request['products']:
            d = dict()
            if product.get('nutrition_grade_fr') and product.get('nutrition_grade_fr')<=nutriscore:
                d = {
                    "product_name": product.get('product_name'),
                    "nutriscore": product.get('nutrition_grade_fr'),
                    "link": product.get('url')
                }
                result.append(d)
            else:
                pass

        return result



#op = OpenFoodFacts()
#print(op.search("nutella"))
#print(op.purpose_replace("breakfast", "d"))
