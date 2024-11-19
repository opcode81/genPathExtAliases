genPathExtAliases
=================

Windows supports a configurable set of file extensions which can be executed when found on the `PATH`.
Specifically, the extensions configured in the `PATHEXT` envioronment variable, e.g.

    PATHEXT=".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.LNK"

Unfortunately, Bash shells for Linux (e.g. Git-Bash) will typically only execute `.exe` files they find on the `PATH`.
This tool generates a shell script containing alias definitions for files that are executable on Windows.
This shell script can then be sourced in e.g. `.bash_profile` to make the respective programs executible in Bash.
For instance, for the msys-based Git-Bash, run

    python genPathExtAliases.py msys

which will generate the file `./pathextAliases.sh`.
Then add a line like the following `.bash_profile`:

    source /path/to/genPathExtAliases/pathextAliases.sh
