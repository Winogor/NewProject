from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


def run_script():
    options = ChromeOptions()
    driver = Chrome(options=options)
    driver.get("https://go.skillbox.ru")
    driver.quit()


if __name__ == '__main__':
    run_script()
