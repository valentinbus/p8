# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class OpenfoodfactViewstest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome("/Users/valentinbus/Development/chromedriver/chromedriver")

#     def test_list_products(self):
#         self.driver.get("http://localhost:8000/")
#         self.driver.find_element_by_id('list_button').click()
#         self.assertIn("http://localhost:8000/openfoodfact/list/", self.driver.current_url)

#     def test_search_products(self):
#         self.driver.get("http://localhost:8000/")
#         self.driver.find_element_by_id('search_form').send_keys("pizza", Keys.ENTER)
#         self.assertIn("http://localhost:8000/openfoodfact/search_product/?q=pizza", self.driver.current_url)

#     def test_search_products(self):
#         self.driver.get("http://localhost:8000/")
#         self.driver.find_element_by_id('search_form').send_keys("pizza", Keys.ENTER)
#         self.assertIn("http://localhost:8000/openfoodfact/search_product/?q=pizza", self.driver.current_url)

#     def test_search_products_2(self):
#         self.driver.get("http://localhost:8000/")
#         self.driver.find_element_by_id('search_product_button').click()
#         self.driver.find_element_by_id('search_product_home').send_keys("pizza", Keys.ENTER)
#         self.assertIn("http://localhost:8000/openfoodfact/search_product/?q=pizza", self.driver.current_url)

#     def test_purpose_replace(self):
#         self.driver.get("http://127.0.0.1:8000/openfoodfact/search_product/?q=Pizza+surgel%C3%A9e+Jambon+Speck+Roquette+Mozzarella")
#         self.driver.find_element_by_id("purpose_substitut_button").click()
#         self.assertIn("http://127.0.0.1:8000/openfoodfact/replace/?id=4894", self.driver.current_url)
        
#     def save_replacement(self):
#         """
#         If user not login
#         """
#         self.driver.get("http://127.0.0.1:8000/openfoodfact/search_product/?q=Pizza+surgel%C3%A9e+Jambon+Speck+Roquette+Mozzarella")
#         self.driver.find_element_by_id("purpose_substitut_button").click()
#         self.driver.find_element_by_id("save_substitut_button").click()
#         self.assertIn("http://127.0.0.1:8000/connexion/?next=/openfoodfact/save_replacement/%3Fid_product_to_replace%3D4894%26id_replace_product%3D4892", self.driver.current_url)

#     def tearDown(self):
#         self.driver.quit

# if __name__ == '__main__':
#     unittest.main()
