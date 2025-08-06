@echo off
echo Starting Sleep Health & Lifestyle Analysis Dashboard...
echo.
echo Using virtual environment Python...
echo.
echo Dashboard will open in your default web browser at: http://localhost:8501
echo.
echo To stop the dashboard, press Ctrl+C in this window
echo.
.\.venv\Scripts\python.exe -m streamlit run streamlit_dashboard.py
