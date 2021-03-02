import requests
import sys
import json
import datetime

def check_dates(fdate, tdate, cdate):
   current_day_of_month = datetime.datetime.today().day
   if (cdate.month == 1 or cdate.month == 3 or cdate.month == 5 or cdate.month == 7 or cdate.month == 8 or cdate.month == 10 or cdate.month == 12):
     if ((tdate >= 1 and tdate <= 31) and (fdate >= 1 and fdate <= 31) and (fdate <= tdate) and (tdate <= current_day_of_month and fdate <= current_day_of_month)) :
         return True
     else:
         return False
   elif (cdate.month == 4 or cdate.month == 6 or cdate.month == 9 or cdate.month == 11):
     if ((tdate >=1 and tdate <=30) and (fdate >= 1 and fdate <=31) and (fdate <= tdate) and (tdate <= current_day_of_month and fdate <= current_day_of_month)):
         return True
     else:
         return False
   elif (cdate.month == 2):
     # Python program to check if year is a leap year or not
     year = cdate.year
     # To get year (integer input) from the user
     # year = int(input("Enter a year: "))
     if (year % 4) == 0:
        if (year % 100) == 0:
           if (year % 400) == 0:
              print("{0} is a leap year".format(year))
              if ((tdate >= 1 and tdate <= 29) and (fdate >= 1 and fdate <= 29) and (fdate <= tdate) and (tdate <= current_day_of_month and fdate <= current_day_of_month)):
                  return True
              else:
                  return False
           else:
              #print("{0} is not a leap year".format(year))
              if ((tdate >= 1 and tdate <= 28) and (fdate >= 1 and fdate <= 28) and (fdate <= tdate) and (tdate <= current_day_of_month and fdate <=current_day_of_month)):
                  return True
              else:
                  return False
        else:
           print("{0} is a leap year".format(year))
           if ((tdate >= 1 and tdate <= 29) and (fdate >= 1 and fdate <= 29) and (fdate <= tdate) and (tdate <= current_day_of_month and fdate <= current_day_of_month)):
               return True
           else:
               return False
     else:
        #print("{0} is not a leap year".format(year))
        if ((tdate >=1 and tdate <= 28) and (fdate >=1 and fdate <= 28) and (fdate <= tdate) and (tdate <= current_day_of_month and fdate <= current_day_of_month)):
            return True
        else:
            return False



def Write_JSON_File (jdat1, f_name):
    output_file = open(f_name, 'w')
    original_stdout = sys.stdout
    sys.stdout = output_file
    print(jdat1)
    output_file.close()
    sys.stdout = original_stdout


def CountFrequency(Kino_w_n):

    # Creating an empty dictionary
    freq = {}
    for item in Kino_w_n:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print ("Number %d has appeared %d times"%(key, value))






