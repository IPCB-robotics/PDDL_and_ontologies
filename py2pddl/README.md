!!!!! Requirements !!!!!

    Python 3.6
    python-fire (pip install fire)


########## You need to check the python version  ##########

    python3 -V


Install pip3 for python3: 

    sudo apt install python3-pip


## Install Java


To install this version, we first need to update apt's package list:

    sudo apt update

Then check that Java is already installed:

    java -version

If Java is not installed, you will see the following message:

    Output
    Command 'java' not found, but can be installed with:

    apt install default-jre            
    apt install openjdk-11-jre-headless
    apt install openjdk-8-jre-headless 

Run the following command to install OpenJDK:

    sudo apt install default-jre

Check the installation with:

    java -version
