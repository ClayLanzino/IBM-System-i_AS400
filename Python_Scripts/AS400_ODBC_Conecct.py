#**************************************************************************************#
# Purpose:  This Script  is designed to illustrate how to use a  connection to an IBM  #
# System i  Server, by using the connect and login methods.                            #
# In addition a database file is connected using a connection (ODBC).                  #
# Note: xx, will be the IP address of the IBM System i Server with which you want      #
# to connect                                                                           #
#**************************************************************************************#
import pyodbc

connection = pyodbc.connect(
    driver='{iSeries Access ODBC Driver}',
    system='xx.xx.xxx.xx',
    uid='UserProfile',
    pwd='Password')
c1 = connection.cursor()

c1.execute("select  field1, field2, field3, field4  from Library_Name.DataBaseFile "  \
           "where  field1 = 'O'  ")
for row in c1:
    print (row)