def get_kino(day_from2,day_to2,current_date, Kino_winningNumbers):
    j = 0
    number_days = day_to2 - day_from2
    if day_to2 == 1 and day_from2 == 1:
        if (current_date.month == 3 or current_date.month == 5 or current_date.month == 7 or current_date.month == 8 or current_date.month == 10 or current_date.month == 12):
           p_c_year = current_date.year
           p_c_month = current_date.month - 1
           if p_c_month == 4 or p_c_month == 6 or p_c_month == 9 or p_c_month == 11:
             if day_from2 == 1 and day_to2 == 1:
                day_from2 = 31
                day_to2 = 31
             elif day_from2 == 1:
                day_from2 = 31
             elif day_to2 == 1:
                day_to2 = 31
           elif p_c_month == 7:
              if day_from2 == 1 and day_to2 == 1:
                 day_from2 = 32
                 day_to2 = 32
              elif day_from2 == 1:
                 day_from2 = 32
              elif day_to2 == 1:
                 day_to2 = 32
           elif p_c_month == 2:
                year = current_date.year
                if (year % 4) == 0:
                   if (year % 100) == 0:
                      if (year % 400) == 0:
                          if day_from2 == 1 and day_to2 == 1:
                             day_from2 = 30
                             day_to2 = 30
                          elif day_from2 == 1:
                             day_from2 = 30
                          elif day_to2 == 1:
                             day_to2 = 30
                      else:
                          if day_from2 == 1 and day_to2 == 1:
                              day_from2 = 29
                              day_to2 = 29
                          elif day_from2 == 1:
                              day_from2 = 29
                          elif day_to2 == 1:
                              day_to2 = 29
                   else:
                      if day_from2 == 1 and day_to2 == 1:
                          day_from2 = 30
                          day_to2 = 30
                      elif day_from2 == 1:
                          day_from2 = 30
                      elif day_to2 == 1:
                          day_to2 = 30
                else:
                    if day_from2 == 1 and day_to2 == 1:
                        day_from2 = 29
                        day_to2 = 29
                    elif day_from2 == 1:
                        day_from2 = 29
                    elif day_to2 == 1:
                        day_to2 = 29

        elif (current_date.month == 4 or current_date.month == 6 or current_date.month == 9 or current_date.month == 11):
            p_c_year = current_date.year
            p_c_month = current_date.month - 1
            if p_c_month == 3 or p_c_month == 5 or p_c_month == 8 or p_c_month == 10:
              if day_from2 == 1 and day_to2 == 1:
                 day_from2 = 32
                 day_to2 = 32
              elif day_from2 == 1:
                 day_from2 = 32
              elif day_to2 == 1:
                 day_to2 = 32
        elif (current_date.month == 1):
            p_c_year = current_date.year - 1
            p_c_month = 12
            if (p_c_month == 12):
              if (day_from2 == 1 and day_to2 == 1):
                 day_from2 = 32
                 day_to2 = 32
              elif day_from2 == 1:
                 day_from2 = 32
              elif day_to2 == 1:
                 day_to2 = 32




    elif day_from2 == 1 and day_to != 1:
            j = 1
            if day_to2 != 1:
                p_c_year = current_date.year
                p_c_month = current_date.month
            else:
                pass
            if (current_date.month == 3 or current_date.month == 5 or current_date.month == 7 or current_date.month == 8 or current_date.month == 10 or current_date.month == 12):
               p_c_year = current_date.year
               p_c_month = current_date.month - 1
               if p_c_month == 4 or p_c_month == 6 or p_c_month == 9 or p_c_month == 11:
                    day_from2 = 31
               elif p_c_month == 7:
                    day_from2 = 32
               elif p_c_month == 2:
                    year = current_date.year
                    if (year % 4) == 0:
                       if (year % 100) == 0:
                          if (year % 400) == 0:
                                 day_from2 = 30
                          else:
                                 day_from2 = 29
                       else:
                          day_from2 = 30
                    else:
                       day_from2 = 29

            elif (current_date.month == 4 or current_date.month == 6 or current_date.month == 9 or current_date.month == 11):
                p_c_year = current_date.year
                p_c_month = current_date.month - 1
                if p_c_month == 3 or p_c_month == 5 or p_c_month == 8 or p_c_month == 10:
                     day_from2 = 32
            elif (current_date.month == 1):
                p_c_year = current_date.year - 1
                p_c_month = 12
                if (p_c_month == 12):
                     day_from2 = 32




    elif day_to2 != 1 and day_from2 != 1:
        j = 0
        p_c_year = current_date.year
        p_c_month = current_date.month




    #print(number_days)
    if (number_days == 0):
     ApiUrl1 = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + str(p_c_year) + "-" + "{:02d}".format(p_c_month) + "-" + "{:02d}".format(day_from2 - 1) + "/" + str(p_c_year) + "-" + "{:02d}".format(p_c_month) + "-" + "{:02d}".format(day_to2 - 1)
     #print(ApiUrl1)
     response = requests.get(ApiUrl1)
     #response = requests.get("https://api.opap.gr/draws/v3.0/1100/draw-date/current_date.year-current_date.month-date_from/current_date.year-current_date.month-date_to")
     status_code=response.status_code
     #print(status_code)
     json_data = response.json()
     # print(json_data)
     #print(json_data.keys())
     Kino_Content = json_data["content"]
     Kino_Firstdraw = Kino_Content[0]
     #print(Kino_Firstdraw)
     Kino_drawId = Kino_Firstdraw["drawId"] + 1
     ApiUrl2 = "https://api.opap.gr/draws/v3.0/1100/" + "{}".format(Kino_drawId)
     #print(ApiUrl2)
     #print(Kino_drawId)
     response2 = requests.get(ApiUrl2)
     status_code2 = response2.status_code
     #print(status_code2)
     json_data2 = response2.json()
     #print(json_data2)

     Kino_results = json_data2["winningNumbers"]["list"]
     for itm in Kino_results:
       Kino_winningNumbers.append(itm)
     #print("The winning numbers are:",Kino_winningNumbers)


    elif (number_days>0):
     i=1
     if j == 1:
         day_from2 = 2
         change_day = day_from2 - 1
     elif j == 0:
         change_day=day_from2 - 1
     while ((change_day <= day_to2) and (i<=number_days+1)):
      ApiUrl1 = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + str(p_c_year) + "-" + "{:02d}".format(p_c_month) + "-" + "{:02d}".format(change_day) + "/" + str(p_c_year) + "-" + "{:02d}".format(p_c_month) + "-" + "{:02d}".format(change_day)
      #print(ApiUrl1)
      response = requests.get(ApiUrl1)
      #response = requests.get("https://api.opap.gr/draws/v3.0/1100/draw-date/current_date.year-current_date.month-date_from/current_date.year-current_date.month-date_to")
      status_code = response.status_code
      #print(status_code)
      json_data = response.json()
      #print(json_data)
      #print(json_data.keys())
      Kino_Content = json_data["content"]
      #print(Kino_Content)
      Kino_Firstdraw = Kino_Content[0]
      Kino_drawId = Kino_Firstdraw["drawId"] + 1
      ApiUrl2 = "https://api.opap.gr/draws/v3.0/1100/" + "{}".format(Kino_drawId)
      #print(ApiUrl2)
      #print(Kino_drawId)
      response2 = requests.get(ApiUrl2)
      status_code2 = response2.status_code
      #print(status_code2)
      json_data2 = response2.json()
      #print(json_data2)

      Kino_results = json_data2["winningNumbers"]["list"]
      for itm in Kino_results:
        Kino_winningNumbers.append(itm)
      #print(Kino_winningNumbers)


      change_day = change_day + 1
      i = i + 1
    #return


