@echo off
title Coin Toss Game - CLI or Web
color 0A
echo.
echo Choose mode:
echo 1. CLI (python coin_toss.py)
echo 2. Web App (streamlit run streamlit_coin_toss.py)
echo 3. Install deps (python -m pip install -r requirements.txt)
set /p choice=Enter choice (1/2/3): 

if "%choice%"=="1" (
    python coin_toss.py
) else if "%choice%"=="2" (
    streamlit run streamlit_coin_toss.py
) else if "%choice%"=="3" (
    python -m pip install -r requirements.txt
) else (
    echo Invalid choice. Try again.
    pause
)
pause
