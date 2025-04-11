@echo off

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Install Playwright browsers
playwright install chromium

REM Create reports directory if it doesn't exist
if not exist reports mkdir reports

echo Setup complete! To activate the environment, run: venv\Scripts\activate.bat