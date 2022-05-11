@echo off
py -3.9-64 -m PyInstaller meleequickreplace.spec
del meleequickreplace.exe
copy dist\meleequickreplace0.5.0_64bit.exe meleequickreplace.exe
