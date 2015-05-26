
Name:           python-shadowsocks
Version:        2.6.9
Release:        1%{?dist}
Summary:        A fast tunnel proxy written in Python

License:        Apache 2.0
Group:          Applications/Internet
URL:            https://github.com/shadowsocks/shadowsocks
#Source0:        

BuildArch:      noarch
BuildRequires:  python-devel python-pip python-setuptools
Requires:	python libsodium
%description

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

pip install shadowsocks==%{version} --install-option="--prefix=%{buildroot}" --ignore-installed

%files
/bin/ssserver
/bin/sslocal
/lib/python2.7/site-packages/shadowsocks/*
/lib/python2.7/site-packages/shadowsocks-%{version}-py2.7.egg-info/*

%changelog
* Mon May 25 2015 peter
- 
