## About

Melee Quick Mod makes it easy to batch apply mods to a Super Smash Bros. Melee iso. It lets you organize your mods by folders and (semi)intelligently finds the correct files to replace.

### Download

Download the latest version from the [releases page](https://github.com/alex-berliner/MeleeQuickMod/releases/).

### Usage

![MQM preview](assets/preview.png?raw=true "MQM preview")

The easiest way to use Melee Quick Mod is to download some mods, place them in the `mods` folder, then drag your Melee iso onto `drag_iso_here.bat`. A file named `meleeout.iso` will be created that uses all your mods!

MQM will check all folders inside the `mods` folder, so feel free to organize!

### Advanced

Your mod's filename can have extra info in it besides the name of the file that it's meant to replace in the iso, which you may find helpful for tagging, or just not having to mass rename things when downloading mods. The only rule is that the original filename (case sensitive) has to be in there.

Examples of what MQM will and won't replace:

| Mod Name  | Overwrites Game File | Note |
| ------------- | ------------- | ------------- |
| mods\PlFcBu.dat  | files/PlFcBu.dat  |  |
| mods\PlFcBu Blue Falco.dat  | files/PlFcBu.dat  | Filename can have extra contents |
| mods\Blue Falco PlFcBu.dat  | files/PlFcBu.dat  | Original filename can be anywhere |
| mods\falco\PlFcBu.dat  | files/PlFcBu.dat  | Subfolders can be used |
| mods\Blue Falco.dat   | invalid  | Original filename missing |
| mods\plfcbu.dat  | invalid  | Original filename case mismatch |
| mods\PlFcBu  | invalid  | No file extension |
| mods\PlFcOj.dat  | invalid  | Not a valid color |

The command line arguments let you set the input iso (-i), output iso name (-o), and mods path (-m), and passing the -t flag will append the time to the output iso's filename. You can tweak these by editing `drag_iso_here.bat` or by running from command line.

### Linux / Mac

Linux users (and probably Mac but untested) can run the python script directly:

`./meleequickmod.py -i cleanmelee.iso`

### Thanks

Thanks to LagoLunatic for the GCM parser from their wwrando repo and build structure from their GCFT repo.

https://github.com/LagoLunatic/wwrando/

https://github.com/LagoLunatic/GCFT
