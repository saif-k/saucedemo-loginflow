# This Python script is made by Saif Alkhaldi.
# Press Shift+F10.
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#Variables__________________________________________________________________________________________
locked = 'Epic sadface: Sorry, this user has been locked out.'
wrong = 'Epic sadface: Username and password do not match any user in this service'
missing_one = 'Epic sadface: Password is required'
missing_two = 'Epic sadface: Username is required'
list_one = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bike-light", "add-to-cart-sauce-labs-bolt-t-shirt"]
list_two = ["add-to-cart-sauce-labs-fleece-jacket", "add-to-cart-sauce-labs-onesie", "add-to-cart-test.allthethings()-t-shirt-(red)"]
seqs = list_one, list_two
item_one = random.choice(random.choices(seqs, weights=map(len, seqs))[0])
item_two = random.choice(random.choices(seqs, weights=map(len, seqs))[0])
item_three = random.choice(random.choices(seqs, weights=map(len, seqs))[0])
#____________________________________________________________________________________________________
#Functions____________________________________________________________________________________________
def loginflow(username, password):
   driver = webdriver.Chrome()
   url = "https://www.saucedemo.com/"
   driver.get(url)
   driver.maximize_window()
   driver.find_element(By.ID, "user-name").send_keys(username)
   sleep(5)
   driver.find_element(By.ID, "password").send_keys(password)
   sleep(5)
   driver.find_element(By.ID, "login-button").click()
   driver.find_element(By.ID, item_one).click()
   sleep(5)
   driver.find_element(By.ID, item_two).click()
   sleep(5)
   driver.find_element(By.ID, item_three).click()
   sleep(5)
   driver.find_element(By.ID, "shopping_cart_container").click()
   sleep(5)

def loginflow_two(username, password):
    driver = webdriver.Chrome()
    url = "https://www.saucedemo.com/"
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys(username)
    sleep(5)
    driver.find_element(By.ID, "password").send_keys(password)
    sleep(5)
    driver.find_element(By.ID, "login-button").click()
    login_form = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
    if locked == login_form:
        print('Epic sadface: Sorry, this user has been locked out.')
    elif wrong == login_form:
        print('Epic sadface: Username and password do not match any user in this service')
    elif missing_one or missing_two == login_form:
        print('Username or Password missing')
    else:
        pass
#______________________________________________________________________________________________________________________

#MAIN__________________________________________________________________________________________________________________
def menu():
    print("[1] Option 1 Test Fully Functional Users")
    print("[2] Option 2 Test Locked and None Users")
    print("[0] Exit the Program.")

menu()
option = int(input("Enter your option: "))

while option != 0:
 if option == 1:
  username = input('Type Username\n')
  password = input('Type Password\n')
  loginflow(username,password)
 elif option == 2:
    user_name = input('Type username\n')
    pass_word = input('Type Password\n')
    loginflow_two(user_name, pass_word)
 else:
    print("Invalid option.")

 menu()
 option = int(input("Enter your option: "))
print("Thank you for using this program, Good Bye")
#End of code________________________________________________________________________________________________________