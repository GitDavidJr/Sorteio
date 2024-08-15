# python .\setup.py build
import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os"], "includes": ["flet"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Sorteador de Numeros",
    version="0.2",
    description="Sorteador de numeros aleatorios",
    options={"build_exe": build_exe_options},
    executables=[Executable("Sorteio.py", base=base)]
)