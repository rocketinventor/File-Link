from file_link import *

# Print intro msg (if not using args)

if not (src and dst):
    print("""
Creates links from one file/folder to multiple others.
For use when you want to create many copies of a file (without using up a bunch of space).
Does not require "quotation marks" in the file/folder paths.""")
    # print a message if we are using symbolic linking
    if use_sym_link:
        print('\nSymbolic Linking activated.')
blank_ln()

# ingnores arguments
src = input_src()

while True:
    print('\nEnter another directory to link to... (Type "enter" to quit.)')
    dst = input_dst(src=src)
    if dst == 'exit':
        break
    else:
        link_paths(src, dst, use_sym_link)
        continue

blank_ln()