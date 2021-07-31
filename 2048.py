#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

gameURL = 'https://gabrielecirulli.github.io/2048/'

browser = webdriver.Firefox()

gameOpen = browser.get(gameURL)
game = browser.find_element_by_tag_name('html')

while game.is_displayed():
    game.send_keys(Keys.UP)
    game.send_keys(Keys.LEFT)
    game.send_keys(Keys.RIGHT)
    game.send_keys(Keys.DOWN)