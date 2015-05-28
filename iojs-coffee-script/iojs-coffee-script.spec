Name:		iojs-coffee-script
Version:	1.9.2
Release:	1%{?dist}
Summary:	A little language that compiles into JavaScript. 

Group:		Development/Languages
License:	MIT
URL:		http://coffeescript.org/
Source0:	src.tar.gz

BuildArch:	noarch
BuildRequires:	npm
Requires:	iojs
Conflicts:	coffee-script

%description
CoffeeScript is a little language that compiles into JavaScript. Underneath that awkward Java-esque patina, JavaScript has always had a gorgeous heart. CoffeeScript is an attempt to expose the good parts of JavaScript in a simple way.

%prep
%setup -qn src

%install
mkdir -p %{buildroot}/usr/lib
npm install coffee-script@%{version} --prefix=%{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/bin
install -m 0755 cake %{buildroot}/usr/bin
install -m 0755 coffee %{buildroot}/usr/bin
rm -rf %{buildroot}/usr/lib/node_modules/.bin

%files
/usr/bin/coffee
/usr/bin/cake
/usr/lib/node_modules/coffee-script/*
/usr/lib/node_modules/coffee-script/.npmignore

%changelog
* Wed May 27 2015 peter
-
