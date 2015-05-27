Name:		iojs
Version:	2.1.0
Release:	1%{?dist}
Summary:	Evented I/O for V8 JavaScript - Node.js fork

License:	MIT
Group:		Development/Languages
URL:		http://iojs.org
Source0:	https://iojs.org/dist/v%{version}/iojs-v%{version}.tar.gz

BuildRequires:	python zlib-devel gcc gcc-c++ glibc-devel
Requires:	zlib glibc
Conflicts:	nodejs

%description
A fork of Node.js. Built with bundled openssl.

%prep
%setup -qn %{name}-v%{version}

%build
./configure \
   --prefix=/usr \
   --shared-zlib \
   --without-npm

make

%install
make DESTDIR=%{buildroot} install

%files
/usr/bin/iojs
/usr/bin/node
/usr/include/node/*
/usr/lib/debug/usr/bin/iojs.debug
/usr/lib/debug/usr/bin/node.debug
/usr/share/man/man1/iojs.*
/usr/share/systemtap/tapset/node.stp
/usr/src/debug/iojs-v%{version}/*
%doc README.md LICENSE CHANGELOG.md

%changelog
* Tue May 26 2015 peter
-
