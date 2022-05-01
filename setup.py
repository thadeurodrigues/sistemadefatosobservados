import sys
from cx_Freeze import setup, Executable
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QToolButton, QApplication, QStyleFactory, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon




# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
icon = "icon.ico"

executables = [
    ('main.py', "base=base" ,"icon.ico")
]
includeFiles = ['virtual env/']
packages = ['PyQt5',"mysql.connector","reportlab.pdfgen"]

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "interface",
        version = "2.0",
        description = "My GUI application!",
        options = {'build_exe': {'include_files':includeFiles}},
        executables = [Executable("controle.py", base=base, icon=icon)])