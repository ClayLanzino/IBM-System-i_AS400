#**************************************************************************************#
# Purpose:  This Script  is designed to illustrate how to use a  connection to an IBM  #
# System i  Server, by using the connect and login methods.                            #
#  In addition a database file is connected using a connection (ODBC).                 #                                      #
#**************************************************************************************#
import pyodbc

connection = pyodbc.connect(
    driver='{iSeries Access ODBC Driver}',
    system='12.34.567.89',
    uid='CLAGUT',
    pwd='CLAGUT')
c1 = connection.cursor()

c1.execute("select  employee_type, employee_code, employee_name, monthly_salary  from dblibrary.nmpp000 "  \
           "where  employee_type = 'O'  ")
for row in c1:
    print (row)
