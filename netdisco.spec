#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netdisco
Version  : 2.6.0
Release  : 12
URL      : https://files.pythonhosted.org/packages/ae/73/2a60ac3292203ac75528b1ae9a475fac6fff690e906cbc13e744701b2436/netdisco-2.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ae/73/2a60ac3292203ac75528b1ae9a475fac6fff690e906cbc13e744701b2436/netdisco-2.6.0.tar.gz
Summary  : Discover devices on your local network
Group    : Development/Tools
License  : Apache-2.0
Requires: netdisco-license = %{version}-%{release}
Requires: netdisco-python = %{version}-%{release}
Requires: netdisco-python3 = %{version}-%{release}
Requires: requests
Requires: zeroconf
BuildRequires : buildreq-distutils3
BuildRequires : requests
BuildRequires : zeroconf

%description
# NetDisco
NetDisco is a Python 3 library to discover local devices and services. It allows to scan on demand or offer a service that will scan the network in the background in a set interval.

%package license
Summary: license components for the netdisco package.
Group: Default

%description license
license components for the netdisco package.


%package python
Summary: python components for the netdisco package.
Group: Default
Requires: netdisco-python3 = %{version}-%{release}

%description python
python components for the netdisco package.


%package python3
Summary: python3 components for the netdisco package.
Group: Default
Requires: python3-core

%description python3
python3 components for the netdisco package.


%prep
%setup -q -n netdisco-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554240649
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/netdisco
cp LICENSE.md %{buildroot}/usr/share/package-licenses/netdisco/LICENSE.md
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/netdisco/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
