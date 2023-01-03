import os, platform
os.system('git pull')

import requests

bit = platform.architecture()[0]

if bit == '64bit':
    from USMI64 import fia
    fia()

elif bit == '32bit':

    from USMI import fia

    fia()
