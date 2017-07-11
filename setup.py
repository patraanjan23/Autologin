import platform
import tarfile
import zipfile

import wget


def get_firefox():
    pass


def get_geckodriver():
    gecko_url_linux32 = "https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux32" \
                        ".tar.gz "
    gecko_url_linux64 = "https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64" \
                        ".tar.gz "
    gecko_url_win32 = "https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-win32.zip"
    gecko_url_win64 = "https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-win64.zip"

    gecko_url_base_len = len("https://github.com/mozilla/geckodriver/releases/download/v0.17.0/")

    gecko = ""
    if platform.system().lower().startswith('linux'):
        if platform.machine().endswith('64'):
            gecko = wget.download(gecko_url_linux64, out=gecko_url_linux64[gecko_url_base_len:])
        else:
            gecko = wget.download(gecko_url_linux32, out=gecko_url_linux32[gecko_url_base_len:])
        gecko = tarfile.open(gecko, 'r:gz')
        gecko.extractall(".")
        gecko.close()
        pass
    elif platform.system().lower().startswith('win'):
        if platform.machine().endswith('64'):
            gecko = wget.download(gecko_url_win64, out=gecko_url_win64[gecko_url_base_len:])
        else:
            gecko = wget.download(gecko_url_win32, out=gecko_url_win32[gecko_url_base_len:])
        gecko = zipfile.ZipFile(gecko, 'r')
        gecko.extractall(".")
        gecko.close()
        pass
    else:
        print 'can not detect os'


#
# def main():
#     get_geckodriver()


if __name__ == '__main__':
    get_geckodriver()
