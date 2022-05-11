#!/usr/bin/env python3
import sys
from gcm import *
import time
from os import walk
import argparse

def splash():
    print("    __  ___   ____     __  ___")
    print("   /  |/  /  / __ \   /  |/  /")
    print("  / /|_/ /  / / / /  / /|_/ / ")
    print(" / /  / /  / /_/ /  / /  / /  ")
    print("/_/  /_/   \___\_\ /_/  /_/   ")
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

def import_mods(disc_handle, mypath):
    fails = []
    for root, dirs, files in os.walk(mypath):
        for f in files:
            applied = False
            mod_name, mod_ext = get_name_and_ext(f)
            for k in disc_handle.files_by_path:
                disc_file_name, disc_file_ext = get_name_and_ext(disc_handle.files_by_path[k].file_path)
                if disc_file_name in mod_name.split(" ") and mod_ext == disc_file_ext:
                    replace_file(disc_handle, disc_handle.files_by_path[k], os.path.join(root, f))
                    print(f"Writing {os.path.join(root, f)} over {disc_handle.files_by_path[k].file_path}")
                    applied = True
                    break
            if not applied:
                fails += [os.path.join(root, f)]
    if len(fails) > 0:
        for e in fails:
            print(f"Could not apply {e}")

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", default="", help="input iso")
    parser.add_argument("-o", "--output", default="moddedmelee.iso", help="output iso name")
    parser.add_argument("-m", "--mods", default="mods", help="mods storage folder, default is \"mods\"")
    parser.add_argument("-t", "--time", default=False, help="append time string to output iso name")
    args = vars(parser.parse_args())
    if args["input"] == "":
        print("You must pass an input iso with -i. Run with -h for help.")
        sys.exit()
    if args["time"]:
        oname, oext = get_name_and_ext(args["output"])
        args["output"] = f"{oname}{int(time.time())}.{oext}"
    return args

def main():
    splash()

    args = parse_args()
    disc_handle = GCM(args["input"])
    disc_handle.read_entire_disc()
    import_mods(disc_handle, args["mods"])
    if len(disc_handle.changed_files) < 1:
        print("No mods were added, aborting.")
        sys.exit()
    g = disc_handle.export_disc_to_iso_with_changed_files(args["output"])
    process_generator(g)

if __name__ == "__main__":
    main()
