#!/bin/sh

DIR=$PWD/$1
SPEC=$DIR/$1.spec
HEAD="[BUILD]"

if [[ -d $DIR && -f $SPEC ]]; then
  echo "$HEAD Cleaning up for $1"
  OUT=$PWD/out
  rm -rf out
  mkdir out
  echo "$HEAD Calling rpmbuild for $1"
  rpmbuild --define "_topdir $OUT" -ba $PWD/$1/$1.spec
  OUTFILE=$OUT/RPMS/*/$1-*.rpm
  if [ -f $OUTFILE ]; then
    echo "$HEAD Placing output"
    mv $OUT/RPMS/*/$1-*.rpm $OUT/
    echo "$HEAD Built package $1"
    echo `ls $OUT/$1-*.rpm`
  else
    echo "$HEAD Build failure"
  fi
else
  echo "usage: build.sh PACKAGE"
fi
