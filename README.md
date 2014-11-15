# Bitcloud

##This Hack was Awarded Second Place at Hack NJIT

This is a flask web app that mines bitcoins in the browser!

Its mining software runs in python, so it's not fast, it's mostly just a cool proof of concept. 

The fun part of this is that you can actually see the bitcoins being mined!

It also uses the sendgrid api for the email sharing the app to other people.


It will soon be able to mine bitcoins on the client AND the server together. If i can find the time to do that.


##What it's doing currently, 

Running the miner will execute a python script thats doing the actual mining and creating a web socket to it in your browser so you can see the output of the mining script itself. So it's mining the bitcoins for you, unfortunately because of how long it takes to actually mine bitcons (especially in python) There wasn't time to testor build the sending of them.


If you want to make pull requests please send me an email first describing your changes first and preferably a link to a runnable.com host of it. Thanks!

I'll be adding pythonparallel clustering support soon!

#How to use
##!!THIS GUIDE WAS BUILT FOR AN UBUNTU MACHINE!!
If you're on mac you'll need to follow [this](https://github.com/bitcoin/bitcoin/blob/master/doc/build-osx.md) tutorial. Just jump in at the how to run bitcoind.

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


## Configuring the flask server
You'll need to install even more fun things.
pip, in case you somehow don't have it. 
	 
```bash
sudo apt-get install python-pip
```
The python flask plugin
```
pip install flask
```
The sendgrid functionality
```
pip install sendgrid
```
For the SQLite database
```
pip install dataset
```
Shelljob
```
pip install flask shelljob
```
Gunicorn
```
pip install gunicorn eventlet
```

##Adding SendGrid functionality

in line 10 of [app.py](https://github.com/DavidAwad/bitcloud/blob/master/app.py#L10) you'll notice that the sendgrid credentials are blank. 

```python
sg = sendgrid.SendGridClient('','')
```

You need to fill this in with your OWN User Name / Password for it to send emails to people.


##Running the server
Open two terminals, inside of both of them navigate to the repo's directory containing app.py

In the two terminals run the commands in this order.
```
gunicorn -k eventlet app:app -w 4
```
and the server will start. In the other terminal type 
```
python app.py
```
Once that works you will access the front-end and can interact with it accordingly.

1. Access app from localhost:5000 or [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

2. ???

3. Profit. Literally.

##Possible Bugs
You may come across some errors where you will be left with some zombie processes. This is likely to happen if you run the app only with "python app.py"

If this is the case you may get an error like this
```bash
  File "app.py", line 73, in <module>
    app.run(debug=True)
  File "/usr/local/lib/python2.7/dist-packages/flask/app.py", line 772, in run
    run_simple(host, port, self, **options)
  File "/usr/local/lib/python2.7/dist-packages/werkzeug/serving.py", line 706, in run_simple
    test_socket.bind((hostname, port))
  File "/usr/lib/python2.7/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: [Errno 98] Address already in use
```
You could find these zombie processes using the command 
```bash
ps aux | grep python 
```
This will list out the processes that are being run by python that have become zombies.

Here's an example.
```bash
david     3380  0.0  0.1  47120 10140 pts/1    S    04:27   0:00 python -u pyminer.py config.cfg
david     3381  0.0  0.1  47120 10140 pts/1    S    04:27   0:00 python -u pyminer.py config.cfg
david     3382  0.0  0.1  47120 10140 pts/1    S    04:27   0:00 python -u pyminer.py config.cfg
david     3383  0.0  0.1  47120 10140 pts/1    S    04:27   0:00 python -u pyminer.py config.cfg
```

So you may have to manually kill all the processes, if for some reason sudo killall python doesn't work; just sudo kill 9 <pid> or in this case 3380 or something. 

#Contributors
Himanshu Chhetri for all his help at HackNJIT getting this off the ground.

[Nikolas Rassoules](http://www.gotchagoodside.com/) for his help with the front-end design I didn't have the time to work on.

Built off of [pyminer](https://github.com/jgarzik/pyminer) by [jgarzik](https://github.com/jgarzik).

Will be improved with the fork of [pyminer](https://github.com/daedalus/pyminer) by [deadalus](https://github.com/daedalus/) to add parallel clustering.

[hamiyoca](https://github.com/derjanb/hamiyoca) for the javascript implementations for the front end mining. 

#Sources
The [Bitcoin Developer Guide](https://bitcoin.org/en/developer-guide#block-chain) as it was really interesting and helpful to read to understand whats happening, not helpful at all to understand how to write it.

Inspired by [idigdoge](http://www.idigdoge.com/) by [https://github.com/7THStage](https://github.com/7THStage/idigdoge)

[Ken Shirriff](http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html)
also his [other post](http://www.righto.com/2014/02/bitcoin-mining-hard-way-algorithms.html)

[degreesofzero](https://degreesofzero.com/article/installing-bitcoind-on-ubuntu.html) for their guides on setting up bitcoind

[Mortoray](http://mortoray.com/2014/03/04/http-streaming-of-command-output-in-python-flask/) for his really helpful guide for terminal output to html. 

<br>

![Major League Hacking](http://mlh.io/assets/logos/mlh-small-text-21f0abdc906225a212cac33b7c6a5139.png) 
