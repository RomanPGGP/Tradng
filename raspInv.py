#-*- coding: utf-8 -*-
import json, requests, sys
sys.path.append('./../scrInv/')
from config import *

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
HEADERS = {"APCA-API-KEY-ID":API_KEY,"APCA-API-SECRET-KEY": SECRET_KEY}

def getAccount():
	print('printing stuff:')
	print(API_KEY)
	print(SECRET_KEY)

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

def main():
	print(getAccount())



if __name__=="__main__":

	main()
