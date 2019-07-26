#this will use an online API for scraping data. I will eventually learn how to scrape data on my own
import requests
#to truncate the decimal output to four decimal places
import math 
#requests module needed for https web requests
#i will be using Indian Rupee(INR) as a base currency
url = 'https://api.exchangerate-api.com/v4/latest/INR'
def truncate_dec(amount):
    #we are truncating the float value to 4 decimal places
    return math.trunc(amount*(10**4))/(10**4)
response=requests.get(url)
#get the response from the url
data=response.json()
#that response will be a json. JSON is basically a great way to get data because computers understand it easily
''' this code shows you that the data object that we get will be in the form of a dictionary
print(type(data))
print(data)
'''
print("Enter Currency code like INR, USD etc")
print('We offer conversion between the following currencies')
print(data['rates'].keys())
start=input("Which currency do you have currently?")
end=input("Which currency do you want?")
#I HAVE TO ADD A PART WHERE we check whether these are actual currencies present
start_amt=float(input('Input the amount of money you have '))
end_amt=start_amt*float(data['rates'][end])/float(data['rates'][start])
print(truncate_dec(end_amt))
