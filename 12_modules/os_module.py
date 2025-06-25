# OS module
import os
cwd = os.getcwd()
print("Current wokring directory: ", cwd)
 
####################### OUTPUT ##########################
# Current wokring directory:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode
##########################################################

os.chdir('12_modules')                           #Change directory
print("Current wokring directory: ", os.getcwd()) 
####################### OUTPUT ##########################
# >> Current wokring directory:  C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\12_modules
##########################################################

path = os.path.join(cwd, "dummy_dir")  
#os.mkdir(path)         #Create new directory
print("Created new directory")
####################### OUTPUT ##########################
#>> Created new directory
##########################################################

# Create multiple directories
#parent_dir = "C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\12_modules\dir1"
#path1 = os.path.join(parent_dir, "child_dir")
#os.mkdirs(path1, 0o666)

dir_list = os.listdir("/")
print("FIle and Directories in '/':\n", dir_list) 
####################### OUTPUT ##########################
# FIle and Directories in '/':
# ['$1Recycle.Bin', '$GetCurrent', '$Recycle.Bin', '$Windows.~WS', '$WinREAgent', 
# 'Config.Msi', 'Documents and Settings', 'DumpStack.log', 'DumpStack.log.tmp', 'edb',
# 'ESD', 'hiberfil.sys', 'inetpub', 'Intel', 'KMSpico Install', 'KMSpico Install.rar', 
# 'LastBak.ini', 'MSOCache', 'NPAVSCN.DAT', 'NPKey.txt', 'OneDriveTemp', 'OSGeo4W', 
# 'pagefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 
# 'Recovery', 'swapfile.sys', 'System Volume Information', 'Users', 'Windows', 'zv']
##########################################################

path1 = 'C:\Users\Admin\OneDrive\Desktop\python\30 days with vscode\12_modules'
file_name = 'dummy_file.txt'
a = os.path.join(path1, file_name)
os.remove(a)
print(f'{file_name} removed!')

dir_name = 'dummy_dir'
b = os.path.join(path1, dir_name)
os.rmdir(dir)

# operating system name depending on interpreters 
print(os.name)
## >> nt

# when files dont exist in given path
try:
    filename = 'abd.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
except IOError:
    print('Problem reading  '+ filename)

# 
file1 = 'abc.txt'
f = open(file1, 'w')
f.write('Hello')
f.close()
file_read = open(file1, 'r')
text = file_read.read()
print(text)

#file_popen = os.popen(file1, 'w')
#file_popen.write('Shreya')
#os.close(file_popen)

#os.rename(file1, 'New.txt')

#os.remove(file1)

print(os.path.exists(file1))
print(os.path.exists('abd.txt'))
# >> True
# >> False
print("SIze of file: ", os.path.getsize(file1))
# >> SIze of file:  5
 