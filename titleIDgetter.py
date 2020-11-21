import os
import binascii

for subdir, dirs, files in os.walk(r'G:\Games\Wii U\DATA\USA\GAMES'):
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