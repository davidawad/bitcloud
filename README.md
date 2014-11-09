# Bitcloud

This is a flask web app that mines bitcoins in the cloud !

Its mining software runs in python, so it's nno fst, it's mostly just a cool proof of concept. 

The fun part of this is that you can actually see the bitcoins being mined!

It also uses the sendgrid api for the email sharing the app to other people.

Please enjoy the interface! I love it.


If you want to make pull requests please send me an email first describing your changes first and preferably a link to a runnable.com host of it. Thanks!

I'll be adding pythonparallel clustering support soon!

#How to use
##!!THIS GUIDE WAS BUILT FOR AN UBUNTU MACHINE!!

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

```bash
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

##Installing bitcoind

```bash
sudo apt-get install python-software-properties
```
Add the bitcoin PPA to get access to the libdb4.8++-dev package:

```bash
add-apt-repository ppa:bitcoin/bitcoin
apt-get update
```

Now you can install EVEN MORE dependencies:

```bash
apt-get install libboost-all-dev libdb4.8-dev libdb4.8++-dev
```
Put the bitcoind binary that you built from the previous tutorial in the /usr/local/bin directory. Then add a symlink in /usr/bin:

```bash
ln -s /usr/local/bin/bitcoind /usr/bin/bitcoind
```
Before starting bitcoind, you'll want to create the bitcoin.conf configuration file:
```bash
cd ~/
mkdir .bitcoin
cd .bitcoin
vim bitcoin.conf
```
Add the following to bitcoin.conf 
```conf 
server=1
daemon=1
testnet=1
rpcuser=UNIQUE_RPC_USERNAME
rpcpassword=UNIQUE_RPC_PASSWORD
```
replace the values with the ones I have below
####note: these are example values. 
```bash
rpcuser=bitcoinrpc
rpcpassword=HmEkqcUW1C8tCGLUamKYSK3AWWYLmLBiacFLRBeC8x4D
```
In the config.cfg you might notice it looks something like this.

```cfg 
host=127.0.0.1
port=8332

rpcuser=bitcoinrpc
rpcpass=HmEkqcUW1C8tCGLUamKYSK3AWWYLmLBiacFLRBeC8x4D
```
####Note that the prcuser and the rpcpass are the SAME values as in the bitcoin.conf that bitcoind is using

Once you've got all this set up you can finally run th server.


## Run the flask server

In your terminal, navigat to the repo's directory and run app.py
```
cd [folder containing flask app]
python app.py
```

1. Access app from localhost:5000 or [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

2. ???

3. Profit. Literally.

#Contributors
Built off of [pyminer](https://github.com/jgarzik/pyminer) by [jgarzik](https://github.com/jgarzik)

[Nikolas Rassoules](http://www.gotchagoodside.com/)

Will be improved with [pyminer](https://github.com/daedalus/pyminer) by [deadalus](https://github.com/daedalus/) to add parallel clustering

#Sources
Inspired by [idigdoge](http://www.idigdoge.com/) by [https://github.com/7THStage](https://github.com/7THStage/idigdoge)

[Ken Shirriff](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)
also his [other post](http://www.righto.com/2014/02/bitcoin-mining-hard-way-algorithms.html)

[degreesofzero](https://degreesofzero.com/article/installing-bitcoind-on-ubuntu.html) for their guides on setting up bitcoind


