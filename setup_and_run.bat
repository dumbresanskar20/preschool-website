@echo off
python manage.py makemigrations enquiry reviews contact gallery accounts core > migrations_log.txt 2>&1
python manage.py migrate >> migrations_log.txt 2>&1
echo Done >> migrations_log.txt
