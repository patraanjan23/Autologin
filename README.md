# Auto login

A python script using Selenium WebDriver which uses Firefox (should be easily portable to Chrome) to login to my
internet portal at specific disconnection times, *00:00 AM* and *8:00 AM* everyday for me. This script keeps a firefox
window open all time. In principle the script can be tweaked to login to any website, as it emulates an user.

**I am not responsible for any wrong use of this script**

## Requirements for running on Windows

* [Firefox](https://www.mozilla.org/en-US/firefox/new/)
* [Python 2.7](https://www.python.org/downloads/release/python-2713/)

## Instructions

### Windows

1. Download this repository as a zip and extract at `YOUR_EXTRACTED_FOLDER_PATH`
2. Open **command prompt (admin)** and execute the following commands
    ```
    pip install -r YOUR_EXTRACTED_FOLDER_PATH/requirements.txt
    python setup.py
    python autologin.py
    ```
3. Let the script run. It will auto login at 8AM/12AM

### Linux

1. Open a terminal
2. Do the equivalent windows things but before using `pip` use `sudo -H`

## Some things I need to mention
I am not a programming genius. I tried *requests*, *twill* to make this as painless as possible, but unfortunately could
not make them work. You have install all those things I mentioned to get this to work. I believe it is a little trouble
for the one who need autologin at all cost, like me. I'd not recommend this script to basic users who are afraid of
installing applications and libraries in their computer. Otherwise this is a very simple script.
