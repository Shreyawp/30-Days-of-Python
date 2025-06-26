# OS module
import os

# View attributes and method
print(dir(os))

# git current working directory
cwd = os.getcwd()
print("Current wokring directory: ", cwd)
 
####################### OUTPUT ##########################
# Current wokring directory:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode
##########################################################
 
# navigate to another directory
os.chdir('12_modules')                           #Change directory
print("Current wokring directory: ", os.getcwd()) 
####################### OUTPUT ##########################
# >> Current wokring directory:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\12_modules
##########################################################

# list of directories and files in cwd
print("list of directories and files in cwd: \n", os.listdir())
# >> list of directories and files in cwd:
# ['abc.txt', 'dummy_file.txt', 'main.py', 'mymodule.py', 'os_module.py', 'random_module.py', 'tempCodeRunnerFile.py', 'tmp', '__pycache__']

dir_list = os.listdir("/")
print("File and Directories in '/':\n", dir_list) 
####################### OUTPUT ##########################
# File and Directories in '/':
# ['$1Recycle.Bin', '$GetCurrent', '$Recycle.Bin', '$Windows.~WS', '$WinREAgent', 
# 'Config.Msi', 'Documents and Settings', 'DumpStack.log', 'DumpStack.log.tmp', 'edb',
# 'ESD', 'hiberfil.sys', 'inetpub', 'Intel', 'KMSpico Install', 'KMSpico Install.rar', 
# 'LastBak.ini', 'MSOCache', 'NPAVSCN.DAT', 'NPKey.txt', 'OneDriveTemp', 'OSGeo4W', 
# 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 
# 'Recovery', 'swapfile.sys', 'System Volume Information', 'Users', 'Windows', 'zv']
##########################################################

# create new directory with mode=rwxrwxrwx
os.mkdir('dummy_dir', mode=0o777)
print("Make new directory(dummy_dir): \n",os.listdir())
####################### OUTPUT ##########################
# >> Make new directory(dummy_dir):
# ['abc.txt', 'dummy_dir', 'dummy_file.txt', 'main.py', 'mymodule.py', 'os_module.py', 'random_module.py', 'tempCodeRunnerFile.py', 'tmp', '__pycache__']
##########################################################

# create sub directories with mode=rwxrwxrwx
os.makedirs('dummy_dir1/sub_dir_1', mode=0o777) 
print("Make new directories(dummy_dir1/sub_dir_1): \n", os.listdir())
####################### OUTPUT ##########################
# >> Make new directories(dummy_dir1/sub_dir_1):
# ['abc.txt', 'dummy_dir', 'dummy_dir1', 'dummy_file.txt', 'main.py', 'mymodule.py', 'os_module.py', 'random_module.py', 'tempCodeRunnerFile.py', 'tmp', '__pycache__']
##########################################################

# deleting folders
os.rmdir('dummy_dir')
print("Delete directory(dummy_dir): \n",os.listdir())
####################### OUTPUT ##########################
# >> Delete directory(dummy_dir):
# ['abc.txt', 'dummy_dir1', 'dummy_file.txt', 'main.py', 'mymodule.py', 'os_module.py', 'random_module.py', 'tempCodeRunnerFile.py', 'tmp', '__pycache__']
##########################################################

# deleting recursive/sub-directories
os.removedirs('dummy_dir1/sub_dir_1')
print("Delete directory(dummy_dir1/sub_dir_1): \n",os.listdir())
####################### OUTPUT ##########################
# >> Delete directory(dummy_dir1/sub_dir_1): 
# ['abc.txt', 'dummy_file.txt', 'main.py', 'mymodule.py', 'os_module.py', 'random_module.py', 'tempCodeRunnerFile.py', 'tmp', '__pycache__']
##########################################################

# Rename file 
os.rename('dummy_file.txt', 'demo_file.txt')
print("File renamed(dummy_file.txt to demo_file.txt): \n", os.listdir())
####################### OUTPUT ##########################
# >> File renamed(dummy_file.txt to demo_file.txt):
# ['abc.txt', 'demo_file.txt', 'main.py', 'mymodule.py', 'os_module.py', 'random_module.py', 'tempCodeRunnerFile.py', 'tmp', '__pycache__']
##########################################################

