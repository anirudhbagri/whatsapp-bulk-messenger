@echo off
REM Windows için otomatik başlatıcı



REM Python yüklü mü kontrol et
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python yüklü değil. Lütfen Python kurun.
    pause
    exit /b 1
)

REM Gerekli paketler yüklü mü kontrol et
set NEEDS_INSTALL=0
python -m pip show requests >nul 2>nul
if %errorlevel% neq 0 set NEEDS_INSTALL=1
python -m pip show PySide6 >nul 2>nul
if %errorlevel% neq 0 set NEEDS_INSTALL=1

if %NEEDS_INSTALL% neq 0 (
    echo Gerekli paketler yükleniyor...
    python -m pip install -r requirements.txt
)

REM Güncellemeleri kontrol et
python update.py

REM Uygulamayı başlat
python main.py
pause
