from flask import Flask,render_template,request,redirect,url_for
from multiprocessing import Process
import dataset,random,sys,sendgrid,time,json,pprint,hashlib,struct,re,base64,httplib,subprocess
from shelljob import proc
import flask,eventlet
app = flask.Flask(__name__)

eventlet.monkey_patch()

sg = sendgrid.SendGridClient('','')

# Connnect to database
db = dataset.connect('sqlite:///file.db')

# create your guests table
table = db['guests']


# when someone sends a GET to / render sign_form.html
@app.route('/', methods=['GET'])
def sign_form():	

	return render_template('sign_form.html')


# when someone sends a GET to /guest_book render guest_book.html
@app.route('/miner')
def miner():
	#time.sleep(30) #delays the mining script from executing 
	#return render_template('miner.html' , time = time.asctime() )
	g = proc.Group()
	p = g.run( [ "python" , "-u" ,"pyminer.py" , "config.cfg" ] )

   	def read_process():
		while g.is_pending():
			lines = g.readlines()
			for proc, line in lines:
				yield line + "\n\n"

	return flask.Response( read_process(), mimetype= 'text/event-stream' )
	#mineMaster()
	#id=subprocess.Popen(["./pyminer.py", "./config.cfg"], stdout=subprocess.PIPE)
	#print id.pid 
	#return render_template('miner.html' , time = time.asctime() )		

# when someone sends  POST to /submit, take the name and message from the body
# of the POST, store it in the database, and redirect them to the guest_book



@app.route('/email', methods=['POST'])
def email():
	#signature = dict(name=request.form['name'], message=request.form['message'] , email=request.form['email'])
	name=request.form['name']
	message=request.form['message']
	email=request.form['email']
	#sendgrid sends an email to whoever wants
	message=sendgrid.Mail()
	message.add_to( str( request.form['email'] ) ) 
	message.add_bcc('davidawad64@gmail.com') ##sends me a BCC of the email for debugging ##
	message.set_subject("Mine Bitcoins in the cloud!") ##reassures the customer
	message.set_html('thanks.html')
	message.set_text('Hey, '+str(name)+' you should mine bitcoins in the cloud! Check out the project at https://github.com/DavidAwad/bitcloud')
	message.set_from('BitCloud <David@bitcloud.io>')
	status, msg = sg.send(message)
	return

@app.errorhandler(404)
def new_page(error):
	pagepath = request.path.lstrip('/')
	return render_template('error.html', pagepath=pagepath)

app.run(debug=True)
