# Web自动化测试  
Web自动化即是用编程语言编写测试脚本，通过selenium驱动Web浏览器来模拟用户行为，到达测试的目的。所以要编写自动化测试用例需要编程环境（语言+IDE），selenium， selenium相应要语言的API封装库和浏览器驱动。这里对应的就是python+pycharm，seleium的python绑定（自带了selenium），以及chrome浏览器的driver。编写脚本的方式也有很多，直接用脚本，使用xunit框架或者bdd框架

### 软件安装
1. 安装python 3.5.1  
   下载链接在这里找到：https://www.python.org/downloads/  
   __注意事项：安装时记得pip要一起安装，安装后需要配置环境变量，把安装目录和安装目录下的Scripts目录加到PATH__
   安装完成zhi
2. 安装python package，在命令行运行下面两条命令：  
   `pip install selenium`  
   `pip install nose`(可选, 让运行测试更简单)  
3. 安装pycharm community edition（社区版）  
   下载链接在这里找到：https://www.jetbrains.com/pycharm/download/  
   __注意事项：选择右侧的Community，社区版免费使用，可以满足写测试用例99%的需要；pycharm本身是用java写的，如果事先没有安装java记得安装java__
4. 安装chrome driver(使用chrome必须要安装)  
   下载链接在这里找到：http://chromedriver.storage.googleapis.com/index.html  
   __注意事项：解压到目录后，把目录加入到PATH环境变量__

### 一个selenium例子
```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

### 一个测试例子
```python
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_split(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)
```


### API文档
1. unittest：https://docs.python.org/3/library/unittest.html#module-unittest
2. selenium python binding: http://selenium-python.readthedocs.org/

### 教程
1. python3教程（中文）：http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
2. selenium基础介绍（中文）：http://www.cnblogs.com/fnng/p/3980093.html

### 参考资料
1. selenium系列文章（中文）：http://www.cnblogs.com/fnng/category/349036.html
2. selenium系列文章（英文）：http://elementalselenium.com/

# 移动APP自动化测试
移动APP自动化测试和Web自动化测试类似，一样是模拟用户的行为，只是驱动的是移动设备而不是浏览器。selenium只能驱动浏览器，驱动移动设备得依靠其他工具。目前最受欢迎的就是appium，appium和selenium的名字很像，它使用的是selenium的wd协议，和selenium的API几乎一模一样，更是提供了移动设备才有的一些操作，如打开关闭应用，滑动手势等。除了appium，驱动设备还需要各个平台的开发工具，对iOS设备来说就是Xcode，对android设备来说就是android sdk。  
![Appium iOS](http://www.3pillarglobal.com/sites/default/files/appium1.png)  
![Appium Android](http://www.3pillarglobal.com/sites/default/files/appium2.png)

### 软件安装
1. 安装appium  
   有两种方式，一种是安装appium独立应用，一种是通过node安装（appium是用node实现）。这里我们选择第一种方式。  
   下载链接在这里找到：https://bitbucket.org/appium/appium.app/downloads/
2. 安装android sdk  
   由于众所周知的原因，google的网站访问不稳定，好在国内有好心人做了镜像，提供了几乎所有android开发工具的下载。我们需要安装的是SDK Tools和Platform Tools  
   下载链接在这里找到：http://www.androiddevtools.cn/  
   __注意事项:先安装SDK Tools，然后把Platform Tools解压到SDK Tools的安装目录下；完成之后把SDK安装目录下的tools和platform-tools都加入到PATH环境变量__
3. 安装xcode，直接在App store里选择安装  
4. 安装appium的python绑定  
   `pip install Appium-Python-Client`
5. 安装genymotion模拟器（Android）  
   在这里注册下载：http://www.genymotion.net/

