from file_link import *

# TODO: make this function useable from a script

# Print intro msg (if not using args)
if not (src and dst):
    print("""
Moves the files/folders, and replaces the original file/folder with a link to itself.
Does not require "quotation marks" in the file/folder path.""")
    # print a message if we are using symbolic linking
    if use_sym_link:
        print('\nSymbolic Linking activated.')
blank_ln()

if src:
    print("Source:", src)

# make sure that we have permission to move the file/directory.
while not os.access(src, os.W_OK | os.X_OK):
    if src != '':
        # we can't write to the path
        print("We don't have write permission. Maybe try again as admin.")
    src = input_src()

dst = dst or input_dst(src=src)

# swap the src and dst
try:
    print('Moving files. Please wait...')
    move(src, dst)
    print('Moved', src, 'to', dst)
except PermissionError:
    print('File move failed. Check permissions.')
    clean_exit()

(src, dst) = (dst, src)

link_paths(src, dst, use_sym_link)

blank_ln()