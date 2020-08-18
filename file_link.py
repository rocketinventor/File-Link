import os
# windows only
if os.name == 'nt':
    from _winapi import CreateJunction as create_junction
from sys import argv
# handling for python2
from sys import version as _version
p_v2 = (_version[0] == '2')
if p_v2:
    PermissionError = 'PermissionError'
    FileExistsError = 'FileExistsError'
    FileNotFoundError = 'FileNotFoundError'
else:
    IOError = TypeError
from shutil import move

src = dst = args = ''
use_sym_link = False

# read in args
args = argv[1:]
# set src and dst if they exists (first 2 params)
# The word "symbolic" is a valid filename choice.
if len(args) >= 2:
    [src, dst] = args[:2]
# check if we should be "symbolic" (unless there are only two arguments)
if (len(args) >= 1) and (len(args) != 2):
    if (args[-1] == 'symbolic'):
        use_sym_link = True
    else:
        print('Did not understand argument:', args[-1])
        print('Both paths must be specified when used as arguments.\n')

def clean_exit():
    print('Exiting.\n')
    exit()

def _input(msg=''):
    # input prompt inside of a try/except loop
    # (for more graceful exiting behaviour)
    try:
        # support for python 2 "raw_input"
        if p_v2:
            input_text = raw_input(msg)
        else:
            input_text = input(msg)
    except KeyboardInterrupt:
        clean_exit()
    input_text = input_text.replace('"', '')
    input_text = input_text.strip()
    return input_text

def delete_dir_if_empty(dir='.'):
    """

    Attempts to delete the directory if it is empty.

    Accepts a directory path as a string "dir".

    Returns 'True' if deleted, and False if not
    (i.e. system error or directory that has files in it)

    """

    # check if the directory is empty (python3 only)
    if os.path.isdir(dst) and not os.listdir(dst):
        print('Empty directory already exists. Deleting it.')
        try:
            if os.path.islink(dir):
                os.remove(dir)
            else:
                os.removedirs(dir)
            return True
        except OSError as err:
            # prompt for a different path:
            print('Error with delete:', err)
    return False
def input_src(input_text='Source location: '):
    while True:
        src = _input(input_text)

        if not (os.path.exists(src) or os.path.isfile(src)):
            # prompt for a different path:
            print('Not a valid file. Please check the file path:', os.path.abspath(src))
            continue
        else:
            # file is valid, continue on
            break
    return src

def input_dst(input_text='Destination location: ', src=''):
    while True:
        dst = _input(input_text)

        if dst == 'skip':
            clean_exit()
        if dst == src:
            # prompt for a different path:
            print('Source and destination paths are the same. Please retry.')
            continue
        if (os.path.exists(dst) or os.path.isfile(dst)):
            dir_deleted = delete_dir_if_empty(dst)
            if dir_deleted:
                # use this path
                break
            else:
                # prompt for a different path:
                print('File/path already exists. Please try a different path, or type "skip" to skip it.')
                continue
        elif os.access(os.path.dirname(dst), os.W_OK):
            # file is valid, continue on
            break
        elif os.access(os.path.dirname(os.path.join('.', dst)), os.W_OK):
            # file is valid, continue on
            break
        else:
            # prompt for a different path:
            print('Cannot write to that directory. Please specify a different filepath, or try again later.')
            continue
    return dst

def link_paths(src, dst, link_symbolic=False):
    # print('\n')
    if os.path.exists(dst):
        dir_deleted = delete_dir_if_empty(dst)
        if not dir_deleted:
            print('Destination file/folder already exists.')
            return False
    try:
        # Windows uses 'NTFS junction point(s)' (instead of hardlinks)
        if link_symbolic:
            # create a symbolic link
            os.symlink(src, dst)
        else:
            # create a hard-link/junction
            if os.path.isdir(src) and os.name == 'nt':
                create_junction(src, dst)
            else:
                os.link(src, dst)
        print('Succes!\n\nLinked from "{}" to "{}"'.format(src, dst))
        return True
    # python 2
    except IOError as err_io:
        print('File system error:', err_io)
    except OSError as err_os:
        print(err_os)
        print('Skipped.')
    except PermissionError:
        print('File link failed. Try again with symbolic linking (python "{}" symbolic), or as root/administrator.'.format('" "'.join(argv)))
    except FileExistsError:
        print('File already exists. Skipped.')
    except FileNotFoundError:
        print('Destination filepath invalid')
    return False

def blank_ln():
    # so that we don't get lines that look like: "()"
    if p_v2:
        print
    else:
        print()

if __name__ == '__main__':
    # Print intro msg (if not using args)
    if not (src and dst):
        print("""
Creates a link from one file/folder to another.
Does not require "quotation marks" in the file/folder path.""")
        # print a message if we are using symbolic linking
        if use_sym_link:
            print('\nSymbolic Linking activated.')
    blank_ln()

    src = src or input_src()
    dst = dst or input_dst(src=src)

    link_paths(src, dst, use_sym_link)
    
    blank_ln()