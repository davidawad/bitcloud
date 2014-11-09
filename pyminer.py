#!/usr/bin/python


import time
import json
import pprint
import hashlib
import struct
import re
import base64
import httplib
import sys
from multiprocessing import Process



if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage: pyminer.py CONFIG-FILE"
		sys.exit(1)

	f = open(sys.argv[1])
	for line in f:
		# skip comment lines
		m = re.search('^\s*#', line)
		if m:
			continue

		# parse key=value lines
		m = re.search('^(\w+)\s*=\s*(\S.*)$', line)
		if m is None:
			continue
		settings[m.group(1)] = m.group(2)
	f.close()

	if 'host' not in settings:
		settings['host'] = '127.0.0.1'
	if 'port' not in settings:
		settings['port'] = 8332
	if 'threads' not in settings:
		settings['threads'] = 1
	if 'hashmeter' not in settings:
		settings['hashmeter'] = 0
	if 'scantime' not in settings:
		settings['scantime'] = 30L
	if 'rpcuser' not in settings or 'rpcpass' not in settings:
		print "Missing username and/or password in cfg file"
		sys.exit(1)

	settings['port'] = int(settings['port'])
	settings['threads'] = int(settings['threads'])
	settings['hashmeter'] = int(settings['hashmeter'])
	settings['scantime'] = long(settings['scantime'])

	thr_list = []
	for thr_id in range(settings['threads']):
		p = Process(target=miner_thread, args=(thr_id,))
		p.start()
		thr_list.append(p)
		time.sleep(1)			# stagger threads

	print settings['threads'], "mining threads started"

	print time.asctime(), "Miner Starts - %s:%s" % (settings['host'], settings['port'])
	try:
		for thr_proc in thr_list:
			thr_proc.join()
	except KeyboardInterrupt:
		pass
	print time.asctime(), "Miner Stops - %s:%s" % (settings['host'], settings['port'])

