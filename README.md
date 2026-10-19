\# GPS Operations Portfolio Demo



A Django web application demonstrating GPS reset workflows, outlet management, activity logging, and Excel file processing.



\## Overview



This project showcases a web-based workflow for handling GPS reset requests and outlet removal records, with validation, activity tracking, and administrative tools.



\*\*This is a portfolio demonstration only.\*\* All operations use local demo data. No production SAP or company databases are accessed or modified.



\## Features



\- \*\*GPS Reset Workflow\*\* — Simulate single and bulk GPS reset operations.

\- \*\*Outlet Management\*\* — Upload Excel files, validate records, preview results, and simulate outlet removal.

\- \*\*Activity Logging\*\* — Record operation status, timestamps, and user activity.

\- \*\*Excel Processing\*\* — Validate `.xlsx` uploads and export activity logs.

\- \*\*Authentication\*\* — Login and access-controlled activity pages.

\- \*\*Admin Dashboard\*\* — Manage demo records through Django Admin.

\- \*\*Demo Safety\*\* — Uses a local SQLite database instead of production systems.



\## Technology Stack



\- Python

\- Django

\- SQLite

\- HTML and CSS

\- JavaScript

\- openpyxl for Excel processing



\## Local Setup



\### Prerequisites



\- Python compatible with the installed Django version

\- Git



\### Installation



Clone the repository:



```bash

git clone https://github.com/XiaoYanKyit/gps-operations-portfolio-demo.git

cd gps-operations-portfolio-demo

```



Create and activate a virtual environment.



\*\*Windows PowerShell:\*\*



```powershell

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

```



\*\*macOS or Linux:\*\*



```bash

python3 -m venv venv

source venv/bin/activate

```



Install dependencies:



```bash

python -m pip install -r requirements.txt

```



Apply migrations:



```bash

python manage.py migrate

```



Create an administrator account:



```bash

python manage.py createsuperuser

```



Start the development server:



```bash

python manage.py runserver

```



Open http://127.0.0.1:8000/ in your browser.



\## Demo Limitations



\- Operations are simulated and do not modify production records.

\- The database contains local demo data only.

\- Automated tests and production deployment configuration are not yet included.



\## Security



Do not use the development secret key or Django debug mode in production. Configure a secure secret key, allowed hosts, and production settings before deployment.



\## Author



\*\*Khant Nyi Nyi Thit\*\*



\[GitHub Profile](https://github.com/XiaoYanKyit)



\---



\*Built as a software development portfolio project.\*

