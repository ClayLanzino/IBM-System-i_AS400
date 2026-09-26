# Python – IBM i (AS/400) Payroll Interface

A Python-based automation tool that bridges a Windows PC and an IBM i (AS/400) server to process payroll data efficiently. The system reads employee salaries from an '.xls' file, converts them to '.csv', and automatically updates the records in the IBM DB2/400 database.

![Python](https://img.shields.io/badge/Python-3.8-3776AB?style=for-the-badge&logo=python&logoColor=white)
![IBM i](https://img.shields.io/badge/IBM%20i-AS%2F400-052FAD?style=for-the-badge&logo=ibm&logoColor=white)
![DB2](https://img.shields.io/badge/DB2%2F400-052FAD?style=for-the-badge&logo=ibm&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10%2B-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 📌 Overview

This project provides a simple and reliable way for payroll teams to **update employee salaries directly in an IBM i (AS/400) system** without needing to know RPG or DB2 syntax.

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
- 🏢 **IBM i (AS/400) OS 6.0+ compatible** – supports both classic and modern IBM i environments.
- 🔒 **Restricted access** – only users with the executable file installed on their PC can run the system.
- 📊 **Excel → CSV → DB2/400 pipeline** – fully automated.

---

## ⚙️ How It Works
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

## 🧰 Tech Stack

| Component | Details |
|-----------|---------|
| Language | Python 3.8 |
| Auxiliary scripting | '.bat' files |
| Database | IBM DB2/400 |
| Connectivity | ODBC, FTP |
| Platform | Windows 10+, IBM i OS 6.0+ |
| File formats | '.xls', '.csv' |
| Security | VPN connection required for IBM i access |

---

## 📁 Project Structure
IBM-System-i_AS400/
├── src/
│ ├── AS400_ODBC_Conection.py # ODBC connection to IBM i
│ ├── Ftp_IBM_System_i.py # FTP transfer to IBM i IFS
│ ├── payroll.py # Main payroll processing script
│ ├── payroll_b.py # Alternative / legacy version
│ ├── Data_EO.csv / .xls # Sample input data
│ ├── ftp_cl_as400.bat # Batch file for FTP operations
│ ├── .env # Environment variables (credentials)
│ └── README.md
├── Java_Scripts/ # Additional Java utilities
├── Python_Scripts/ # Standalone Python scripts
└── README.md

---

## 🛠️ Installation

### Prerequisites

On the user's PC or laptop:

- **Microsoft Windows 10 or later**
- **Python 3.8** (if running from source; not required if using the '.exe')
- **VPN connection enabled** with IBM i Series / AS/400 service availability
- Access to the `Python_Nomina` folder containing all required files:
  - '.xls', '.csv', '.bat', '.dll' files

### Setup Steps

1. Copy the 'Python_Nomina' folder to the user's PC.
2. Ensure the '.xls' and '.csv' templates are in the same folder.
3. Confirm the same files exist in the **IBM i IFS (Integrated File System)**.
4. Enable the VPN connection to the IBM i server.
5. Run 'PAYROLL.exe' (or 'payroll.py' if running from source).

---

## 🚀 Usage

The program is based on the executable **PAYROLL**:

1. Place the '.xls' file containing the list of workers with their **base salary** in the correct folder.
2. Run 'PAYROLL.exe'.
3. The script:
   - Converts the '.xls' file into a '.csv' file.
   - Connects to the IBM i server.
   - Automatically updates the salary records in the DB2/400 database.
4. Verify the update on the IBM i side.

---

## 🔐 Security Notes

- Credentials are managed through a '.env' file (excluded from version control).
- VPN connection is required to reach the IBM i server.
- Only authorized payroll users with the executable installed can run the system.

---

## 📜 License

This project is licensed under the **MIT License**. See the 'LICENSE' file for details.

---

## 📬 Contact

**Clay Lancini**

- 📧 Email: [claylancini@gmail.com](mailto:claylancini@gmail.com)
- 🐙 GitHub: [github.com/ClayLanzino](https://github.com/ClayLanzino)

---

*Built to bridge modern Python automation with classic IBM i (AS/400) systems.*
