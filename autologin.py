import json
import time

from selenium import webdriver

CONFIG_FN = "config.json"


def update_config():
    print "can not find configuration file or the file is wrongly formatted. Reconfiguring.."

    url = raw_input("Login url: ")
    username = raw_input("Username: ")
    password = raw_input("Password: ")

    config = open(CONFIG_FN, "w")
    json.dump({'url': url, 'username': username, 'password': password}, config)
    config.close()


def check_config():
    try:
        config = open(CONFIG_FN, mode="r")
        data = json.load(config)
        config.close()
        if 'url' not in data:
            raise IOError
        if 'username' not in data:
            raise IOError
        if 'password' not in data:
            raise IOError
        return data
    except IOError:
        update_config()
        return check_config()


def open_new_tab(browser, tab_id):
    if type(browser).__name__ == 'WebDriver':
        script = "window.open('', '_new_tab" + str(tab_id) + "')"
        browser.execute_script(script)
        return True
    return False


def switch_to_tab(browser, tab_index=0):
    if type(browser).__name__ == 'WebDriver':
        browser.switch_to_window(browser.window_handles[tab_index])
        return True
    return False


def close_login_page(browser, x):
    open_new_tab(browser, x)
    browser.close()
    switch_to_tab(browser, 0)
    return True


TAB_ID = 0


def reset_tab_id():
    global TAB_ID
    TAB_ID = 0


def increase_tab_id():
    global TAB_ID
    TAB_ID = TAB_ID + 1


def login2(browser, url, USER, PASS):
    browser.get(url)
    time.sleep(5)

    status = browser.find_element_by_id('lblusername')

    if str(status.text) == USER:
        if TAB_ID > 100:
            browser.quit()
            reset_tab_id()
            return False
        close_login_page(browser, TAB_ID)
        increase_tab_id()
        return True

    else:
        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")
        username.send_keys(USER)
        password.send_keys(PASS)
        login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()
        return True


def main():
    config = check_config()
    firefox = webdriver.Firefox()

    # test_case = "11:56"

    while True:
        now = time.strftime("%H:%M", time.localtime())
        print now
        if now == "00:00" or now == "08:00":  # or now == test_case:
            if not login2(firefox, config['url'], config['username'], config['password']):
                firefox = webdriver.Firefox()
            print 'success'
            time.sleep(60)
        time.sleep(5)


def test():
    config = check_config()
    f = webdriver.Firefox()

    while True:
        if not login2(f, config['url'], config['username'], config['password']):
            f = webdriver.Firefox()
        time.sleep(10)
        print 'Success'


if __name__ == "__main__":
    main()
