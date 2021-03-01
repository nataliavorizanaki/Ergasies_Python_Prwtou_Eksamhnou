import requests
import json
import ast
import os



def main():
  file_name = input("Please insert file name  ")
  file_name = file_name.strip()
  if os.path.exists(file_name):
     infile = open(file_name, 'r')
     contents = infile.read()
  else:
     print("The file does not exist")
     flag = True
     while flag == True:
         file_name = input("Please insert file name  ")
         file_name = file_name.strip()
         if os.path.exists(file_name):
             infile = open(file_name, 'r')
             contents = infile.read()
             flag = False
         else:
             continue

  #infile = open(file_name, 'r')
  #contents = infile.read()
  dict_file = {}
  dict_file = ast.literal_eval(contents)
  print(dict_file)
  list_crypto = make_list_of_cryptocurrencies()
  dict_file2 = list(dict_file.keys())
  #print(dict_file2)
  dict_file3 = list(dict_file.values())
  #print(dict_file3)
  for k in dict_file2:
         if (k not in list_crypto):
              print("Error,",k,"cryptocurrency does not exist")
         else:
              pass
  for x in dict_file3:
         if (type(x) != float and type(x) != int):
             print("Error",x,"is not numeric")
         else:
             pass
  get_coin_data(dict_file2,dict_file3)



  infile.close()




def get_coin_data(d_f2,d_f3):

  #APIurl = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH,DASH&tsyms=BTC,USD,EUR&api_key=INSERT-YOUR-API-KEY-HERE"
  i = 0
  sum = 0
  for x in d_f2:
    APIurl = "https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=EUR&api_key=362c2c77e39aae573ec3ff7ff8ea564b071cff35cdc14ee4b59cdd5d21dde8b3".format(x)
    print("\n")
    #print(APIurl)
    response = requests.get(APIurl)
    print(response)
    status_code = response.status_code
    #print(status_code)
    json_data = response.json()
    print(json_data)
    #print("Keys :", json_data.keys())
    amount_in_euro = d_f3[i] * json_data[x]['EUR']
    r_amount_in_euro=float("{:.2f}".format(amount_in_euro))
    print("\n")
    print("The amount in euro is:  ", r_amount_in_euro)
    i = i + 1
    sum = sum + amount_in_euro
  r_sum = float("{:.2f}".format(sum))
  print("\n")
  print("The total amount in euro for all cryptocurrencies is:  ",r_sum)


def make_list_of_cryptocurrencies():
    list_of_cryptocurrencies = []
    my_file = open("crypto.txt", "r")
    content = my_file.read()
    list_of_cryptocurrencies = content.splitlines()
    my_file.close()
    return list_of_cryptocurrencies



main()
