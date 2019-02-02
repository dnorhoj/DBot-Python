import json, os

#Change config to something else if you need to
FOLDER = "../config/"
CONFIG = "{}config.json".format(FOLDER)
SERVERCONF = "{}servers.json".format(FOLDER)
SECRET = "{}secret.json".format(FOLDER)

class serverNotFound:pass

#Gets a config value
def getConfig(server, setting):
	if not type(server) is str:
		try:
			server = server.message.server.id
		except:
			server = server.id

	with open(SERVERCONF) as json_file:  
		data = json.load(json_file)
		return data[server][setting]

#Sets a per-server congfig
def setConfig(server, setting, value):
	if not type(server) is str:
		server = server.message.server.id

	with open(SERVERCONF) as json_file:  
		data = json.load(json_file)
		data[server][setting] = value
		with open(SERVERCONF, 'w') as outfile:  
			json.dump(data, outfile, indent=4)

#Gets a global config
def getUConfig(setting):
	with open(CONFIG) as json_file:
		data = json.load(json_file)
		return data[setting]

#Sets a global config
def setUConfig(setting, value):
	with open(CONFIG) as json_file:  
		data = json.load(json_file)
		data[setting] = value
		with open(CONFIG, 'w') as outfile:  
			json.dump(data, outfile, indent=4)

#Makes a template for a new server
def setupServerConfig(server):
	with open(SERVERCONF) as json_file:
		data = json.load(json_file)
		data[server.id] = {}
		data[server.id]['name'] = server.name
		for x in data['sample']:
			data[server.id].update({str(x):data['sample'][x]})

		with open(SERVERCONF, 'w') as outfile:  
			json.dump(data, outfile, indent=4)

def serverConfix(server):
	with open(SERVERCONF) as json_file:
		data = json.load(json_file)
		try:
			data[server.id]
		except KeyError:
			setupServerConfig(server)
		return True

def getPrefix(server):
	try:
		return getConfig(server, "prefix")
	except:
		return getUConfig("prefix")

def getSecret(key):
	try:
		res = os.environ[key]
	except KeyError:
		try:
			with open(SECRET) as json_file:
				data = json.load(json_file)
				res = data[key]
		except FileNotFoundError:
			return ""
	return res