# Bitcloud

This is a flask web app that mines bitcoins in the cloud !

Its mining software runs in python, so it's nno fst, it's mostly just a cool proof of concept. 

The fun part of this is that you can actually see the bitcoins being mined!

It also uses the sendgrid api for the email sharing the app to other people.

Please enjoy the interface! I love it.


If you want to make pull requests please send me an email first describing your changes first and preferably a link to a runnable.com host of it. Thanks!

#How to use
##!This guide was written for an ubuntu machine!

So for this to work your going to need to have bitcoind installed and running on your computer. the bitcoind will have to be built from source. You can find that [here](https://github.com/bitcoin/bitcoin/releases)

```bash 
cd /usr/local/src;\
wget https://github.com/bitcoin/bitcoin/archive/v0.9.3	.tar.gz;

```
Extract the archive
```bash
cd /usr/local/src
tar -zxvf v0.9.3.tar.gz
```

##Dependencies
To get add-apt-repository, which we will use later to add the bitcoin PPA:
```bash
sudo apt-get install python-software-properties
```
Add the bitcoin PPA to get access to the libdb4.8++-dev package:

```bash 
add-apt-repository ppa:bitcoin/bitcoin
apt-get update
```
Now you can install and build the dependencies: 

```
apt-get install build-essential
apt-get install libtool autotools-dev autoconf
apt-get install libssl-dev
apt-get install libboost-all-dev libdb4.8-dev libdb4.8++-dev
apt-get install pkg-config
```
###Building bitcoind from source
Here are the commands to build it.
```bash
cd /usr/local/src/bitcoin-0.9.3
./autogen.sh
./configure --with-cli=no --with-gui=no
make
```
####This will take a little while. 
If you encounter errors during the build process, first try searching the [bitcoin](https://github.com/bitcoin/bitcoin) GitHub repo. 



## Run the flask server

1. In your terminal, navigat to the repo's directory and run app.py
```
cd [REPO LOCATION]
python app.py
```

2. Access app from localhost:5000 or [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
