chcp 65001
@echo off
REM Определяем папку батника
set script_dir=%~dp0

REM Создаем виртуальное окружение, если нет
if not exist "%script_dir%venv" (
    echo Создаю виртуальное окружение...
    python -m venv "%script_dir%venv"
    call "%script_dir%venv\Scripts\activate.bat"
    echo Устанавливаю библиотеки...
    pip install -r "%script_dir%requirements.txt"
) else (
    call "%script_dir%venv\Scripts\activate.bat"
)

echo Запускаю скрипт...
python "%script_dir%autoaccept.py"

pause
