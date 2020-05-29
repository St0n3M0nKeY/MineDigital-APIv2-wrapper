import base64
import hashlib
import hmac
import time
import json
import requests
import urllib.parse

class MineAPIv2:

    def __init__(self, key, secret):
        self.api_path = "api/2/"
        self.base_url = f'https://trade.minedigital.exchange/{self.api_path}'
        if key is not None and secret is not None:
            self.__key = key
            self.__secret = base64.b64decode(secret)

    def gen_tonce(self):
        return str(int(time.time() * 1e6))

    def get_request(self, path):
        try:
            return requests.get(self.base_url + path).json()
        except Exception as error:
            print("SERVER ERROR GET REQUEST: %s" % error)
            return False

    def post_request(self, path, data):
        try:
            message = (path + chr(0) + data).encode()
            hmac_obj = hmac.new(self.__secret, message, hashlib.sha512)
            hmac_sign = base64.b64encode(hmac_obj.digest())

            header = {
                'Content-Type': 'application/json',
                'User-Agent': '',
                'Rest-Key': self.__key,
                'Rest-Sign': hmac_sign,
            }
            response = requests.post(self.base_url + path, data, headers=header, verify=True)
            json_resp = response.json()
            return json_resp
        except Exception as error:
            print("SERVER ERROR POST REQUEST: %s" % error)
            return False

    ##########################################
    #### Private API Requests ################
    ##########################################
    def get_money_info(self):
        '''
        https://bctv2.docs.apiary.io/#reference/account/moneyinfo
        This method returns the balance, available balance, 
        daily withdrawal limit and maximum withdraw for every 
        currency in your account.
        '''
        path = "money/info"
        params = {}
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def get_wallet_history(self, currency_pair, page_num, from_timestamp, to_timestamp):
        '''
        https://bctv2.docs.apiary.io/#reference/account/moneywallethistory
        Wallet History
        A full history of the transaction in each of your wallet. 
        Transactions include buy, sell, deposit, withdrawal and fees.
        '''
        path = "money/wallet/history"
        params = {}
        params['currency'] = currency_pair
        params['page'] = page_num
        params['from'] = from_timestamp
        params['to'] = to_timestamp
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))      

    def money_order_add_limit(self, currency_pair, price, amount, side):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/currencypairmoneyorderadd
        Place a limit order
        '''
        path = f"{currency_pair}/money/order/add"
        params = {}
        params['type'] = side
        params['amount_int'] = amount
        params['price_int'] = price
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def money_order_add_market(self, currency_pair, amount, side):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/currencypairmoneyorderadd
        Place a market order
        '''
        path = f"{currency_pair}/money/order/add"
        params = {}
        params['type'] = side
        params['amount_int'] = amount
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def order_cancel(self, currency_pair, order_id):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/currencypairmoneyordercancel
        Cancel an open order
        '''
        path = f"{currency_pair}/money/order/cancel"
        params = {}
        params['oid'] = order_id
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def order_result(self, currency_pair):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/currencypairmoneyorders
        Order Result
        Enquire the result of a completed order. 
        Get detail information such as average cost, 
        total amount and of an executed order.
        '''
        path = f"{currency_pair}/money/order/result"
        params = {}
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def open_orders(self, currency_pair):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/currencypairmoneyorders
        Open orders
        Returns limit orders in pending state submission to the orderbook, or already active (they may be partially filled).
        Note you could have market orders in state pending that would not be retrieved by this request.
        '''
        path = f"{currency_pair}/money/orders"
        params = {}
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def request_for_quote(self, currency_pair, side, amount):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/currencypairmoneyorderquote
        Order Quote.
        Quote an estimated amount to buy/sell a currency pair
        '''
        path = f"{currency_pair}/money/order/quote"
        params = {}
        params['type'] = side
        params['amount'] = amount
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))

    def get_executed_trades(self, from_timestamp, to_timestamp):
        '''
        https://bctv2.docs.apiary.io/#reference/trade/moneytradelist
        Get a list of executed trade
        '''
        path = "money/trade/list"
        params = {}
        params['from'] = from_timestamp
        params['to'] = to_timestamp
        params['tonce'] = self.gen_tonce()
        return self.post_request(path, urllib.parse.urlencode(params))
    
    ##########################################
    #### Public API Requests #################
    ##########################################
    def get_market_data(self, currency_pair):
        '''
        https://bctv2.docs.apiary.io/#reference/market-data
        Get the most recent ticker for a currency pair
        '''
        path = f"{currency_pair}/money/ticker"
        return self.get_request(path)

    def get_orderbook_data(self, currency_pair):
        '''
        https://bctv2.docs.apiary.io/#reference/market-data/currencypairmoneydepthfull
        Get a complete copy of the order book on a particular currency pair.
        '''
        path = f"{currency_pair}/money/depth/full"
        return self.get_request(path)
