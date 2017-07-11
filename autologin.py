import json
import time

import ntplib
from selenium import webdriver

CONFIG_FN = "config.json"


def update_config():
    print "Creating new configuration. Enter the following"

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


def login():
    config = check_config()

    _url = config['url']
    _username = str(config['username'])
    _password = str(config['password'])

    print _url, _username, _password

    firefox = webdriver.Firefox()
    time.sleep(1)
    firefox.get(_url)
    time.sleep(4)

    script_1 = "document.getElementById('username').setAttribute('value', '" + _username + "')"
    script_2 = "document.getElementById('password').setAttribute('value', '" + _password + "')"
    firefox.execute_script(script_1)
    firefox.execute_script(script_2)

    login_attempt = firefox.find_element_by_xpath("//*[@type='submit']")
    print login_attempt.submit()
    time.sleep(10)

    firefox.quit()


def main():
    ntp = ntplib.NTPClient()
    print "make sure the machine is connected to internet while launching the script\nso it can get real time delta for your place"
    time_delta = ntp.request('in.pool.ntp.org').tx_time - time.mktime(time.gmtime()) + 5 * 3600 + 30 * 60
    while True:
        now = time.strftime("%H:%M", time.gmtime(time.mktime(time.gmtime()) + time_delta))
        print now
        if now == "00:00" or now == "08:00":
            login()
            time.sleep(50)
        else:
            time.sleep(5)
            pass


if __name__ == '__main__':
    main()
