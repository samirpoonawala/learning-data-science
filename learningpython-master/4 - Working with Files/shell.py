# Example file for working with filesystem shell methods

import os
from os import path
import shutil
from shutil import make_archive
from zipfile import zipfile

def main():
    # make a duplicate in the current directory
    if path.exists("textfile.txt"):

        # get the path to the file in the current directory
        source = path.realpath("textfile.txt")

        # let's make a backup copy by appending "back" to the name
        destination = source + ".bak"
    
        # copy over the permissions, modification times, and other info
        # shutil.copy(source, destination) # only copies over contents of the file
        # shutil.copystat(source, destination) # includes metadata in copy

        # rename the original file
        # os.rename("textfile.txt", "newfile.txt")

        # now put things into a zip archive
        root_dir, tail = path.split(source)
        shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over zip
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("textfile.txt")
            newzip.write("textfile.txt.bak")


if __name__ == "__main__":
  main()