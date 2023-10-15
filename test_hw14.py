'''
Дана програма тестує коректність підбору контекстних підказок пошукової системи Google,
в чотири етапи збільшуючи строку пошукового запиту до значення "скільки буде 0 в 0 степені",
щоразу звіряючи ідентичність підбору першої строки серед контекстних підказок.
(свідомо залишив у кожному тесті перевідкриття сторінки)
'''

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://google.ua/"
question = ''  # змінна строки пошукового запиту
sl = 2  # змінна затримки часу (для наочності роботи програми)


@pytest.fixture(scope="class")  # ця фікстура виконується 1 раз (при першому звертанні до класу)
def browser():
    browser = webdriver.Chrome()  # відкриваємо браузер 1 раз
    yield browser
    browser.quit()  # закриваємо браузер 1 раз


@pytest.fixture(autouse=True)  # ця фікстура виконується кожен раз перед запуском будь-якого методу класу та додає
def space():                     # пробіл в змінну строки пошукового запиту для відокремлення наступної її частини
    global question
    question = question + ' '


class TestQuestion():

    @classmethod
    def setup_class(cls):  # метод автостарту (повідомляємо про старт 1 раз)
        print("\nstart browser for test suite..")

    @classmethod
    def teardown_class(cls):  # метод автозакриття (повідомляємо про завершення 1 раз)
        print("\nquit browser for test suite..")

    def test_word1(self, browser):  # перевіряємо 'скільки'
        global question
        question = 'скільки'
        browser.get(link)
        search_field = browser.find_element(By.XPATH, '//textarea[@name="q"]')
        search_field.send_keys(question)
        time.sleep(sl)
        print(f'\n[{question}]')
        print(f'[{(browser.find_element(By.XPATH, "//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span").text)[0:len(question)]}]')
        assert (browser.find_element(By.XPATH, '//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span').text)[0:len(question)] == question

    def test_word2(self, browser):  # перевіряємо 'скільки буде'
        global question
        question = question + 'буде'
        browser.get(link)
        search_field = browser.find_element(By.XPATH, '//textarea[@name="q"]')
        search_field.send_keys(question)
        time.sleep(sl)
        print(f'\n[{question}]')
        print(f'[{(browser.find_element(By.XPATH, "//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span").text)[0:len(question)]}]')
        assert (browser.find_element(By.XPATH, '//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span').text)[0:len(question)] == question

    def test_word3(self, browser):  # перевіряємо 'скільки буде 0 в 0'
        global question
        question = question + '0 в 0'
        browser.get(link)
        search_field = browser.find_element(By.XPATH, '//textarea[@name="q"]')
        search_field.send_keys(question)
        time.sleep(sl)
        print(f'\n[{question}]')
        print(f'[{(browser.find_element(By.XPATH, "//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span").text)[0:len(question)]}]')
        assert (browser.find_element(By.XPATH, '//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span').text)[0:len(question)] == question

    def test_word4(self, browser):  # перевіряємо 'скільки буде 0 в 0 степені'
        global question
        question = question + 'степені'
        browser.get(link)
        search_field = browser.find_element(By.XPATH, '//textarea[@name="q"]')
        search_field.send_keys(question)
        time.sleep(sl)
        print(f'\n[{question}]')
        print(f'[{(browser.find_element(By.XPATH, "//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span").text)[0:len(question)]}]')
        assert (browser.find_element(By.XPATH, '//ul/li[1]/div[1]/div[2]/div[1]/div[1]/span').text)[0:len(question)] == question

