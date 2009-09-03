#!/usr/bin/env python

"""\
%prog PACKAGE

Convert a package source directory into a tarball ready for submission to
SlackBuilds.org
"""

import os
import subprocess
import sys
import tempfile


def main(args):
    if len(args) <= 0:
        sys.exit("Invalid number of arguments")
    package_name = args[0]
    tempdir = tempfile.mkdtemp()
    subprocess.call(["rsync",
                     "--recursive",
                     "--cvs-exclude",
                     "--exclude", ".svn",
                     "--exclude", ".git",
                     "--exclude", "*.tar.*",
                     package_name, tempdir])
    subprocess.call(["tar",
                     "--create",
                     "--file", "%s.tar" % package_name,
                     "--directory", tempdir, "."])
    subprocess.call(["bzip2", "%s.tar" % package_name])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
