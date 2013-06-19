import os
import re
import sys

if __name__ == '__main__':
	args = sys.argv[1:]
	if len(args) != 1 or args[0] not in ("msys", "cygwin"):
		print "usage: genPathextAliases <cygwin|msys>"
		sys.exit(1)
	with file("pathextAliases.sh", "wb") as f:
		for ext in map(str.lower, os.getenv("PATHEXT").split(";")):
			if ext in (".exe", ".com"): 
				continue
			paths = os.getenv("PATH").split(os.path.pathsep)
			for path in paths:
				if not os.path.exists(path):
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
						f.write("alias %s='%s'\n" % (alias, cmd))
