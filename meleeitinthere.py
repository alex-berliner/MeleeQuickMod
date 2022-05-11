#!/usr/bin/env python3

from gcm import *
import time
from os import walk

GAMEPATH = r"C:\Users\alexb\Desktop\New folder\meleeitinthere\newmelee.iso"
NEWGAMEPATH = r"C:\Users\alexb\Desktop\New folder\meleeitinthere\modifiedmelee.iso"

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
            # print(next_progress_text, progress_value)
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

def make_modified_disc(disc_handle):
    mypath = "replace"
    for root, dirs, files in os.walk(mypath):
        for f in files:
            mod_name, mod_ext = get_name_and_ext(f)
            for k in disc_handle.files_by_path:
                disc_file_name, disc_file_ext = get_name_and_ext(disc_handle.files_by_path[k].file_path)
                if disc_file_name == mod_name.split(" ")[0] and mod_ext == disc_file_ext:
                    replace_file(disc_handle, disc_handle.files_by_path[k], os.path.join(root, f))
                    print(f"Adding {os.path.join(root, f)}")
                    break
    g = disc_handle.export_disc_to_iso_with_changed_files(NEWGAMEPATH)
    process_generator(g)

def main():
    disc_handle = GCM(GAMEPATH)
    disc_handle.read_entire_disc()
    make_modified_disc(disc_handle)

if __name__ == "__main__":
    main()
