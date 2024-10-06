@echo off

:: Create virtual environment named 'env'
python -m venv env

:: Activate the virtual environment
call env\Scripts\activate

:: Install required packages
pip install -r requirements.txt

echo Virtual environment setup complete. To activate it, use: call env\Scripts\activate
pause
