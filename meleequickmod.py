#!/usr/bin/env python3
from collections import OrderedDict
from gcm import *
from os import walk
import argparse
import time
import version

def splash():
    print("    __  ___   ____     __  ___")
    print("   /  |/  /  / __ \   /  |/  /")
    print("  / /|_/ /  / / / /  / /|_/ / ")
    print(" / /  / /  / /_/ /  / /  / /  ")
    print("/_/  /_/   \___\_\ /_/  /_/   ")
    print(f"Version {version.VERSION}")
    print("https://github.com/alex-berliner/MeleeQuickMod")

def process_generator(g):
    # ripped from GCFT\gcft_ui\gcft_common.py GCFTThread.run
    try:
        last_update_time = time.time()
        while True:
            # Need to use a while loop to go through the generator
            # instead of a for loop, as a for loop would silently exit if a
            # StopIteration error ever happened for any reason.
            next_progress_text, progress_value = next(g)
            if progress_value == -1:
                break
            if time.time()-last_update_time < 0.1:
                # Limit how frequently the signal is emitted to 10 times per second.
                # Extremely frequent updates (e.g. 1000 times per second) can cause
                # the program to crash with no error message.
                continue
            last_update_time = time.time()
    except Exception as e:
        print(e)

def replace_file(disc_handle, iso_file, replace_filepath):
    with open(replace_filepath, "rb") as f:
      data = BytesIO(f.read())
      disc_handle.changed_files[iso_file.file_path] = data

def get_name_and_ext(path):
    name = path.split("/")[-1]
    return name.split(".")[0], name.split(".")[-1]

class ReplaceHandle():
    def __init__(self, full_path):
        self.full_path = full_path
        nandx = get_name_and_ext(full_path)
        self.dir = get_dir_only(full_path)
        self.name = nandx[0]
        self.ext = nandx[1]
        self.replaced = False
        self.replaced_with = None

    def __lt__(self, other):
         return len(self.name) < len(other.name)

    def __str__(self):
        return f"{self.full_path} {self.name} {self.ext}"

def remove_first_slash(path):
    return "/".join(path.split("/")[1:])

def get_dir_only(path):
    if "." not in path:
        return path

    return "/".join(path.split("/")[:-1])

def replace_disc_conts(disc_handle, mypath, game_files_od, strict_name, disc_replace):
    mods_applied = set()
    for root, dirs, files in os.walk(mypath):
        for f in files:
            raw_mod_path = root + "/" + f
            mod_path = remove_first_slash(raw_mod_path)
            if not disc_replace and mod_path.startswith("disc/"):
                continue
            dict_addr = remove_first_slash(mod_path)
            mod_dir = get_dir_only(mod_path)
            mod_name, mod_ext = get_name_and_ext(mod_path)
            gf = None
            if dict_addr in game_files_od:
                gf = game_files_od[dict_addr]
            else:
                for k in game_files_od:
                    gf_name, gf_ext = get_name_and_ext(k)
                    if gf_name in mod_name and gf_ext == mod_ext:
                        gf = game_files_od[k]
                        break
            if not gf:
                continue
            dir_cond = (mod_dir == ("disc/" + gf.dir)) if disc_replace else True
            name_cond = (gf.name == mod_name) if strict_name else (gf.name in mod_name)
            if dir_cond and name_cond and gf.ext == mod_ext and not gf.replaced:
                gf.replaced = True
                print(f"Writing {mod_path} over {gf.full_path}")
                replace_file(disc_handle, disc_handle.files_by_path[gf.full_path], raw_mod_path)
                mods_applied.add(mod_path)
    return mods_applied

def import_mods(disc_handle, mypath):
    game_files = [ReplaceHandle(x) for x in disc_handle.files_by_path]
    game_files.sort(reverse=True)

    game_files_od = OrderedDict((obj.full_path, obj) for obj in game_files)
    mods_applied = set()
    mods_applied |= replace_disc_conts(disc_handle, mypath + "/disc", game_files_od, strict_name=True,  disc_replace=True)
    mods_applied |= replace_disc_conts(disc_handle, mypath + "/disc", game_files_od, strict_name=False, disc_replace=True)
    mods_applied |= replace_disc_conts(disc_handle, mypath, game_files_od, strict_name=True,  disc_replace=False)
    mods_applied |= replace_disc_conts(disc_handle, mypath, game_files_od, strict_name=False, disc_replace=False)
    for root, dirs, files in os.walk(mypath):
        for f in files:
            raw_mod_path = root + "/" + f
            mod_path = remove_first_slash(raw_mod_path)
            if mod_path not in mods_applied:
                print(f"Could not apply {raw_mod_path}")

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", default="", help="input iso")
    parser.add_argument("-o", "--output", default="moddedmelee.iso", help="output iso name")
    parser.add_argument("-m", "--mods", default="mods", help="mods storage folder, default is \"mods\"")
    parser.add_argument("-t", "--time", action='store_true', default=False, help="append time string to output iso name")
    parser.add_argument("-c", "--contents", action='store_true', default=False, help="list the contents of the disc")
    args = vars(parser.parse_args())
    if args["input"] == "":
        print("You must pass an input iso with -i. Run with -h for help.")
        exit()
    if args["time"]:
        oname, oext = get_name_and_ext(args["output"])
        args["output"] = f"{oname}{int(time.time())}.{oext}"
    if args["contents"]:
        print_disc(disc_handle)
        exit()
    return args

def print_disc(disc_handle):
    for f in disc_handle.files_by_path:
        print(f)

def main():
    splash()
    args = parse_args()
    disc_handle = GCM(args["input"])
    disc_handle.read_entire_disc()
    import_mods(disc_handle, args["mods"])
    if len(disc_handle.changed_files) < 1:
        print("No mods were added, aborting.")
        exit()
    g = disc_handle.export_disc_to_iso_with_changed_files(args["output"])
    process_generator(g)
    print(f'Wrote output to {args["output"]}')


if __name__ == "__main__":
    main()
