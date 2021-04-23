# trafficLigth.py

def switchLight(stopLight):
	for key in stopLight.keys():
		if stopLight[key] == 'green':
			stopLight[key] = 'yellow'
		elif stopLight[key] == 'yellow':
			stopLight[key] = 'red'
		elif stopLight[key] == 'red':
			stopLight[key] = 'green'
	assert 'red' in stopLight.values(), 'Neither light is red: ' + str(stopLight)