#!/usr/bin/python3

# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Bikroy Automation App"""


import threading
import b_info
import b_links

def startGrabbing():
    threading.Timer(14.0,startGrabbing).start()
    links = b_links.getPageLinks('https://bikroy.com/en/ads')

    for link in links:
        b_info.getInformation(link)

if __name__ == "__main__":
    startGrabbing()