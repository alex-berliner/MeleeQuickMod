## About

Melee Quick Mod makes it easy to batch apply mods to a Super Smash Bros. Melee iso. It intelligently replaces game files with mod files and lets you organize your mods by folder.

### Download

Download the latest version from the [releases page](https://github.com/alex-berliner/MeleeQuickMod/releases/).

### Usage

![MQM preview](assets/preview.gif?raw=true "MQM preview")

The easiest way to use Melee Quick Mod is to download some mods, place them in the `mods` folder, then drag your Melee iso onto `drag_iso_here.bat`. A file named `meleeout.iso` will be created that uses all your mods!

MQM checks all folders inside the `mods` folder, so feel free to organize!

### Linux / Mac

Linux users (and probably Mac) can run the python script directly:

`./meleequickmod.py -i cleanmelee.iso`

### Mod Naming Rules

Mod files must contain the entire text of the game file they are meant to replace, and have the same extension. Aside from that, the mod can be named whatever you wish and MQM will find it. You may find this helpful for tagging, or just not having to mass rename things when downloading mods.

Examples of what MQM will and won't replace:
| Mod Name  | Overwrites Game File | Note |
| ------------- | ------------- | ------------- |
| mods\PlFcBu.dat  | files/PlFcBu.dat  |  |
| mods\PlFcBu Blue Falco.dat  | files/PlFcBu.dat  | Filename can have extra contents |
| mods\BluePlFcBuFalco.dat  | files/PlFcBu.dat  | Game filename can be anywhere without delimiter|
| mods\falco\PlFcBu.dat  | files/PlFcBu.dat  | Subfolders can be used |
| mods\disc\files\audio\us\1padv.ssm  | files/audio/us/1padv.ssm  | [Target specific files](#avoiding-incorrect-file-replacement) |
| mods\Blue Falco.dat   | invalid  | Original filename missing |
| mods\plfcbu.dat  | invalid  | Original filename case mismatch |
| mods\PlFcBu  | invalid  | No file extension |
| mods\PlFcOj.dat  | invalid  | Not a valid color (See [Avoiding File Misplacement](#avoiding-incorrect-file-replacement)) |

### Command Line Arguments

| Argument | Description |
| ------------- | ------------- |
| -h | get help |
| -i | set input iso |
| -o | set output iso name |
| -m | set mods folder |
| -t | append the time to the output iso's filename |
| -c | print a list of files on the disc |

You can use these by editing `drag_iso_here.bat` or by running from command line.

### Avoiding Incorrect File Replacement

TL;DR: `PlFcOj.dat` incorrectly replaces `PlFc.dat` instead of not replacing any file. This is intended behavior, so make sure your mod filenames contain the full name of the file it should replace.

MQM finds files to replace by looking for the full disc filename **inside** the mod filename. If your mod files don't contain the full disc filename, MQM may erroneously target similar looking files to replace on the disc instead, resulting in a broken iso.

Example:

You include a mod named `PlFcOj.dat`, expecting it to add an orange skin for Falco. However the stock Melee iso contains no such file since Falco has no orange skin by default so MQM does not perform the intended file replacement.

Afterwards, MQM looks for a mod file to replace the disc file `PlFc.dat`, Falco's common texture data. Since the text `PlFc` appears inside `PlFcOj`, MQM incorrectly targets `PlFcOj.dat` to replace `PlFc.dat`. Now Falco's common textures file has been incorrectly been replaced with a skin file and so the game will crash when loading him.

The way to avoid this is to ensure that the **entire text** of the file you wish to replace exists inside the mod filename.

### Structured Disc Replacement

A caveat surrounding throwing all your mods in a single folder is that if two files with the same name exist on the disc in different folders MQM won't know which file to replace.

If this happens you can target the file you wish to replace directly by storing it using the disc file's entire folder structure.

Get the exact location of the file on the disc with `.\meleequickmod.exe -i cleanmelee.iso -c`. Then place your file in `mods\disc\my\exact\location\file.dat`. Note that everything goes in the subfolder `disc\` in the `mods` folder.

Example: Melee has both `files/audio/1padv.ssm` and `files/audio/us/1padv.ssm`.

Replace `files/audio/us/1padv.ssm` by placing a new `1padv.ssm` at

`mods\disc\files\audio\us\1padv.ssm`

Inexact replacement also works:

`mods\disc\files\audio\us\my_modded_1padv.ssm`

### Contact

Comments, questions, issues, found a dead bug in a box?

Twitter https://twitter.com/allocsb

Reddit https://reddit.com/u/LavaSalesman

### Thanks

Thanks to LagoLunatic for the GCM parser from their wwrando repo and build structure from their GCFT repo.

https://github.com/LagoLunatic/wwrando/

https://github.com/LagoLunatic/GCFT
