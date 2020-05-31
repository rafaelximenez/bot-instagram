#*-* coding: utf-8 *-*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json


class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"/usr/local/bin/geckodriver")  # Caminho do geckodriver

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('Tentativa de login')
            pass
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4, 6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))       

    def like_photos_and_follow_users_with_hashtag(self, hashtag, number_likes):
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/?hl=pt-br")
        time.sleep(2)
        # Rolar páginas
        for i in range(1, 2):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        # Pegar links
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        print("Fotos com a hashtag '" +  hashtag + "': " + str(len(pic_hrefs)))
        i = 0
        # Percorrer links
        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:                
                continue
            driver.get(pic_href)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            try:
                # Pegar usuário da publicação
                user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/a')
                # Valida se o usuário é valido para seguir
                if user.text != None:
                    # Seguir usuário
                    driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button').click()
                    # Gerar arquivo com usuários para unfollow
                    open(str(self.username) + '.txt', 'a').write(str(user.text) + '\n')
                    time.sleep(random.randint(3, 5))
                # Curtir a foto
                driver.find_element_by_xpath(
                    '//button[@class="wpO6b "]').click()                    
                time.sleep(random.randint(12, 18))
            except Exception as e:
                print(e)
                time.sleep(5)
            # Limitar quantidade de likes por hashtag
            if i == number_likes:
                break
            i += 1
    
    def unfollow_user(self, user):        
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.instagram.com/" + user + "/?hl=pt-br")
        time.sleep(4)
        unfollow_buttons = driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button")
        for unfollow_button in unfollow_buttons:
            unfollow_button.click()
        time.sleep(random.randint(3, 6))
        confirm_unfollow_user = driver.find_elements_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]")
        for confirm_unfollow in confirm_unfollow_user:
            if confirm_unfollow.text == "Deixar de seguir":
                confirm_unfollow.click()
        time.sleep(random.randint(2, 5))
        