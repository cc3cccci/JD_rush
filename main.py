# 这是一个示例 Python 脚本。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。f

from selenium import webdriver
from time import sleep
import random
from selenium.webdriver.chrome.service import Service





mobile_emulation = {"deviceName": "Nexus 5"}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)  # 这里看清楚了，不是add_argument

driver = webdriver.Chrome(r'C:\Users\lmx\PycharmProjects\pythonProject1\chromedriver.exe',chrome_options = chrome_options)



# driver1 = webdriver.Chrome(r'C:\Users\lmx\PycharmProjects\pythonProject1\chromedriver.exe',chrome_options = chrome_options) # 这里的chrome_options 建议都使用 desired_capabilities ，应为在Grid分布式中比较方便


# #driver = webdriver.Chrome(r'C:\Users\lmx\PycharmProjects\pythonProject1\chromedriver.exe')
#
driver.get('https://daojia.jd.com/')
print('获取网页')
# try:
#     driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/img').click()
# except:
sleep(2)
# /html/body/div/div/div[2]/div/div[2]/div/img
#/html/body/div/div/div[2]/div/div[2]/div/img
#//*[@id="root"]/div/div[2]/div/div[2]/div/img

#/html/body/div/div/div[2]/div/div[2]/div/img

driver.find_element_by_xpath('/html/body/div/div/div[3]/a[4]/i').click()
print('我的')
sleep(1)
#
driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div/div[1]/div[3]/div/div[1]').click()
print('登录中')
#
sleep(30)

driver.find_element_by_xpath('/html/body/div/div/div[2]/a[3]/span').click()
print('购物车')
sleep(1)

driver.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div[2]/div[2]/div/div/div').click()
print('结算')
sleep(1)



# driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]').click()
# print('选择时间')

#/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div

sleep(0.3)

n=0
while n<100:
    t = random.randint(4,10)
    print('随机数值%s',t)
    driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]').click()
    print('打卡选择时间菜单成功')
    try:
            driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]').click()
            print('打卡选择时间菜单成功')

            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div').click()
            print('选择时间2')

            sleep(0.1)

            driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()

            #/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div
            print('提交订单')
    except:
            try:
                driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[4]/div').click()
                print('选择时间4')

                sleep(0.1)

                driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                print('提交订单')
            except:
                    try:
                        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[5]/div').click()
                        print('选择时间5')

                        sleep(0.1)

                        driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                        print('提交订单')
                    except:
                        try:
                            driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[6]/div').click()
                            print('选择时间6')

                            sleep(0.1)

                            driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                            print('提交订单')
                        except:
                            try:
                                driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[7]/div').click()
                                print('选择时间7')

                                sleep(0.1)

                                driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                                print('提交订单')
                            except:
                                try:
                                    driver.find_element_by_xpath(
                                        '/html/body/div[2]/div/div/div[2]/div[2]/div/div[8]/div').click()
                                    print('选择时间7')

                                    sleep(0.1)

                                    driver.find_element_by_xpath(
                                        '/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                                    print('提交订单')
                                except:
                                    try:
                                        driver.find_element_by_xpath(
                                            '/html/body/div[2]/div/div/div[2]/div[2]/div/div[9]/div').click()
                                        print('选择时间7')

                                        sleep(0.1)

                                        driver.find_element_by_xpath(
                                            '/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                                        print('提交订单')
                                    except:
                                        try:
                                            driver.find_element_by_xpath(
                                                '/html/body/div[2]/div/div/div[2]/div[2]/div/div[10]/div').click()
                                            print('选择时间7')

                                            sleep(0.1)

                                            driver.find_element_by_xpath(
                                                '/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                                            print('提交订单')
                                        except:
                                            try:
                                                driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div/div[8]/div').click()
                                                print('选择时间8')

                                                sleep(0.1)

                                                driver.find_element_by_xpath('/html/body/div/div/div[1]/div[4]/div/div/div[2]/div/div/div/div').click()
                                                print('提交订单')
                                            except:
                                                print("无时间可选")
                                                sleep(t)
                                                n=n+1
                                                sleep(5)
                                                driver.refresh()
                                                print('刷新成功')
                                                print('下一步')
                                                sleep(t)


                            # driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/div[3]/div[2]/div/div[1]/div[2]/div[1]').click()
                            # print('选择时间')

                            #/html/body/div[2]/div/div/div[1]/div[1]/div/img







# /html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div
# /html/body/div[2]/div/div/div[2]/div[2]/div/div[4]/div
print('ok')


















# def main():
#     # 在下面的代码行中使用断点来调试脚本。
#     print('hi')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     main()
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
