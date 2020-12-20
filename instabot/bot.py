from selenium import webdriver
from time import sleep
from random import randrange


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.totlikes = 0

        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        login_field = self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        password_field = self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(2)
        code = input("insert code")
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div/label/input').send_keys(code)
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/section/div/button').click()
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(2)

    def work_randomly(self, profile, stop=100, start=0):
        n = start
        number_list = []
        rand_number = 0
        while True:

            #barra di ricerca
            self.driver.get("https://instagram.com/{}".format(profile))
            sleep(2)

            #entra nei follower
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            sleep(2)



            last_ht,ht = 0,1
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")

            # entra nel profilo di un follower random
            while True:
                rand_number = randrange(start, stop, 1) #start,stop,step
                if rand_number not in number_list:
                    number_list.append(rand_number)
                    break

            print("user to find: {}".format(rand_number))
            while True:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(rand_number)).click()
                    print("Found!")
                    break
                except Exception:
                    pass

                try:
                    ht = self.driver.execute_script("""
                                arguments[0].scrollTo({},{});
                                return arguments[0].scrollHeight""".format(ht,ht+10), scroll_box)

                except Exception:
                    break
                sleep(1.5)

            sleep(3)


            #prende la prima foto
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                print("getting the picture")
            except Exception:
                pass
            sleep(1.4)

            # mette like
            try:
                self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                print("pushing like")
                self.totlikes += 1
                print("total likes done until now: {}".format(self.totlikes))
            except Exception:
                pass
            sleep(1.4)

            n += 1

            if n == stop:
                print("process finished")
                print("total number of likes done: {}".format(self.totlikes))
                print("Last user number: {}".format(n))
                break

    def work_sequentially(self, profile, stop=100, start=0):
        n = start
        while True:
            # barra di ricerca
            self.driver.get("https://instagram.com/{}".format(profile))
            sleep(2)

            # entra nei follower
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            sleep(2)

            last_ht, ht = 0, 1
            scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            # entra nel profilo di un follower random


            print("user to find: {}".format(n))
            while True:
                try:
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div/div[2]/ul/div/li[{}]/div/div[2]/div[1]/div/div/span/a'.format(
                            n)).click()
                    print("Found!")
                    break
                except Exception:
                    pass

                try:
                    ht = self.driver.execute_script("""
                                arguments[0].scrollTo({},{});
                                return arguments[0].scrollHeight""".format(ht, ht + 10), scroll_box)

                except Exception:
                    break
                sleep(1.5)

            sleep(3)

            try:
                # prende la prima foto
                self.driver.find_element_by_xpath(
                    '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
                print("getting the picture")
            except Exception:
                pass
            sleep(2)

            # mette like
            try:

                self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                print("pushing like")
                self.totlikes += 1
                print("total likes done until now: {}".format(self.totlikes))
            except Exception:
                pass
            sleep(2)

            n += 1

            if n == stop:
                print("process finished")
                print("total number of likes done: {}".format(self.totlikes))
                print("Last user number: {}".format(n))
                break






