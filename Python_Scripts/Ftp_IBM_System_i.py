#*************************************************************************************
# Purpose:  This Script  is designed to illustrate how to use a  connection on IBM
# System i  FTP Server, using the connect and login methods with Python.     
#                                                                                               
#*************************************************************************************
from ftplib import FTP
ftp = FTP()
ftp.connect('xx.xx.xxx.xx or Host_name' , 21, -999) 
ftp.login('USER_PROFILE', 'PASSWORD')
print('Welcome to  =>' , ftp.getwelcome())
ftp.close()
