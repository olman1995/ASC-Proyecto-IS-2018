import unittest
#from main.views import cargar_imagen
#click izquierdo en el proyecto
#>djang
#>>managepy. {custon}
#>>>test main
from selenium import webdriver

class SystemTest(unittest.TestCase):
    driver = webdriver.Chrome("C:\\Users\\olman\\Desktop\\chromedriver.exe")
    def test_1(self):
        print("Test1: Login")
        SystemTest.driver.get("http://127.0.0.1:8000/inicio/login.html")
        SystemTest.driver.find_element_by_name("nombre").clear()
        SystemTest.driver.find_element_by_name("nombre").send_keys("admin")
        
        SystemTest.driver.find_element_by_name("contrasena").clear()
        SystemTest.driver.find_element_by_name("contrasena").send_keys("12345")
        SystemTest.driver.find_element_by_name("LOGIN").click()
        #DjangoTest.driver.find_element_by_css_selector("input.btn.btn-success").click()
    def test_2(self):
        print("Test2: ver pacientes")
        SystemTest.driver.get("http://127.0.0.1:8000/inicio/login.html")
        SystemTest.driver.find_element_by_name("nombre").clear()
        SystemTest.driver.find_element_by_name("nombre").send_keys("abc")
        
        SystemTest.driver.find_element_by_name("contrasena").clear()
        SystemTest.driver.find_element_by_name("contrasena").send_keys("12345")
        SystemTest.driver.find_element_by_name("LOGIN").click()
        SystemTest.driver.get("http://127.0.0.1:8000/inicio/ver_pacientes.html")
        
if __name__ == '__main__':
    unittest.main()
        