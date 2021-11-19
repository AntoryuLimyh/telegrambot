
import telebot
import yfinance as yf
import os
from dotenv import dotenv_values

APIKEY = dotenv_values(".env")['API_Key']


bot = telebot.TeleBot(APIKEY)


def stock_request(message):
  request = message.text.split()
  if len(request) < 2:
    return False
  else:
    return True


@bot.message_handler(func=stock_request)
def sendsum(message):
  request = message.text.split()[1]
  
  ticker = yf.Ticker(request)

  bot.send_message(message.chat.id, 'ALim Bot Loading ....')

  try:
    Current = ticker.get_info()['currentPrice']
    bot.send_message(message.chat.id,'Last Price - ' + str(Current) + '\n\n')
    #bot.send_message(message.chat.id, Current)
  except:
    pass

  


  try:
    sharesOutstanding = ticker.get_info()['sharesOutstanding']/1000000
    bot.send_message(message.chat.id,'Shares Outstanding (M) - '+ str(round(sharesOutstanding,3)))
    #bot.send_message(message.chat.id, sharesOutstanding)
  except:
    pass

  

  try:
    MarketCap = ticker.get_info()['marketCap']/100000000
    bot.send_message(message.chat.id,'Market Cap (B) - '+ str(round(MarketCap,3)))
    #bot.send_message(message.chat.id, MarketCap)
  except:
    pass
  
  
  try:
    Beta =ticker.get_info()['beta']
    bot.send_message(message.chat.id,'Beta(5yr) - '+ str(round(Beta,2)))
    #bot.send_message(message.chat.id, Beta)
  except:
    pass

  try:
    PTB = ticker.get_info()['priceToBook']
    bot.send_message(message.chat.id,'Price to Book - '+ str(round(PTB,2)))
    #bot.send_message(message.chat.id, PTB)
  except:
    pass

  try:
    RevShare =ticker.get_info()['revenuePerShare']
    bot.send_message(message.chat.id,'Rev / Share - '+ str(round(RevShare,2)))
    #bot.send_message(message.chat.id, RevShare)
  except:
    pass

  try:
    Cashshare = ticker.get_info()['totalCashPerShare']
    bot.send_message(message.chat.id,'Cash / Share - '+ str(round(Cashshare,2)))
    #bot.send_message(message.chat.id, Cashshare)
  except:
    pass

  try:
    TrailingEPS = ticker.get_info()['trailingEps']
    bot.send_message(message.chat.id,'Trailing EPS - '+ str(round(TrailingEPS,3)))
    #bot.send_message(message.chat.id, TrailingEPS)
  except:
    pass

  try:
    TrailingPE = ticker.get_info()['trailingPE']
    bot.send_message(message.chat.id,'Trailing PE - '+ str(round(TrailingPE,2)))
    #bot.send_message(message.chat.id, TrailingPE)
  except:
    pass


  try:
    GP = ticker.get_info()['grossMargins']*100
    bot.send_message(message.chat.id,'Gross Profits % - '+ str(round(GP,2)))
    #bot.send_message(message.chat.id, GP)
  except:
    pass

  
  try:
    OpMargin = ticker.get_info()['operatingMargins']*100
    bot.send_message(message.chat.id,'Operating Margin % - '+ str(round(OpMargin,2)))
    #bot.send_message(message.chat.id, OpMargin)
  except:
    pass

    
  try:
    ProfitMargin =ticker.get_info()['profitMargins']*100
    bot.send_message(message.chat.id,'Profit Margin % - ' + str(round(ProfitMargin,2)))
    #bot.send_message(message.chat.id, ProfitMargin)
  except:
    pass


  try:
    CR = ticker.get_info()['currentRatio']
    bot.send_message(message.chat.id,'Quick Ratio - '+ str(round(CR,2)))
    QR = ticker.get_info()['quickRatio']
    bot.send_message(message.chat.id,'Quick Ratio - '+ str(round(QR,2)))
    #bot.send_message(message.chat.id, sharesOutstanding)
  except:
    pass

  try:
    ROA = ticker.get_info()['returnOnAssets']*100
    bot.send_message(message.chat.id,'ROA - ' + str(round(ROA,2)))
    #bot.send_message(message.chat.id, ROA)
  except:
    pass

  try:
    ROE  = ticker.get_info()['returnOnEquity']*100
    bot.send_message(message.chat.id,'ROE - ' + str(round(ROE,2)))
    #bot.send_message(message.chat.id, ROE)

  except:
    pass 

  try: 
    Sector = ticker.get_info()['sector']
    bot.send_message(message.chat.id,'Sector - ' + Sector)
  except:
    pass

  try:
   Bizsum = ticker.get_info()['longBusinessSummary']
   bot.send_message(message.chat.id,'Business Summary' + '\n\n' + Bizsum)
   #bot.send_message(message.chat.id,Bizsum)
  except:
    pass

  try:
    news = ticker.news
  
    for i in news:
      pub = i['publisher']
      title = i['title']
      bot.send_message(message.chat.id,'Source - ' + pub + '\n\n' + title )
      
    #  bot.send_message(message.chat.id,'News Summary - ' + title )
      
  except:
    pass
 

bot.polling()

