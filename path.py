import os
import sys
import ctypes
from subprocess import call
cwd = str(os.getcwd())
ffmpeg = 'setx PATH "'+cwd+'\\ffmpeg\\bin;%PATH%"'
colmap = 'setx /m PATH "'+cwd+'\\COLMAP;%PATH%"'
tmp = cwd+'\\instant-ngp\\tmp'
os.system(ffmpeg)
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system(colmap)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
os.mkdir(tmp)
