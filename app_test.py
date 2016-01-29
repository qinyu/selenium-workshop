import unittest

from selenium import webdriver

desired_caps = {"platformName": "Android",
                "app": "/Users/yqin/Github/gdgcd-demo/app/build/outputs/apk/app-workShop-debug.apk",
                "deviceName": "192.168.58.101:5555"}


class TestApp(unittest.TestCase):
    def test_search_google(self):
        self.driver = \
            webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



        # org.gdgcd.demo
        # .activity.BooksActivity
