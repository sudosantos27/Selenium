from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def initialize_browser():
    return webdriver.Safari()

def login(driver, username, password):
    """
    Realiza el inicio de sesión en el sitio web.

    :param driver: Instancia del navegador web.
    :param username: Nombre de usuario.
    :param password: Contraseña.
    """
    driver.get('https://www.saucedemo.com/')
    
    username_element = find_element(driver, By.ID, 'user-name')
    password_element = find_element(driver, By.ID, 'password')

    username_element.send_keys(username)
    password_element.send_keys(password)

    click_element(driver, By.ID, 'login-button')

def add_products_to_cart(driver, products):
    """
    Agrega productos al carrito de compras.

    :param driver: Instancia del navegador web.
    :param products: Lista de productos para agregar al carrito.
    """
    for product in products:
        try:
            xpath_product = f"//button[@data-test='add-to-cart-{product.lower().replace(' ', '-')}' and contains(@id, 'add-to-cart')]"
            click_element(driver, By.XPATH, xpath_product)
            wait_for_cart_update(driver)
            time.sleep(2)
        except Exception as e:
            print(f"No se pudo agregar '{product}' al carrito. Error: {e}")

def go_to_cart(driver):
    """
    Navega a la página del carrito.

    :param driver: Instancia del navegador web.
    """
    click_element(driver, By.CLASS_NAME, 'shopping_cart_link')
    wait_for_cart_page(driver)

def checkout(driver):
    """
    Completa el proceso de pago.

    :param driver: Instancia del navegador web.
    """
    click_element(driver, By.ID, 'checkout')
    wait_for_checkout_form(driver)
    
    fill_checkout_form(driver, 'Agustin', 'Santos', '123')
    
    click_element(driver, By.ID, 'continue')
    time.sleep(2)

    click_element(driver, By.ID, 'finish')
    time.sleep(2)
    
    print("Proceso de compra finalizado correctamente.")

def find_element(driver, by, value):
    # Espera y devuelve un elemento según la estrategia de espera explícita
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, value))
    )

def click_element(driver, by, value):
    # Encuentra un elemento y hace clic en él
    element = find_element(driver, by, value)
    element.click()

def wait_for_cart_update(driver):
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
    )

def wait_for_cart_page(driver):
    wait_for_element(driver, By.CLASS_NAME, 'cart_list')

def wait_for_checkout_form(driver):
    wait_for_element(driver, By.ID, 'first-name')

def wait_for_element(driver, by, value):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, value))
    )

def fill_checkout_form(driver, first_name, last_name, postal_code):
    driver.find_element(By.ID, 'first-name').send_keys(first_name)
    driver.find_element(By.ID, 'last-name').send_keys(last_name)
    driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

def main():
    # Inicializa el navegador
    driver = initialize_browser()
    
    try:
        # Realiza el inicio de sesión y compra productos
        login(driver, 'standard_user', 'secret_sauce')
        
        products_to_add = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt']
        add_products_to_cart(driver, products_to_add)
        
        # Va al carrito y completa el proceso de pago
        go_to_cart(driver)
        checkout(driver)
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
