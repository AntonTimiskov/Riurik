import os
import settings, resources
from django.core.cache import cache

def getWorkingDir():
	return settings.STATIC_TESTS_ROOT

def mkdir(path, name):
	try:
		fullpath = os.path.join(getWorkingDir(), path.strip('/'), name)
		os.mkdir(fullpath)
	except Exception, e:
		return str(e)
	
	return resources.ok

def remove(path):
	try:
		fullpath = os.path.join(getWorkingDir(), path.strip('/'))
		if os.path.isdir(fullpath):
			import shutil
			shutil.rmtree(fullpath)
		else:
			os.remove(fullpath)
	except Exception, e:
		print e
		return str(e)
	
	return resources.ok

def mksuite(path, name):
	try:
		fullpath = os.path.join(getWorkingDir(), path.strip('/'), name)
		os.mkdir(fullpath)
		filename = os.path.join(fullpath, settings.TEST_CONTEXT_FILE_NAME)
		f = open(filename, 'w')
		f.close()
	except Exception, e:
		return (False, str(e))
	
	return (True, os.path.join(name, settings.TEST_CONTEXT_FILE_NAME))

def mktest(path, name):
	try:
		filename = os.path.join(name + settings.TEST_FILE_EXT)
		fullpath = os.path.join(getWorkingDir(), path.strip('/'), filename)
		f = open(fullpath, 'w')
		f.close()
	except Exception, e:
		return (False, str(e))
	
	return (True, filename)

def resolveRemoteAddr(host):
	import socket
	return cache.get(host, socket.gethostbyname(host))

def remotesavetest(host, data):
	import urllib, urllib2
	post = urllib.urlencode(data)
	url = "http://%s:8000/actions/remote/save/" % resolveRemoteAddr(host)
	print url
	return urllib2.urlopen(url, post).read()

def savetest(content, path):
	try:
		fullpath = os.path.normpath(os.path.join(getWorkingDir(), path.strip('/')))
		if not os.path.exists(os.path.dirname(fullpath)):
			os.makedirs(os.path.dirname(fullpath))
			
		f = open(fullpath, 'w')
		f.write(content.replace('\r', ''))
		f.close()
	except Exception, e:
		return str(e)
	
	return resources.ok

def gettest(path):
	try:
		fullpath = os.path.normpath(os.path.join(getWorkingDir(), path.strip('/')))
		f = open(fullpath, 'r')
		content = f.read()
		f.close()
	except Exception, e:
		return str(e)
	
	return content