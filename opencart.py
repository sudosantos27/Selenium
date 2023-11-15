from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def initialize_browser():
    return webdriver.Safari()

def choose_currency():
    try:
        # Solicitar al usuario que seleccione la divisa
        print("Seleccione la moneda:")
        print("1. EUR")
        print("2. Libras")
        print("3. USD")
        currency_choice = input("Ingrese el número de la moneda deseada (1, 2 o 3): ")
        return currency_choice
    except Exception as e:
        print(f"Error al elegir la moneda: {e}")
        return None

def update_currency(driver, currency_code):
    try:
        # Hacer clic en el botón de selección de moneda
        currency_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/a'))
        )
        currency_button.click()
        time.sleep(2)

        # Esperar a que se carguen las opciones de la moneda
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="form-currency"]/div/ul'))
        )
        time.sleep(2)

        # Seleccionar la moneda deseada
        currency_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="form-currency"]/div/ul/li[{currency_code}]/a'))
        )
        currency_option.click()
        time.sleep(2)

        print(f"Moneda cambiada a {currency_code}")

    except Exception as e:
        print(f"Error al cambiar la moneda: {e}")

def register(driver):
    try:
        # Hacer clic en el enlace de registro
        register_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div'))
        )
        register_link.click()
        time.sleep(2)

        # Esperar a que se carguen las opciones de registro
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/a'))
        )
        time.sleep(2)

        currency_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div[2]/div[2]/ul/li[2]/div/ul/li[1]/a'))
        )
        currency_option.click()
        
        # Esperar a que se cargue la página de registro
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'input-firstname'))
        )


        # Completar el formulario de registro
        driver.find_element(By.ID, 'input-firstname').send_keys("John")
        driver.find_element(By.ID, 'input-lastname').send_keys('Doe')
        driver.find_element(By.ID, 'input-email').send_keys("agustin@gmail.com")
        driver.find_element(By.ID, 'input-password').send_keys("123")

        # Aceptar los términos y condiciones
        terms_checkbox = driver.find_element(By.NAME, 'agree')
        terms_checkbox.click()

        time.sleep(2)

        # Hacer clic en el botón continue
        register_button = driver.find_element(By.XPATH, '//*[@id="form-register"]/div/div/button')
        register_button.click()

        print(f"Usuario registrado")

    except Exception as e:
        print(f"Error durante el registro: {e}")


def main():
    driver = initialize_browser()
    
    try:
        # Simulación de espera
        time.sleep(2)

        # Obtener la elección de la moneda del usuario
        currency_choice = choose_currency()

        # Visitar el sitio web
        driver.get('https://demo.opencart.com/')

        # Simulación de espera
        time.sleep(2)
        
        # Actualizar la moneda con la elección del usuario
        if currency_choice:
            update_currency(driver, currency_choice)

        # Simulación de espera
        time.sleep(5)

        register(driver)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
