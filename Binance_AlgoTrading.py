
import time
from binance.client import Client



api_key='your key here'
api_secret='your secret here'

client = Client(api_key, api_secret)


yanas=0
quantity=800
symbol='XRPBTC'
b=0.00000015

b= '{:0.0{}f}'.format(b, 8)
        

def get_ticker():
    tickers = client.get_ticker()
    for i in tickers:
        if i["symbol"]=="XRPBTC":
            print(i)

get_ticker()

def last_trade_side():
    a=client.get_all_orders(symbol='XRPBTC')
    a=a[-1]['side']
    return a
    
def last_trade_amount():
    a=client.get_all_orders(symbol='XRPBTC')
    a=a[-1]['price']
    a=float(a)
    a=a-yanas
    precision = 8
    a = '{:0.0{}f}'.format(a, precision)
    return a


def balance():
    a=client.get_asset_balance(asset='BTC')
    c=float(a['free'])+float(a['locked'])
    b=client.get_asset_balance(asset='XRP')
    d=float(b['free'])+float(b['locked'])
    tickers = client.get_ticker()
    for i in tickers:
        if i["symbol"]=="BTCUSDT":
            z=i['lastPrice']
            z=float(z)
        if i["symbol"]=="XRPBTC":
            x=i['lastPrice']
            x=float(x)
            a=c+d*x
            z=a*z
            z='{:0.0{}f}'.format(z, 8)
            a='{:0.0{}f}'.format(a, 8)
            b=d+c/x
            b='{:0.0{}f}'.format(b, 8)
  
            return a,b,z
#print(balance())

#print(last_trade_side(),last_trade_amount())

#def ma_30():
#    klines = client.get_historical_klines("XRPBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
#    sum=0
#    for i in range(1,31):
#        sum = sum+float(klines[-i][4])
##        print(klines[-i][4])
#    average=sum/30
#    precision = 8
#    average = '{:0.0{}f}'.format(average, precision)
#    return average
#    
##ma_30()
#
#def ma_20():
#    klines = client.get_historical_klines("XRPBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
#    sum=0
#    for i in range(1,21):
#        sum = sum+float(klines[-i][4])
##        print(klines[-i][4])
#    average=sum/20
#    precision = 8
#    average = '{:0.0{}f}'.format(average, precision)
#    return average
    
#ma_20()
        
def get_sell_price():
    tickers = client.get_ticker()
    for i in tickers:
        if i["symbol"]=="XRPBTC":
            a=i['askPrice']
            a=float(a)
            a=a-yanas
            precision = 8
            price = '{:0.0{}f}'.format(a, precision)
            return price
#print('sell',get_sell_price())

def get_buy_price():
    tickers = client.get_ticker()
    for i in tickers:
        if i["symbol"]=="XRPBTC":
            a=i['bidPrice']
            a=float(a)
            a=a+yanas
            precision = 8
            price = '{:0.0{}f}'.format(a, precision)
            return price
        
#print('buy',get_buy_price())


def _buy(quantity,price,symbol):
    client.order_limit_buy(
    symbol=symbol,
    quantity=quantity,
    price=price)
    
#_buy(quantity,get_buy_price(),symbol)

def _sell(quantity,price,symbol):
    client.order_limit_sell(
    symbol=symbol,
    quantity=quantity,
    price=price)
    
#_sell(quantity,get_sell_price(),symbol)
    
    
def ma():
    klines = client.get_historical_klines("XRPBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    sum=0
    sumg=0
    
    
    for i in range(1,31):
        sum = sum+float(klines[-i][4])
        sumg = sumg+float(klines[-i-1][4])
#        print(klines[-i][4])
    otuz=sum/30
    otuzg=sumg/30
    precision = 8
    otuz = '{:0.0{}f}'.format(otuz, precision)
    otuzg = '{:0.0{}f}'.format(otuzg, precision)

    ssum=0
    ssumg=0
    
    
    for i in range(1,21):
        ssum = ssum+float(klines[-i][4])
        ssumg = ssumg+float(klines[-i-1][4])
#        print(klines[-i][4])
    yirmi=ssum/20
    yirmig=ssumg/20
    precision = 8
    yirmi = '{:0.0{}f}'.format(yirmi, precision)
    yirmig = '{:0.0{}f}'.format(yirmig, precision)
    
    print('30 eski',otuzg,yirmig,'20 eski')
    print('30 ma  ',otuz,yirmi,'20 ma')
    
#'YIRMI BUYUK'    
    if yirmig>otuzg:
        print('satacagim',balance())
        if otuz==yirmi:
            if last_trade_side()=='BUY':
                if last_trade_amount()+b<get_sell_price():    
                    print('sell beybi',get_sell_price(),balance())
                    _sell(quantity,get_sell_price(),symbol)
        
#'OTUZ BUYUK'            
    if otuzg>yirmig:
        print('alacagim',balance())
        if otuz==yirmi:
            if last_trade_side()=='SELL':
                if last_trade_amount()>get_buy_price()+b:   
                    print('buy beybi',get_buy_price(),balance())
                    _buy(quantity,get_buy_price(),symbol)
            

while True:

    ma()
    time.sleep(60)
    
    
#while True:
#    print('20 is',ma_20(),'30 is',ma_30())
#    if ma_20()<ma_30():
#        time.sleep(5)
#        if ma_20()==ma_30():
#            print('AL AL Al AL Koy amina KOY KOY KOY')
#    if ma_20()>ma_30():
#        time.sleep(5)
#        if ma_20()==ma_30():
#            print('SAT SAT SAT SAT Koy amina KOY KOY KOY')
            
