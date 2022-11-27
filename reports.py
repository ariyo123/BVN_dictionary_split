import os
from unittest import result
import csv
import datetime
import time
import mysql.connector as msql
from mysql.connector import Error



#from datetime import date, timedelta
import time
print("\n\n\n\n")
print("you're about to see the status of your webservices")
#get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#get cureent date
CurrentDate=datetime.date.today()  
days = datetime.timedelta(2)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date) 
path1='C:/python_work/bvn_user_actitities/bank_code.csv'
with open(path1, 'r') as file_object:
    lines=file_object.read()
        #print(lines)
    contents1=lines.split()
    #print(contents1)

institutions_list=[*csv.DictReader(open('BANK_TABLE.csv'))]; #print(institutions_list)


#calling the webservices dictionary to confirm the status

for code in contents1[:]:
    for institutions in institutions_list[:]:
        #print(institutions)
        if institutions['bankCode']==f'{code}':
            bankCode=institutions['bankCode']
            bankName=institutions['bankName']
            dest=institutions['dest']
            #print(bankCode)
            #print(bankName)
            #print(dest)
            # Directory
            directory = bankName

            # Parent Directory path
            parent_dir = f"{dest}"
            # Path
            path = os.path.join(parent_dir, directory)
            print(path)

            # Create the directory
            # 'GeeksForGeeks' in
            # '/home / User / Documents'
            os.mkdir(path)
           #print(f"Directory {bankName} created")
            #pass
            # textfile = open(f"{path}/{bankName}.txt", "a")
            # textfile.write('ID,ACTION,IPADDRESS,ACTIONDATE,EMAIL,BANKCODE,DETAILS,ITEMSEARCHCOUNT,AUDITTYPE\n')
            conn = msql.connect(host='127.0.0.1', database='housing_data', user='u', password='@')
  
            # get cursor object
            cursor= conn.cursor()
            sql=f"SELECT * FROM housing_data.useractivity where BANKCODE = '{bankCode}' and ACTIONDATE between '{final_date} 00:00:00' and '{final_date} 23:59:59';"

            # execute your query
            cursor.execute(sql)
            
            # fetch all the matching rows 
            result = cursor.fetchall()
            #location=f"{path}.txt"
            with open(f"{path}/{bankName}.txt", 'a', newline = '') as csvfile:
                fieldnames=['ID', 'ACTION', 'IPADDRESS', 'ACTIONDATE', 'EMAIL', 'BANKCODE', 'DETAILS', 'ITEMSEARCHCOUNT', 'AUDITTYPE']
                my_writer = csv.writer(csvfile, delimiter = ',')
                my_writer.writerow(fieldnames)
                  
                #my_writer = open(f"{path}/{bankName}.txt", "a")
                
            # loop through the rows
                for row in result:
                    print(row)
                    print("\n")
                    my_writer.writerow(row)
            cursor.close()    
        
      
