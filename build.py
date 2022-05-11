
from zipfile import ZipFile
import os

from version import VERSION

base_name = "meleequickmod"
base_name_with_version = base_name + "_" + VERSION

import struct
if (struct.calcsize("P") * 8) == 64:
  base_name_with_version += "_64"
  base_zip_name = base_name_with_version
else:
  base_name_with_version += "_32"
  base_zip_name = base_name_with_version

zip_name = base_zip_name.replace(" ", "_") + ".zip"

exe_path = "./dist/%s.exe" % base_name_with_version
if not os.path.isfile(exe_path):
  raise Exception("Executable not found: %s" % exe_path)

with ZipFile("./dist/" + zip_name, "w") as zip:
  zip.write(exe_path, arcname="%s.exe" % base_name)
  zip.write("README.md", arcname="README.txt")
