Name:		python-thefuck
Version:	1.34
Release:	1%{?dist}
Summary:	A commandline auto-correction tool

URL:		https://github.com/nvbn/thefuck
License:	MIT

BuildArch:	noarch
BuildRequires:	python-devel python-pip python-setuptools python-pathlib python-colorama python-psutil python-six
Requires:	python python-pathlib python-colorama python-psutil python-six

%description
Magnificent app which corrects your previous console command, inspired by a @liamosaur tweet.

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

pip install thefuck==%{version} --root=%{buildroot} --ignore-installed

rm -rf %{buildroot}/usr/lib*/python2.7/site-packages/{pathlib,colorama,psutil,six}*
rm -rf %{buildroot}/usr/lib*/python2.7/site-packages/*.so

%files
/usr/bin/thefuck
/usr/bin/thefuck-alias
/usr/lib/python2.7/site-packages/thefuck-%{version}-py2.7.egg-info/*
/usr/lib/python2.7/site-packages/thefuck/*

%changelog
* Tue May 26 2015 peter
-
