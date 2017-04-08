# Auto login

A python script using Selenium WebDriver which uses Firefox (should be easily portable to Chrome) to login to my
internet portal at specific disconnection times, *00:00 AM* and *8:00 AM* everyday for me. This script keeps a firefox
window open all time. In principle the script can be tweaked to login to any website, as it emulates an user.

**I am not responsible for any wrong use of this script**

## Requirements for running on Windows

* [Firefox](https://www.mozilla.org/en-US/firefox/new/)
* [Python 2.7](https://www.python.org/downloads/release/python-2713/)
* [geckodriver](https://github.com/mozilla/geckodriver/releases)
* Json for Python
* Selenium for Python

## Instructions

1. Install Firefox
2. Install Python 2.7 and make sure to choose **Add Python to PATH** in the component while installing
3. Open a cmd with as admin and use the following following commands:

    `pip install json selenium`
4. Download [geckodriver](https://github.com/mozilla/geckodriver/releases) and extract the *geckodriver.exe* in
`C:/Python27`
5. Download **Autologin.py** from this git and put it in a folder and double click it to run
6. You don't need to close the script. It'll keep running.

## Some things I need to mention
I am not a programming genius. I tried *requests*, *twill* to make this as painless as possible, but unfortunately could
not make them work. You have install all those things I mentioned to get this to work. I believe it is a little trouble
for the one who need autologin at all cost, like me. I'd not recommend this script to basic users who are afraid of
installing applications and libraries in their computer. Otherwise this is a very simple script.
