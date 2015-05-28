#!/bin/sh

DIR=$PWD/$1
SPEC=$DIR/$1.spec
HEAD="[BUILD]"

if [[ -d $DIR && -f $SPEC ]]; then
  echo "$HEAD Cleaning up for $1"
  OUT=$PWD/out
  rm -rf $OUT
  mkdir -p $OUT

  echo "$HEAD Fetching source for $1"
  mkdir -p $OUT/SOURCES
  pushd $OUT/SOURCES
  spectool -g $SPEC
  popd
  if [ -d $DIR/src ]; then
    pushd $DIR
    tar czvf $OUT/SOURCES/src.tar.gz src
    popd
  fi

  echo "$HEAD Calling rpmbuild for $1"
  rpmbuild --define "_topdir $OUT" -ba $SPEC
  echo "$HEAD Build finished."
  echo `ls $OUT/RPMS/*/`

else
  echo "usage: build.sh PACKAGE"
fi
