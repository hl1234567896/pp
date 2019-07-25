from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys #调用键盘按键操作
from selenium.webdriver import ActionChains #鼠标动作链
driver=webdriver.Chrome()    #调用环境变量指定的PhantomJS浏览器创建浏览器对象

# https://blog.csdn.net/fenglei0415/article/details/80316241

driver.get("http://www.baidu.com/")
# data=driver.find_element_by_id('wrapper').text
# driver.save_screenshot('baidu.png') #生成快照并保存
driver.find_element_by_id('kw').send_keys(u'德玛西亚')   #搜索框搜索

driver.find_element_by_id('su').click() #模拟点击
time.sleep(5)

# print(driver.page_source) #打印网页渲染后的源代码
# print(driver.get_cookies())  #获取当前页面Cookie

# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a') #ctrl+a全选输入框内容
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')    #ctrl+x剪切输入框内容
# driver.find_element_by_id('kw').send_keys('技能') #输入框重新输入内容

# driver.find_element_by_id('su').send_keys(Keys.RETURN)    #模拟Enter回车键
# time.sleep(5)

# driver.find_element_by_id('kw').clear() #清空输入框内内容
# print(driver.current_url)   #获取当前url
driver.find_element_by_partial_link_text("图片").click()

driver.find_element_by_xpath('//a[@class="div_2002919951,1372519208"]').click()
time.sleep(5)
driver.find_element_by_xpath('//div/span[@class="bar-btn btn-download"]').click()














