@echo off
py -3.9-64 -m PyInstaller meleequickmod.spec
del meleequickmod.exe
copy dist\meleequickmod0.5.0_64bit.exe meleequickmod.exe
