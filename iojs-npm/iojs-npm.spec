Name:		iojs-npm
Version:	2.11.0
Release:	1%{?dist}
Summary:	A JavaScript package manager

Group:		Development/Libraries
License:	MIT
URL:		https://www.npmjs.com
Source0:	https://github.com/npm/npm/archive/v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
Requires:	iojs
Provides:	npm

%description
A JavaScript package manager, built against iojs

%prep
%setup -qn npm-%{version}

%build
%configure
make

%install
npm_config_prefix=%{buildroot}/usr \
npm_config_root=%{buildroot}/usr/lib/node \
npm_config_binroot=%{buildroot}/usr/bin \
npm_config_manroot=%{buildroot}/usr/share/man \
make DESTDIR=%{buildroot} install

%files
/usr/bin/npm
/usr/lib/node_modules/npm/*
/usr/lib/node_modules/npm/.*
/usr/share/man/man*/
%doc README.md LICENSE

%changelog
* Wed May 27 2015 peter
-
