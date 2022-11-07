# Приложение для конвертации маршрутов на Яндекс Картах в gpx файл

## Как пользоваться:
Windows - просто скачать приложение из [релиза](https://github.com/kintolayli/ym_to_gpx_converter_pyside_app/releases), ym_to_gpx.exe

Для Linux и MacOS доступно только в виде консольного приложения, для этого нужно:

0. Проверить, установлен ли python в системе `python3 --version`
1. Клонировать репозиторий из командной строки - `git clone https://github.com/kintolayli/ym_to_gpx_converter_pyside_app.git`
2. В папке с репозиторием создать виртуальное окружение `python3 -m venv venv`. 
3. Активировать виртуальное окружение. Linux - `$ source ym_to_gpx_converter_pyside_app/bin/activate`. MacOS -  `source ym_to_gpx_converter_pyside_app/bin/activate`
4. Установить в него зависимости `pip3 install requirements.txt`
5. запустить из консоли файл `python3 convert_to_gpx.py`
