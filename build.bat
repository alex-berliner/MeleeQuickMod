@echo off
py -3.9-64 -m PyInstaller meleequickmod.spec
FOR /F "tokens=*" %%g IN ('python3 -c "import version; print(version.VERSION.strip())"') do (SET VAR=%%g)
del meleequickmod.exe
mkdir MeleeQuickMod
mkdir MeleeQuickMod\mods
copy drag_iso_here.bat MeleeQuickMod\drag_iso_here.bat
copy dist\meleequickmod%VAR%_64bit.exe MeleeQuickMod\meleequickmod.exe

@REM echo meleequickmod_windows_%VAR%.zip
rm meleequickmod_windows_%VAR%.zip
copy NUL meleequickmod_windows_%VAR%.zip
