This Script is a simple solution for all those out there who love debian
but also want a solution to always keep firefox up to date.
 
 == Prequisites ==
A version of firefox must already be installed for this script to work.
 
  == What it does ==
It connects to the romote server and compares the two versions of firefox.
If compared to the string it finds a newer version at the server  it will
download the current version of firefox for you.
 
 == Does it work / BUGS ==
* it works for me 
* it work with 32 bit firefox but modifying it may result the script also to work with 64 bit as well.
 
I recommend to setup an alias to keep it simple:
for example just typing update in a command line after setting up this alias together with your update_firefox script will
allow you to have it all in one run:
alias update='sudo apt-get -y update && sudo apt-get -y --ignore-hold upgrade && sudo apt-get clean && sudo update_firefox && sudo -k'
 

