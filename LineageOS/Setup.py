import os
def print_menu(): 
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. ROM Builder"
    print "2. Install Tools"
    print "3. Repo Install/Sync"
    print "4. Information"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
	os.system("python LineageOS/ROM-Builder.py")
    elif choice==2:
	os.system("apt-get install bc bison build-essential curl flex g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline6-dev lib32z1-dev libesd0-dev liblz4-tool libncurses5-dev libsdl1.2-dev libwxgtk2.8-dev libxml2 libxml2-utils lzop pngcrush schedtool squashfs-tools xsltproc zip zlib1g-dev openjdk-8-jdk --yes")
	os.system("mkdir -p ~/bin")
	os.system("mkdir -p ~/android/system")
	os.system("curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo")
	os.system("chmod a+x ~/bin/repo")
	os.system("cat Setup.cfg | head -n 4 >> ~/.profile")
	os.system("source ~/.profile")
    #elif choice==3:
	os.system("python LineageOS/Repo-Setup.py")
   #elif choice==4:
    elif choice==5:
	exit()
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        raw_input("Wrong option selection. Enter any key to try again..")

