from datetime import date, datetime, timedelta
from tsendSms import *
import mysql.connector
import MySQLdb
import nexmo
import os


# inserts skylabel, buydate and household Id in the mySql database
def insertHH(hid,pid):
    dbHost=os.getenv('DBHOST')
    dbDb=os.getenv('DATABASE')
    dbUser=os.getenv('DBUSER')
    dbPwd=os.getenv('DBPWD')
    db= MySQLdb.connect(user=dbUser, passwd=dbPwd, host=dbHost,db=dbDb)

    cur = db.cursor()
    tday=datetime.now().date()
    pid=pid.replace(" ","")
    print(pid)
    cur.execute('''insert into CM_Household(householdId, sku,buydate)
	 VALUES(%s,%s,%s)''', (hid,pid,tday))

    db.commit()
    db.close()


def getFoodList():

    dbHost=os.getenv('DBHOST')
    dbDb=os.getenv('DATABASE')
    dbUser=os.getenv('DBUSER')
    dbPwd=os.getenv('DBPWD')
    cnx= MySQLdb.connect(user=dbUser, passwd=dbPwd, host=dbHost, db=dbDb)

    cur = cnx.cursor()
    today=datetime.now().date()

    #query=("select b.skyLabel, a.buyDate from CM_Household AS a INNER JOIN CM_SKU AS b ON a.sku=b.sku and a.buyDate+b.expiryDays<=curdate()+6")
    query=("select b.skyLabel, a.buyDate from CM_Household AS a INNER JOIN CM_SKU AS b ON LOCATE(CONVERT(a.sku,CHAR),CONVERT(b.sku,CHAR))>0" )
    cur.execute(query)
    
    final_str=''
    for (skyLabel,buyDate) in cur:
      print("{}, {}".format(skyLabel,buyDate))
      final_str = "%s,%s,%s\n"%(final_str,skyLabel,buyDate)
    cur.close()
    cnx.close()
    #print(final_str)
    sendTwilioSMS(final_str)
getFoodList()

