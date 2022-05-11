from gcm import *

MELEEPATH = r"C:\Users\alexb\Desktop\New folder\newmelee.iso"
NEWMELEEPATH = r"C:\Users\alexb\Desktop\New folder\modifiedmelee.iso"

disc_handle = GCM(MELEEPATH)
disc_handle.read_entire_disc()
disc_handle.export_disc_to_iso_with_changed_files
