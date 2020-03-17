#!/usr/bin/python3

# Author: Mohammad Shiblee Noman Ahad
# Email: hello@iamahad.com
# Website: www.iamahad.com
# Github: www.github.com/i-am-ahad


"""Bikroy Automation App"""


import time
import threading
import b_info
import b_links

def startGrabbing():
    toc = time.perf_counter()
    t = threading.Timer(10.0,startGrabbing)
    t.start()
    links = b_links.getPageLinks('https://bikroy.com/en/ads')
    if toc - tic >= 20:
        t.cancel()
    for link in links:
        b_info.getInformation(link)

if __name__ == "__main__":
    tic = time.perf_counter()
    startGrabbing()