def main():

 flag = True

 from datetime import date # Current date time in local system print(datetime.now())
 current_date = date.today()
 #print(current_date)
 print("Current year:", current_date.year)
 print("Current month:", current_date.month)
 Kino_winningNumbers = []


 while flag == True:
  try:
   day_from = input("Insert starting day:  ")
   day_from = day_from.strip()
   while (day_from.isnumeric() != True):
      day_from = input("Insert starting day:  ")
      day_from = day_from.strip()
      if (day_from.isnumeric() == True):
          break
      else:
          pass
   day_from = int(day_from)
   day_to = input("Insert ending day:  ")
   day_to = day_to.strip()
   while (day_to.isnumeric() != True):
      day_to = input("Insert ending day:  ")
      day_to = day_to.strip()
      if (day_to.isnumeric() == True):
          break
      else:
          pass
   day_to = int(day_to)


   while check_dates(day_from, day_to, current_date) != True:
       print("Please enter valid dates")
       day_from = input("Insert starting day:  ")
       day_from = day_from.strip()
       day_from = int(day_from)
       day_to = input("Insert ending day:  ")
       day_to = day_to.strip()
       day_to = int(day_to)

# Get actual Kino results
   get_kino(day_from, day_to,current_date, Kino_winningNumbers)
   print("The winning numbers are:",Kino_winningNumbers)
   print("The frequency of numbers is:")
   CountFrequency(Kino_winningNumbers)

# Ask user if he would like to continue
   answer = input("Do you want to continue?  ")
   if (answer.upper().strip() == "NO"):
       break
   elif (answer.upper().strip() =="YES"):
       Kino_winningNumbers.clear()
       continue
   while (answer.upper() != "NO" and answer.upper() != "YES"):
     answer = input("Do you want to continue? Acceptable answers: Yes or No ")
     cans = answer.upper()
     if cans.strip() == "NO":
       flag = False
       break
       #sys.exit()
     elif cans.strip() == "YES":
       Kino_winningNumbers.clear()
       continue


  except TypeError:
      print("You didn\'t respond with integer value")
      continue


if __name__ == "__main__":
    main()
