#defining a function curconv() which will take currency and amount as input and then convert and return the amount in US dollars 
import pandas as pd

def curconv(currency, amount):
    df = pd.read_csv('currencies.txt', sep="\t",header=None)
    count = 0
    for index, row in df.iterrows():
        if currency.upper() == row[0]: 
            conv_amount = amount*row[1]
            count += 1
            
    if count != 0:
        print("Amount conversion for {} is {}".format(currency,conv_amount))
    else:
        print("Currencies Doesn't exist in file")

curconv('as', 100 )