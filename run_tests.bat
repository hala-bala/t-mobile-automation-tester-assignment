@echo off

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run tests
pytest tests/ %*