# decribe/information of file
print(os.stat('demo_file.txt'))
####################### OUTPUT ##########################
# >> os.stat_result(st_mode=33206, st_ino=25895697857387914, st_dev=3896922441, st_nlink=1, st_uid=0, st_gid=0, st_size=15, st_atime=1750917781, st_mtime=1749822036, st_ctime=1749822022)  
##########################################################

# checking each attribute of file
print("size of file: ", os.stat('demo_file.txt').st_size)     
print("last modification of file: ", os.stat('demo_file.txt').st_mtime)
####################### OUTPUT ##########################
# >> size of file:  15
# last modification of file:  1749822036.3383386
##########################################################

# use datetime
from datetime import datetime
mod_time = os.stat('demo_file.txt').st_mtime
print("last modification of file: ", datetime.fromtimestamp(mod_time))
####################### OUTPUT ##########################
# >> last modification of file:  2025-06-13 19:10:36.338339
##########################################################

# view directory tree as tuple
print(os.walk(cwd))  
#>> <generator object _walk at 0x000002B4C0649D20>

for dirpth,dirname,filenames in os.walk(cwd):
    print("Current path: ", dirpth)
    print("Directories: ", dirname)
    print("Files: ",filenames)
    print()
####################### OUTPUT ##########################
# >> Current path:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode
# Directories:  ['.git', '12_modules', '__pycache__']
# Files:  ['01_helloworld.py', '02_variables.py', '03_operators.py', '04_strings.py', '05_list.py', '06_tuple.py', '07_set.py', '08_dictionary.py', '09_conditionals.py', '10_loops.py', '11_functions.py', '12_modules.py', 'countries.py', 'countries_data.py', 'README.md', 'tempCodeRunnerFile.py']
#
# Current path:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\.git
# Directories:  ['hooks', 'info', 'logs', 'objects', 'refs']
# Files:  ['COMMIT_EDITMSG', 'config', 'description', 'FETCH_HEAD', 'HEAD', 'index', 'ORIG_HEAD']
#
# Current path:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\.git\hooks        
# Directories:  []
# Files:  ['applypatch-msg.sample', 'commit-msg.sample', 'fsmonitor-watchman.sample', 'post-update.sample', 'pre-applypatch.sample', 'pre-commit.sample', 'pre-merge-commit.sample', 'pre-push.sample', 'pre-rebase.sample', 'pre-receive.sample', 'prepare-commit-msg.sample', 'push-to-checkout.sample', 'sendemail-validate.sample', 'update.sample']
#
# Current path:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\.git\info
# Directories:  []
# Files:  ['exclude']
#
##########################################################

# get environment variables
print(os.environ.get('HOMEPATH'))
# >> \Users\Admin

# creating file_path with name which can be use to create new file
file_path = os.environ.get('HOMEPATH') + 'test.txt'
print(file_path)
# >> \Users\Admintest.txt

# above method is missing '\', hence using os.path module
file_path = os.path.join(os.environ.get('HOMEPATH') , 'test.txt')
print(file_path)
# >> \Users\Admin\test.txt

# check all methods and attributes in os.path
print(dir(os.path))
####################### OUTPUT ##########################
# >> ['_LCMAP_LOWERCASE', '_LCMapStringEx', '_LOCALE_NAME_INVARIANT', '__all__', '__builtins__', 
# '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_abspath_fallback', '_get_bothseps', '_getfinalpathname', '_getfinalpathname_nonstrict', '_getfullpathname', '_getvolumepathname', '_nt_readlink', '_readlink_deep', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 
# 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
##########################################################

# to get base of given path, here test.txt file
print(os.path.basename('/tmp/test.txt'))
# >> test.txt

# to get directory of path
print(os.path.dirname('/tmp/test.txt'))
# >> /tmp

# to get both separately as tuple
print(os.path.split('/tmp/test.txt'))
# >> ('/tmp', 'test.txt')

# to check if path exists
print(os.path.exists('/tmp/test.txt'))
# >> False

# check if given is directory of file
print(os.path.isdir(cwd))
print(os.path.isfile(cwd))
# >> True
# >> False

# split root path and extension
print(os.path.splitext('/tmp/test.txt'))
# >> ('/tmp/test', '.txt')


