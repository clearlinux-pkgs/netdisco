#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : netdisco
Version  : 2.8.0
Release  : 17
URL      : https://files.pythonhosted.org/packages/b4/88/38297c300b480129f5c4dfbe23f56658f37794c931811d4651893d0f6c03/netdisco-2.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/88/38297c300b480129f5c4dfbe23f56658f37794c931811d4651893d0f6c03/netdisco-2.8.0.tar.gz
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
Provides: pypi(netdisco)
Requires: pypi(requests)
Requires: pypi(zeroconf)

%description python3
python3 components for the netdisco package.


%prep
%setup -q -n netdisco-2.8.0
cd %{_builddir}/netdisco-2.8.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593529883
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/netdisco
cp %{_builddir}/netdisco-2.8.0/LICENSE.md %{buildroot}/usr/share/package-licenses/netdisco/4a606a34022a7ef2eab88e43148dd48547d3c017
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/netdisco/4a606a34022a7ef2eab88e43148dd48547d3c017

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
