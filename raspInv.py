#-*- coding: utf-8 -*-
import json, requests, sys
from urllib.request import urlopen
sys.path.append('./../scrInv/')
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {"APCA-API-KEY-ID":API_KEY,"APCA-API-SECRET-KEY": SECRET_KEY}

def getAccount():
	r = requests.get(ACCOUNT_URL,headers=HEADERS)

	return json.loads(r.content)

def createOrder(symbol, qty, side, typep, time_in_force):
	data = {
		"symbol":symbol,
		"qty":qty,
		"side":side,
		"type":typep,
		"time_in_force":time_in_force
	}

	r = requests.post(ORDERS_URL, json=data, headers=HEADERS)

	return json.loads(r.content)

def getOrders():

	r = requests.get(ORDERS_URL, headers=HEADERS)

	return json.loads(r.content)

def selectSymbol():

	data_tbp = ""
	tbjsn    = ""
	auxstr   = ""
	loop_str = ""
	jsn_start = "\"results\":{\"rows\":[{\"symbol\":"
	json_first_end = "}],\"columns\":"
	jsn_end   = "\"priceHint\":"
	jsn_start_idx = 0
	jsn_end_idx   = 0
	auxend   = 0
	endchars = 15
	maxchange1 = 0
	maxchange2 = 0
	maxchange3 = 0
	stck_sys = {}

	## READ WEB PAGE, PARSING.
	url = "https://finance.yahoo.com/most-active?offset=0&count=100"
	response = urlopen(url)

	data_tbp = str(response.read())
	jsn_start_idx = data_tbp.index(jsn_start)
	jsn_end_idx   = data_tbp.index(json_first_end)
	loop_str = data_tbp[jsn_start_idx+10:jsn_end_idx + 2]
	loop_str = loop_str.replace("\\","")
	#PREVIOUS DATA 2900, NOW 20 Values jsn_start_idx+15300

	#print(loop_str)
	    
	for i in range(0,99):
	    auxend = loop_str.index(jsn_end)
	    
	    if(i==98):
	        endchars = 14    
	    
	    auxstr = loop_str[0:auxend+endchars]
	    loop_str = loop_str[auxend+15:-1]
	    tbjsn  = tbjsn + auxstr 

	tbjsn = tbjsn + "]}"
	data = json.loads(tbjsn)
	stck_sys[0] = ""
	stck_sys[1] = ""
	stck_sys[2] = ""

	for stk in data['rows']:
	   if( stk['regularMarketChangePercent']['raw'] > maxchange1 ):
	       maxchange3 = maxchange2
	       stck_sys[2] = stck_sys[1]
	       maxchange2 = maxchange1
	       stck_sys[1] = stck_sys[0]
	       maxchange1 = stk['regularMarketChangePercent']['raw']
	       stck_sys[0] = stk['symbol']

	for sym in stck_sys:
	    print(data['rows']['regularMarketChangePercent']['raw'])
    
def main():
	selectSymbol()

if __name__=="__main__":

	main()
