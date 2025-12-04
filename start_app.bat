@echo off
echo =======================================
echo   Starting AI Resume Screening System
echo =======================================

REM Python executable
SET PYTHON=C:\Python312\python.exe

REM Streamlit executable (found from your system)
SET STREAMLIT=C:\Users\sxk9280\AppData\Roaming\Python\Python312\Scripts\streamlit.exe

REM Path to Streamlit Home page
SET APP_PATH=C:\Users\sxk9280\Desktop\capstone_project\app\Home.py

echo Using Python: "%PYTHON%"
echo Using Streamlit: "%STREAMLIT%"
echo Starting app...

"%STREAMLIT%" run "%APP_PATH%"

pause