#!/bin/bash
# macOS/Linux için otomatik başlatıcı



# Python yüklü mü kontrol et
if ! command -v python3 &> /dev/null; then
    echo "Python3 yüklü değil. Lütfen Python3 kurun."
    exit 1
fi

# Gerekli paketler yüklü mü kontrol et
needs_install=0
python3 -m pip show requests > /dev/null 2>&1 || needs_install=1
python3 -m pip show PySide6 > /dev/null 2>&1 || needs_install=1

if [ "$needs_install" -ne 0 ]; then
    echo "Gerekli paketler yükleniyor..."
    python3 -m pip install -r requirements.txt
fi

# Güncellemeleri kontrol et
python3 update.py

# Uygulamayı başlat
python3 main.py
