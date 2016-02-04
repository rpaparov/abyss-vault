def log(message):
	with open('/tmp/aqua-vault.log', 'a') as f:
		f.write(str(message)+'\n')
