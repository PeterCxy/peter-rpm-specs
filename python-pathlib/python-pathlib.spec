Name:		python-pathlib
Version:	1.0.1
Release:	1%{?dist}
Summary:	Pathlib offers a set of classes to handle filesystem paths

License:	MIT
URL:		https://pypi.python.org/pypi/pathlib

BuildArch:	noarch
BuildRequires:	python-pip python-devel python-setuptools

%description


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}

pip install pathlib==%{version} --install-option="--prefix=%{buildroot}" --ignore-installed

%files
/lib/python2.7/site-packages/pathlib.*
/lib/python2.7/site-packages/pathlib-%{version}-py2.7.egg-info/*

%changelog
* Tue May 26 2015 peter
-
