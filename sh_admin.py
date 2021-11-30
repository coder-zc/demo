import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAdmin(unittest.TestCase):
    def test_01_login(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(6)
        driver.get("https://admin.shuishan.net.cn/login")
        driver.find_element(By.XPATH, "//input[@name='username']").send_keys("sysadmin")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("shuishan2021")
        driver.find_element(By.XPATH, "//span[text()='登录 ']").click()
        time.sleep(3)
        # 查询东华大学教师人数
        driver.find_element(By.XPATH, "//span[text()='企业管理']").click()
        time.sleep(2)
        teacher_num = driver.find_element(By.XPATH, "//div[text()='东华大学']/../../td[3]/div").text
        print("教师人数：" + teacher_num)

        driver.find_element(By.XPATH, "//span[text()='讲师管理']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[2]/section/header/div/button[6]").click()
        # windows = driver.window_handles
        # driver.switch_to_window(windows[2])
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[2]/section/main/div/form/div[2]/div/div[1]/input").send_keys("test@webUI")
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[2]/section/main/div/form/div[4]/div/div[1]/input").send_keys("test@webUI.com")
        driver.find_element(By.XPATH, "//*[@id='app']/div/div[2]/section/div/div[1]/div/div/div[2]/section/main/div/form/div[5]/div/div/input").send_keys("18866668888")
        driver.find_element(By.XPATH, "//span[text()='添加']").click()
        # 查询东华大学教师人数
        # 如果信息相同的话会显示已注册
        # 测试内容：测试添加教师功能是否正常，批量添加教师后，教师人数是否和预期一样
        driver.find_element(By.XPATH, "//span[text()='企业管理']").click()
        time.sleep(2)
        teacher_num = driver.find_element(By.XPATH, "//div[text()='东华大学']/../../td[3]/div").text
        print("教师人数：" + teacher_num)
        driver.quit()

# if __name__ = '__main__':
#     unittest.main()
