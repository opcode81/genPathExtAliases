from __future__ import print_function
import os
import re
import sys

BLACKLIST_DIRNAME_REGEX = ["Miniconda.*", ".conda"]
BLACKLIST_ALIAS = ["eval"]

if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) != 1 or args[0] not in ("msys", "cygwin"):
		print("usage: genPathextAliases <cygwin|msys>")
		sys.exit(1)
	extensions_to_process = [s.lower() for s in os.getenv("PATHEXT").split(";")]
	print("Processing extensions %s" % extensions_to_process)
	with open("pathextAliases.sh", "w") as f:
		paths = os.getenv("PATH").split(os.path.pathsep)
		for path in paths:
			print("Processing path %s" % path)
			if not os.path.exists(path):
				continue

			# split path into parts and check if any part matches the blacklist
			blacklisted = False
			for part in path.split(os.path.sep):
				for regex in BLACKLIST_DIRNAME_REGEX:
					if re.match(regex, part):
						blacklisted = True
						break
				if blacklisted:
					print("Skipping blacklisted path %s" % path)
					break
			if blacklisted:
				continue

			for ext in extensions_to_process:
				if ext in (".exe", ".com"):
					continue
				for file in os.listdir(path):
					if file[-len(ext):].lower() == ext:
						p = os.path.join(path, file)
						if args[0] == "msys":
							p = p.replace("\\", "/")
							alias = file[:-len(ext)]
							cmd = '''python -c "import subprocess; from sys import argv; subprocess.Popen([\\"cmd\\", \\"/c\\", \\"%s\\"] + argv[1:])"''' % p
						else:
							p = re.sub(r"/cygdrive/(\w)", r"\1:", p)
							alias = file[:-len(ext)]
							cmd = ('cmd /c "%s"' % p).replace('\\', '/')
						if alias in BLACKLIST_ALIAS:
							print("Skipping alias %s" % alias)
							continue
						alias_definition = "alias %s='%s'\n" % (alias, cmd)
						print("Adding %s" % alias_definition.strip())
						f.write(alias_definition)
