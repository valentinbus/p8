import requests
import urllib.parse 

from pprint import pprint


SEARCH_URL = 'https://fr.openfoodfacts.org/cgi/search.pl'
CATEGORIES = 'https://fr.openfoodfacts.org/categories?json=1'
CATEGORY_URL = 'https://fr.openfoodfacts.org/categorie/'
PRODUCT_URL = 'https://world.openfoodfacts.org/api/v0/product/'
OPENFOODFACT_URL = 'https://fr.openfoodfacts.org/produit/'

class OpenFoodFacts:
    def __init__(self):
        self.categories = list()
        self.product_id = list()

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
                "link": a.get('url')
                }

            result.append(d)
        return result

    def purpose_replace(self, product):
        """
        Give best nutriscore purpose by category for user
        """
        category = product['category']
        nutriscore = product['nutriscore']
        
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

    def list_all_categories(self, number_of_category):
        """
        Get All Categories from Op
        """
        result = list()
        request = requests.get(
            url=CATEGORIES, params=None
        ).json()

        self.categories = [categorie['id'][3:] for categorie in request["tags"][:number_of_category]]

    def get_products_id_by_category(self):
        """
        Get All products id by category
        """
        params = {
            "json": 1
        }

        for category in self.categories:
            url = f"{CATEGORY_URL}/{category}"
            request = requests.get(url=url, params=params).json()

            self.product_id.append([product['_id'] for product in request['products']])

    def product_informations(self):
        """
        Get all products information
        """
        products = list()
        params = {
            "json": 1
        }

        for i in self.product_id:
            for product in i:
                url = f"{PRODUCT_URL}/{product}.json"
                request = requests.get(url=url, params=params).json()
                products.append(
                    {
                        "name": request.get("product").get("product_name"),
                        "category": request.get("product").get("categories_hierarchy")[0][3:],
                        "nutriscore": request.get("product").get("nutrition_grades_tags")[0],
                        "url_op": f"{OPENFOODFACT_URL}/{product}",
                        "image_url": request.get("product").get("image_url")
                    }
                )

        return products

    def init_db(self, number_of_category):
        """
        Runs all methods to init db
        """
        self.list_all_categories(number_of_category)
        self.get_products_id_by_category()
        return self.product_informations()


op = OpenFoodFacts()
pprint(op.init_db(3))
#print(op.search("nutella"))
#print(op.purpose_replace("breakfast", "d"))
