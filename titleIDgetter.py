import os
import binascii

folder_name = "INSERT_YOUR_FOLDER_NAME_HERE"

for subdir, dirs, files in os.walk(folder_name):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".tmd"):
            print (subdir)
            with open(filepath, "rb+") as f:
                f.seek(0x18C)
                titleID = bytes.hex(f.read(8))
                print((titleID).upper())
                """if (titleID).upper() not in subdir:
                    td = (titleID).upper()
                    f.close()
                    os.rename(subdir, subdir+" ["+td+"]")
                    print("Error fixed!")"""