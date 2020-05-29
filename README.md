# Mine Digital Exchange - Python client
Python client for Mine Digital Exchange API version 2 https://minedigital.exchange/

---
A simple python client for Mine Digital Exchange API version 2. Not all API calls have been implemented. Official documentation can be found at: https://bctv2.docs.apiary.io/#
---
## Installation
Clone the Git repository:
```
git clone https://github.com/St0n3M0nKeY/MineDigital-APIv2-wrapper.git
```
Go to the folder of the cloned repository and run:
```
python setup.py install
```
Run Python and import the Mine Digital client.

## Dependencies
Install libs
```
pip install -r .\requirements.txt
```

## Usage - REST API - Public
Get Market data (ticker)
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(None, None)

currency_pair = "BTCUSD"

print(mine.get_market_data(currency_pair))
```

Get Orderbook data
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(None, None)

currency_pair = "BTCUSD"

print(mine.get_orderbook_data(currency_pair))
```


## Usage - REST API - Private
Account Information
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.get_money_info())
```

Wallet History
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.get_wallet_history(currency_pair, page_num, from_timestamp, to_timestamp))
```

Place Limit Order
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.money_order_add_limit(currency_pair, price, amount, side)) 
```

Place Market Order
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.money_order_add_market(currency_pair, amount, side))
```

Cancel Order
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.order_cancel(currency_pair, order_id))
```

Completed Orders
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.order_result(currency_pair))
```

Open Orders
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.open_orders(currency_pair))
```

Request for Quote
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.request_for_quote(currency_pair, side, amount))
```

Executed Trades
```
import minedigitalv2

mine = minedigitalv2.MineAPIv2(api_key, api_secret)

print(mine.get_executed_trades(from_timestamp, to_timestamp))
```

## Compatibility

This code has been tested on:

- Python 3.7.2


## TODO

- Implement all API version 2 calls available for Mine digital Exchange.
