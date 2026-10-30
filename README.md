# Python – IBM i (AS400) Payroll Interface

A Python-based automation tool that bridges a Windows PC and an IBM i (AS400) server to process payroll data efficiently. The system reads employee salaries from an '.xls' file, converts them to '.csv', and automatically updates the records in the IBM DB2/400 database.

![Python](https://img.shields.io/badge/Python-3.8-3776AB?style=for-the-badge&logo=python&logoColor=white)
![IBM i](https://img.shields.io/badge/IBM%20i-AS%2F400-052FAD?style=for-the-badge&logo=ibm&logoColor=white)
![DB2](https://img.shields.io/badge/DB2%2F400-052FAD?style=for-the-badge&logo=ibm&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10%2B-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 Overview

This project provides a simple and reliable way for payroll teams to **update employee salaries directly in an IBM i (AS400) system** without needing to know RPG or DB2 syntax.

The user works with an Excel template ('.xls') containing worker records and base salaries. The tool:

1. Reads and validates the '.xls' file.
2. Converts the data into a '.csv' format.
3. Connects to the IBM i server (via ODBC / FTP).
4. Updates the salary records in the **IBM DB2/400** database automatically.

This reduces manual data entry, avoids human error, and speeds up the payroll cycle.

---

## ✨ Features

- ✅ **Easy installation** – no complex setup required for end users.
- 🔄 **Bulk data conversion** – handles large volumes of payroll data.
- 🖥️ **Windows compatible** – runs on Windows 10 or later.
- 🐍 **Python 3.8** – leverages simple, readable scripting.
- 🏢 **IBM i (AS400) OS 6.0+ compatible** – supports both classic and modern IBM i environments.
- 🔒 **Restricted access** – only users with the executable file installed on their PC can run the system.
- 📊 **Excel → CSV → DB2/400 pipeline** – fully automated.

---

## ⚙️ How It Works

```text
[ .xls file with employee salaries ]
              │
              ▼
     [ payroll.py / PAYROLL.exe ]
              │
              ▼
    [ .csv intermediate file ]
              │
              ▼
  [ ODBC / FTP connection to IBM i ]
              │
              ▼
  [ Salary records updated in DB2/400 ]
---
📱 Interface Preview
1. PAYROLL Confirmation Dialog
https://raw.githubusercontent.com/ClayLanzino/IBM-System-i_AS400/master/images/payroll.png

2. Payroll Execution Console (Python & DB2/400 Connection)
https://raw.githubusercontent.com/ClayLanzino/IBM-System-i_AS400/master/images/payroll.exe.png

Confirmation dialog of the PAYROLL executable. The user confirms the execution, and the system converts the .xls file to .csv and updates the salaries in the IBM DB2/400 database.
