@echo off
echo ============================================
echo   Netflix DataViz - Environment Setup
echo ============================================
echo.

echo [1/3] Creating virtual environment...
python -m venv venv
echo       Done!
echo.

echo [2/3] Activating virtual environment...
call venv\Scripts\activate.bat
echo       Done!
echo.

echo [3/3] Installing dependencies...
pip install -r requirements.txt
echo       Done!
echo.

echo ============================================
echo   Setup Complete! 
echo   Run: venv\Scripts\activate
echo   Then: jupyter notebook netflix_analysis.ipynb
echo ============================================
pause
