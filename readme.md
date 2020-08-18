File/Folder Linking Utilities (in Python)
===

These python scripts allow for the easy creation of file/folder hard-link/soft-link/junction(s). The main file-linking function can be used from the command line, a bash script, or even from another python script.

Designed for making space on systems with a (smaller) SSD as their main drive i.e. (offload files to another drive/device) but they will work just as well anywhere else. Also useful for syncing various files/folders with online cloud syncing services.

Tested working with Python 2/3 on Linux (WSL) and Python 3 on Windows. Should work also on OSX, but it has not been tested.
On Windows, there are convenience scripts, `symbolic_link.bat` and `admin_link.bat`, included to facilitate running the script as admin with minimal effort.

Created due to personal need and shared with the world... Because doing it with the built-in system tools is too annoying.

Scripts included:
---
<h4>file_link.py:</h4>

Creates a link from one file/folder to another.
Does not require "quotation marks" in the file/folder path.
Supports both hard-linking, and symbolic-linking (requires admin privileges on windows).

<h4>replace_with_link.py</h4>

Moves the files/folders, and replaces the original file/folder with a link to itself.
Does not require "quotation marks" in the file/folder path.
Supports both hard-linking, and symbolic-linking (requires admin priveleges on windows).

<h4>link_many.py</h4>
Creates links from one file/folder to multiple others.
For use when you want to create many copies of a file (without using up a bunch of space).
Does not require "quotation marks" in the file/folder paths.
Supports both hard-linking, and symbolic-linking (requires admin priveleges on windows).

CLI Usage:
---

`python file_link.py [[source] [destination]] [symbolic]`

Specifying the "source" and "destination" arguments ahead of time allows for skipping the file/folder prompts (i.e. for usage with a bash script). These two arguments are optional, but must be used together.

Adding the "symbolic" flag at the end of the command tells the program to use a _symbolic_ link instead of a _hard_ link (or junction).