# NOTICE: Only for knowledge purpose, extracting title and price from top deals page of AMAZON INDIA website. 

#Runtime ~ 2-5mins

#* IF YOU GET Module not found error then install dependencies first:
# pip install bs4
# pip install pandas
# pip install requests

from bs4 import BeautifulSoup
import pandas as pd
import requests


# Check if URL is active
URL="https://www.amazon.in/s?k=Over+ear+headphones&crid=UHZPEW7W0CV7&sprefix=over+ear+headphone%2Caps%2C827&ref=nb_sb_noss_2"


#Headers of request
#User Agent (get yours and place in <get-your-userAgent> below)- https://www.whatismybrowser.com/detect/what-is-my-user-agent/
HEADERS= ({'User-Agent':'<get-your-userAgent>','Accept-Language':'en-US,en;q=0.5'})

#Request test
webpage=requests.get(URL,headers=HEADERS)

webpage
type(webpage.content)
webpage.content
# Check if code is properly loaded

soup=BeautifulSoup(webpage.content,"html.parser")

soup
# Check if tags are properly loaded

links=soup.find_all("a",attrs={'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

links


# Working on all links
list_link=[]
product_links=[]
def getting_links(links):
  for link in links:
    list_link.append(link.get('href'))
  for link in list_link:
    product_links.append('https://amazon.in'+link)

product_webpages=[]
product_soups=[]
Title=[]
Price=[]
Stocks=[]
Product_dict={}
def get_product_webpage(product_links):
  for link in product_links:
    #print(link)
    product_webpages.append(requests.get(link,headers=HEADERS))
  #print('elements in product_webpages',len(product_webpages))
  for webpage in product_webpages:
    product_soups.append(BeautifulSoup(webpage.content,"html.parser"))

  for product_soup in product_soups:
    P_title=product_soup.find("span",attrs={"id":"productTitle"}).text.strip()
    P_price=product_soup.find("span",attrs={'class':'a-price-whole'}).text.strip('.')+'₹'
    Product_dict[P_title]=P_price
    # Title.append(product_soup.find("span",attrs={"id":"productTitle"}).text.strip())
    # Price.append(product_soup.find("span",attrs={'class':'a-price-whole'}).text.strip('.'))
    # Stocks.append(product_soup.find("span",attrs={'class':'a-size-medium a-color-success'}).text.strip())
 

getting_links(links)
get_product_webpage(product_links)

# ____ TO CHECK DATA BEFORE CREATING CSV
#print('elements in product_dict',len(Product_dict))
#for title in Product_dict:
#   print("Title:",title + ' Price:',Product_dict[title] + '₹')

#Sample Ouput
# elements in product_dict 21
#Title: Philips Audio TAH6506BK/00 Slim & Lightweight Bluetooth Wireless Over Ear Headphones with Active Noise Cancellation, 30 Hrs Playtime & Multipoint Pairing with mic (Black) Price: 3,899₹₹ 
#Title: JBL Tune 760NC, Wireless Over Ear Active Noise Cancellation Headphones with Mic, up to 50 Hours Playtime, Pure Bass, Dual Pairing, AUX & Voice Assistant Support for Mobile Phones (Black) Price: 5,390₹₹
#Title: boAt Rockerz 550 Over Ear Bluetooth Headphones with Upto 20 Hours Playback, 50MM Drivers, Soft Padded Ear Cushions and Physical Noise Isolation, Without Mic (Black) Price: 1,799₹₹       
#Title: Sony WH-CH710N Active Noise Cancelling Wireless Headphones Bluetooth Over The Ear Headset with Mic for Phone-Call, 35Hrs Battery Life, Aux, Quick Charge and Google Assistant Support for 
#Mobiles -Black Price: 6,490₹₹
#Title: boAt Rockerz 550 Bluetooth Wireless Over Ear Headphones with Upto 20 Hours Playback, 50MM Drivers, Soft Padded Ear Cushions and Physical Noise Isolation with Mic (Black Symphony) Price: 
#1,999₹₹
#Title: Redgear Cosmo 7,1 Usb Gaming Wired Over Ear Headphones With Mic With Virtual Surround Sound,50Mm Driver, Rgb Leds & Remote Control(Black) Price: 1,699₹₹
#Title: AKG K72 Wired Over Ear Headphones Without Mic (Black) Price: 2,751₹₹
#Title: ZEBRONICS Zeb-Duke1 Bluetooth Wireless Over Ear Headphones with Mic (Blue) Price: 999₹₹
#Title: boAt Nirvana 751 ANC Hybrid Active Noise Cancelling Bluetooth Wireless Over Ear Headphones with Up to 65H Playtime, ASAP Charge, Ambient Sound Mode, Immersive Sound, Carry Pouch(Silver Sterling) Price: 3,999₹₹
#Title: boAt Rockerz 550 Bluetooth Wireless Over Ear Headphones with Mic Upto 20 Hours Playback, 50MM Drivers, Soft Padded Ear Cushions and Physical Noise Isolation (Red) Price: 1,799₹₹
#Title: JBL Tune 710BT by Harman, 50 Hours Playtime with Quick Charging Wireless Over Ear Headphones with Mic, Dual Pairing, AUX & Voice Assistant Support for Mobile Phones (Black) Price: 4,799₹₹
#Title: ZEBRONICS Zeb-Duke Bluetooth Wireless Over Ear Headphone with Mic (Blue) Price: 1,299₹₹
#Title: Tribit XFree Go Headphones with Mic, Wireless Bluetooth Headphone Over Ear, HiFi Sound,Deep Bass,Lightweight,Type-C Lightening Fast Charge, Voice Control,Black Price: 2,650₹₹
#Title: ZEBRONICS Zeb-Duke Wireless Bluetooth Over The Ear Headphone with Mic - (Green) Price: 1,299₹₹
#Title: Boult Audio Bass Buds Q2 Lightweight Stereo Wired Over Ear Headphones Set with Mic with Deep Bass, Comfortable Ear Cushions, & Long Cord (Black) Price: 649₹₹
#Title: JBL Live 650BTNC, Over Ear Active Noise Cancelling Headphones with Mic, Signature Sound, Quick Charge, Dual Pairing, AUX, Built-in Alexa and Google Assistant (White, Wireless) Price: 5,999₹₹
#Title: Boult Audio ProBass Ranger Over-Ear Wireless Bluetooth Headphones with Microphone, Headset with Long Battery Life Price: 1,799₹₹
#Title: Sony WH-1000XM5 Wireless Industry Leading Active Noise Cancelling Headphones, 8 Mics for Clear Calling, 30Hr Battery, 3 Min Quick Charge = 3 Hours Playback, Multi Point Connectivity, Alexa - Black Price: 26,990₹₹
#Title: boAt Rockerz 550 Bluetooth Wireless Over Ear Headphones with Upto 20 Hours Playback, 50MM Drivers, Soft Padded Ear Cushions and Physical Noise Isolation with Mic (Maroon Maverick) Price: 1,799₹₹
#Title: HP 500 Bluetooth Wireless Over Ear Headphones with Bluetooth 5.0,2X Speed, 4X Connectivity, with Mic,Water-Resistant Design and Up to 20 Hours Battery Life. 1-Year Warranty (2J875Aa) Price: 2,598₹₹


#details

#Importing data from dictionary to dataframe:
adf= pd.DataFrame.from_dict(Product_dict.items())
adf.rename
adf.to_csv("Data")
adf.rename( columns={0:'Title',1:'Price'}, inplace=True )
adf

# IF USING GOOGLE COLAB DOWNLOAD OPION FOR FILE
#from google.colab import files
#files.download("data.csv")
