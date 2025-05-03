# Language: Python 3.9
#  -*- coding: utf-8 -*-

""" Python script to reading an Excel file and write the output to a CSV file. Additionally it connects to the IBM i
    Server and sends to the Integrated File System (IFS) the CSV file.
     On November 05 2022 by Clay Lancini """

import csv
import sys
import subprocess
from ftplib import FTP
import xlrd
from decouple import config
import time
from colorama import init, Fore

# start colorama
init()


def csv_from_excel():
    Counter = 0
    try:
        wb = xlrd.open_workbook('Data_EO.xls')
        sh = wb.sheet_by_index(0)
    except FileNotFoundError:
        print(Fore.RED + "Opening the Data_EO.xls file failed, Please make sure that the file exists in the folder.")
        waiting_time = 13
        time.sleep(waiting_time)
        sys.exit(1)

    """ In order to avoid that the numeric fields of the csv file take an invalid value and as a consequence
    the RPGILE program aborts on the IBM AS/400 server, the newline parameter must be included when opening 
    the CSV file.  """

    csv_file = open('Data_EO.csv', 'w', newline="")
    wr = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)

    for row in range(sh.nrows):
        wr.writerow(sh.row_values(row))
        Counter += 1
        print(sh.row_values(row))
    print(Fore.GREEN + 'Total records in the csv file ------> ', Counter)
    csv_file.close()


def ftp_upload():
    file_transfer_name = "./Data_EO.csv"
    print('')

    # Open ftp connection to the AS/400 server to start csv file transfer.
    try:
        print(Fore.YELLOW + 'Establishing connection with IBM i Server (AS/400), please wait...')

        ftp = FTP()
        ftp.connect(config('Host'), 21, -999)
        ftp.login(config('user'), config('password'))
        print(Fore.GREEN + 'Connection established with ==>', ftp.getwelcome())

        print(ftp.cwd("/tmp"))

        # Transferring csv file to IBM i IFS folder
        with open(file_transfer_name, 'rb') as csv_file:
            storeCommand = ftp.storlines('STORE Data_EO.csv', csv_file)
            ftpResponse = storeCommand
            print(ftpResponse, file_transfer_name)

        ftp.quit()
        ftp.close()

        """ Call the interface to connect to IBM i - AS/400 via ftp and invoke the update and report 
        issuing programs... """
        completed_process = subprocess.run('ftp_cl_as400.bat')
        print(completed_process)

        # successfully completed process ...
        completed_process = subprocess.run('python payroll_process_done.py')
        print(completed_process)

    except Exception as err:
        print(Fore.RED + 'Could not establish connection to the server ===>:', config('Host'), str(err))
        waiting_time = 13
        time.sleep(waiting_time)


if __name__ != "__main__":
    pass
# calls the csv_from_excel function:
else:
    csv_from_excel()
    ftp_upload()
