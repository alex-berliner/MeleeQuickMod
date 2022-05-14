## About

Melee Quick Mod makes it easy to batch apply mods to a Super Smash Bros. Melee iso. It lets you organize your mods by folders and (semi)intelligently finds the correct files to replace.

### Usage

![MQM preview](assets/preview.png?raw=true "MQM preview")

The easiest way to use Melee Quick Mod is to download some mods, place them in the `mods` folder, then drag your Melee iso onto `drag_iso_here.bat`. A file named `meleeout.iso` will be created that uses all your mods!

MQM uses the game's filename as the keyword (ie `PlFcBu`) to look for in the mod's filename. The keyword doesn't have to be the only word in the mod's filename but it has to be spaced apart from any other words, and is case-sensitive.

Mods can be organized in folders.

Examples:

| Mod Name  | Overwrites Game File | Note |
| ------------- | ------------- | ------------- |
| mods\PlFcBu.dat  | files/PlFcBu.dat  |  |
| mods\PlFcBu Blue Falco.dat  | files/PlFcBu.dat  | Filename doesn't need to be exact match |
| mods\Blue Falco PlFcBu.dat  | files/PlFcBu.dat  | Keyword can be anywhere |
| mods\falco\PlFcBu.dat  | files/PlFcBu.dat  | Subfolders can be used |
| mods\falco\PlFcBuCoolFalco.dat  | invalid  | Keyword must be spaced apart from other words |
| mods\Blue Falco.dat   | invalid  | No game file keyword |
| mods\plfcbu.dat  | invalid  | Keyword casing mismatch |
| mods\PlFcBu  | invalid  | No file extension |
| mods\PlFcOj.dat  | invalid  | Not a valid color |

The command line arguments let you set the input (-i), output (-o), and mods path (-m), and passing the -t flag will append the time to the output iso's filename.

### Thanks

Thanks to LagoLunatic for the GCM parser from their wwrando repo and build structure from their GCFT repo.

https://github.com/LagoLunatic/wwrando/
https://github.com/LagoLunatic/GCFT
