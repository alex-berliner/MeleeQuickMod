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

For MQM to recognize a mod file to replace a game file, the game filename must exist inside mod filename. You may find this helpful for tagging, or just not having to mass rename things when downloading mods.

Examples of what MQM will and won't replace:
| Mod Name  | Overwrites Game File | Note |
| ------------- | ------------- | ------------- |
| mods\PlFcBu.dat  | files/PlFcBu.dat  | Game file and mod file are the same |
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

TL;DR: `PlFcOj.dat` incorrectly replaces `PlFc.dat` instead of not replacing any file. This is intended.

MQM looks to see if the name of any file on the disc exists **inside** of your mod's name. This may lead to incorrect file replacements if, by way of your mod being named incorrectly, it doesn't match to the intended game file, and then does match to a different, unintended game file.

Example: You include a mislabeled mod named `PlFcOj.dat`. Since `Oj` isn't one of Falco's skin colors, MQM performs no file replacement.

Afterwards, MQM looks for a mod file to replace the disc file `PlFc.dat`, Falco's common texture data. Since `PlFc` exists inside `PlFcOj`, MQM incorrectly replaces `PlFcOj.dat` with `PlFc.dat`. Falco's common textures file has been incorrectly been replaced with a skin file and so the game will crash when loading him.

The way to avoid this is to ensure that the **entire text** of the file you wish to replace exists inside the mod filename.

### Structured Disc Replacement

A caveat throwing all your mods in a single folder is that if two files with the same name exist on the disc in different folders MQM won't know which file to replace.

If this happens and you need to target a particular file on the disc, get the exact location of the file on the disc with `.\meleequickmod.exe -i cleanmelee.iso -c`. Then place your file in `mods\disc\my\exact\location\file.dat`. Everything goes in the subfolder `disc\`.

Example: Melee has both `files/audio/1padv.ssm` and `files/audio/us/1padv.ssm`.

Replace `files/audio/us/1padv.ssm` by placing a new `1padv.ssm` at

`mods\disc\files\audio\us\1padv.ssm`

Inexact replacement also works:

`mods\disc\files\audio\us\my_modded_1padv.ssm`

### Thanks

Thanks to LagoLunatic for the GCM parser from their wwrando repo and build structure from their GCFT repo.

https://github.com/LagoLunatic/wwrando/

https://github.com/LagoLunatic/GCFT
