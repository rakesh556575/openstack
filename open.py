from selenium import webdriver
import logging
logging.basicConfig(filename="sample.log", level=logging.INFO,format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S")


def login(url,username,password):
    driver=webdriver.Firefox(executable_path="C:\geckodriver-v0.18.0-win64\geckodriver.exe")
    driver.get(url)
    try:
       login_element=driver.find_element_by_xpath("//input[@id='id_username']")
       login_element.send_keys(username)
       login_password=driver.find_element_by_xpath("//input[@id='id_password']")

       login_password.send_keys(password)
       login_button=driver.find_element_by_xpath(".//*[@id='loginBtn']")
       login_button.click()
       logging.info("Logging to openstack console")
    except Exception as e:
        logging.error("Logging to openstack console failed")
        print("Execption occured {}".format(e))

    return driver

def logout(driver):
    try:
        admin_element=driver.find_element_by_xpath("//*[@id='navbar-collapse']/ul[2]/li[1]/a/span[3]")
        admin_element.click()
        logout_element=driver.find_element_by_xpath("//*[@id='editor_list']/li[6]/a")
        logout_element.click()
    except Exception as e:
        logging.error("Logout failed")
        print("Exception occured {}".format(e))
    return driver

#login("http://10.103.199.191/",'admin',"1b966873f14445e2")
logout(login("http://10.103.199.191/",'admin',"1b966873f14445e2"))


