from selenium import webdriver

yqin@thoughtworks.com

def test_baidu_should_return_training_as_first_result_if_you_search_selenium():

    driver = webdriver.Firefox()

    driver.get("http://www.baidu.com")

    element = driver.find_element_by_id("kw")

    element.send_keys("selenium")

    button = driver.find_element_by_css_selector("input#su")

    button.click()

    driver.implicitly_wait(30)

    driver.save_screenshot("result.png")

    driver.quit()
