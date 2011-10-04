#!/bin/sh

DIRNAME=wayland
PACKAGENAME=${DIRNAME}-0.1
GITPRJ=/root/wayland
#SRC_VER=21e877f3f6ac0a5b88b69d0eb4850f962af3b4cb
pushd $GITPRJ
if ! git describe >/dev/null 2>/dev/null; then
   count=$(git rev-list HEAD | wc -l)
   realcommitid=$(git describe --always)
   commitid=$count.g$realcommitid
else
   commitid=$(expr match $(git describe) '.*-\([0-9]*-g[a-z0-9]*\)$' \
              | tr - .)
   realcommitid=$commitid
fi
echo $commitid
popd

GIT_DIR=$GITPRJ/.git git archive --format=tar --prefix=$PACKAGENAME~git$commitid/ $realcommitid \
	| bzip2 > $PACKAGENAME~git$commitid.tar.bz2

# rm -rf $DIRNAME
