# LAB 01

## How to set up the environment and install dependencies

1. Create and activate a virtual environment (Windows PowerShell):

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install required packages:

   ```powershell
   pip install -r requirements.txt
   ```

## How to run tests and generate HTML report

To run all unit tests:

```powershell
pytest
```

To generate an HTML report (saved in the reports directory):

```powershell
pytest --html=reports/report.html
```

You can open the generated `reports/report.html` file in your browser to view a detailed test report.

If you don't have Python installed, download it from https://www.python.org/
