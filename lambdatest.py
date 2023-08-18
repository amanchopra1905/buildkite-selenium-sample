import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

username = os.getenv("LT_USERNAME")  # Replace the username
access_key = os.getenv("LT_ACCESS_KEY")  # Replace the access key
build_name = os.getenv("BUILDKITE_JOB_ID")


class FirstSampleTest(unittest.TestCase):
    # Generate capabilites from here: https://www.lambdatest.com/capabilities-generator/
    # setUp runs before each test case and
    def setUp(self):

        options = ChromeOptions()
        options.browser_version = "114.0"
        options.platform_name = "Windows 10"
        lt_options = {}
        lt_options["build"] = build_name
        lt_options["name"]= "Sample test"
        lt_options["selenium_version"] = "4.0.0"
        lt_options["w3c"] = True
        options.set_capability('LT:Options', lt_options)

       
        self.driver = webdriver.Remote(
             command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            options=options)

        # self.driver = webdriver.Remote(
        #     command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
        #         username, access_key),
        #     options=desired_caps)

# tearDown runs after each test case


    def tearDown(self):
        self.driver.quit()

    # """ You can write the test cases here """
    def test_demo_site(self):

        # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

        # Url
        print('Loading URL')
        driver.get("https://stage-lambda-devops-use-only.lambdatestinternal.com/To-do-app/index.html")

        # Let's click on a element
        driver.find_element(By.NAME, "li1").click()
        location = driver.find_element(By.NAME, "li2")
        location.click()
        print("Clicked on the second element")

        # Let's add a checkbox
        driver.find_element(By.ID, "sampletodotext").send_keys("LambdaTest")
        add_button = driver.find_element(By.ID, "addbutton")
        add_button.click()
        print("Added LambdaTest checkbox")

        # print the heading
        search = driver.find_element(By.CSS_SELECTOR, ".container h2")
        assert search.is_displayed(), "heading is not displayed"
        print(search.text)
        search.click()
        driver.implicitly_wait(3)

        # Let's download the invoice
        heading = driver.find_element(By.CSS_SELECTOR, ".container h2")
        if heading.is_displayed():
            heading.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        else:
            driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()
