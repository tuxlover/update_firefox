#!/usr/bin/env python3

import os 
import tarfile
from urllib import request

ARCH = "i686" #valid valiues are i686 or x86_64
LANG = "de"  # specifies the language for the script to update. have a look at mozilla.org to see which languages are siupported
baseurl = "https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest/" #this is the url of the server.
current_userhome = os.getenv('HOME')
receive_url = current_userhome+"/Downloads/"+"firefox_latest.tar.bz2"
tar_url = current_userhome+"/"+"Downloads/"
install_path = "/usr/local/share/alternatives/firefox" #path for installation if root

# we look and store the local version of firefox in this function
def firefox_get_version_string(inputString):
    firefox_version_string = os.popen(inputString).read()
    
    # short name for firefox version number
    fvn = " "

    for i in firefox_version_string:
        if i.isalpha() != True and i != "-" :
            fvn  = fvn  + i

    return fvn.strip()

def unpack_firefox(archfile,pathuri):
	new_file = tarfile.open(archfile)
	if os.getlogin() == "root": 
		new_file.extractall(path=install_path)
		new_file.close()
	else:
		new_file.extractall(path=tar_url)
		new_file.close()

firefox_version_remote = (firefox_get_version_string("curl -s -l ftp.mozilla.org/pub/mozilla.org/firefox/releases/latest/linux-i686/de/|awk -F "".tar.bz2"" {'print $1'}"))

# uncomment this for testing
#firefox_version_local = "firefox-0.0.0" 
firefox_version_local = (firefox_get_version_string("firefox -v"))
download_url =  baseurl+"linux"+"-"+ARCH+"/"+LANG+"/"+"firefox-"+firefox_version_remote+".tar.bz2"



if firefox_version_remote == firefox_version_local:
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("This is a Testphase for autoupdate firefox")
    print("version is up to date")
    print("no update required")
else:
    print("++++++++++++++++++++++++++++++++++++++++++")
    print("This is a Testphase for autoupdate firefox")
    print("version differs. There might be a newer version available on the remote server")
    print("wait until i get it for you ....")
    print(download_url)
    request.urlretrieve(download_url, receive_url)
    print ("downloaded to"+ " "+receive_url)
    print("now unpacking ...")
    unpack_firefox(receive_url,tar_url)
    print("for now update must be done manually")

"""" 
TODO:
unpack and move tar.bz2 file
change ownership and rights to root:root and 755
set symlink to /usr/locacl/share/alternative
check which user is logged in and if a certain directory to download to exists
pretty up code
"""
