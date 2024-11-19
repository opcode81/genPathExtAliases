genPathExtAliases
=================

Windows supports a configurable set of file extensions which can be executed when found on the PATH.
These extensions are configured in the PATHEXT envioronment variable.

Bash shells for Linux (e.g. Git-Bash) will typically only execute .exe files they find on the PATH.
This tool generates a shell script containing alias definitions for files that are executable on Windows.
This shell script can then be sourced in e.g. `.bash_profile` to make the respective programs executible in Bash.
For instance, for the msys-based Git-Bash, run

    python genPathExtAliases.py msys

which will generate the file `./pathextAliases.sh`.
Then add this line to, for example, `.bash_profile`:

    source /path/to/genPathExtAliases/pathextAliases.sh
