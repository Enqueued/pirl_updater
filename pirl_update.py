#!/usr/bin/python
import urllib2
import time
import datetime
from bs4 import BeautifulSoup
old_amt = None
while True:
	html = urllib2.urlopen('https://walletinvestor.com/converter/pirl/usd/1').read()
	soup = BeautifulSoup(html, "lxml")
	soup.prettify()

	spanz = soup.find_all('span', {'class' : 'converter-title-amount'})
	for span in spanz:
                current_amt = span.get_text()

        if old_amt == None:
            started_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            print "Started on " + started_on
            old_amt = current_amt
	    print "1 Pirl is worth: " + old_amt + " USD"
        if float(old_amt) != float(current_amt):
            old_amt = current_amt
            print "updated!"
	    print "1 Pirl is worth: " + old_amt + " USD"

	time.sleep(5)
