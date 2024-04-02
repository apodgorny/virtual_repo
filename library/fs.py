import hashlib
import os


class Fs:

	@staticmethod
	def checksum(path):
		if os.path.isfile(path):
			hash_sha256 = hashlib.sha256()
			with open(path, 'rb') as f:
				for chunk in iter(lambda: f.read(4096), b''):
					hash_sha256.update(chunk)
			return hash_sha256.hexdigest()
		elif os.path.isdir(path):
			hashes = []
			for root, dirs, files in os.walk(path):
				for file in files:
					hashes.append(Fs.checksum(os.path.join(root, file)))
			return hashlib.sha256(''.join(hashes).encode()).hexdigest()
		return None
