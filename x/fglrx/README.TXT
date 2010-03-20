This is a SlackBuild for re-packing a snapshot of the fglrx driver that supports X Server 1.7
(plus a patch from ARCH to add support for 2.6.33)

The pre-release tarball can be obtained from Ubuntu here:

http://archive.ubuntu.com/ubuntu/pool/restricted/f/fglrx-installer/fglrx-installer_8.660.orig.tar.gz

Then just build & install as per a normal package. I have only tested this on x86-64, so I don't
know if 32 bit support actually works.

Many thanks to the maintainer of the ARCH PKGBUILD, Vi0L0, who did most of the hard work of
figuring out how to build and package this driver properly.

Carlos Corbacho
20th March 2010
