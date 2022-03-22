#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-logilab_common
Version  : 1.9.1
Release  : 85
URL      : https://files.pythonhosted.org/packages/bf/12/ba16f7d0c1c7152210b2417b927d89e9e399b0a9e84c886e3339e68cd286/logilab-common-1.9.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/12/ba16f7d0c1c7152210b2417b927d89e9e399b0a9e84c886e3339e68cd286/logilab-common-1.9.1.tar.gz
Summary  : collection of low-level Python packages and modules used by Logilab projects
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: pypi-logilab_common-bin = %{version}-%{release}
Requires: pypi-logilab_common-license = %{version}-%{release}
Requires: pypi-logilab_common-python = %{version}-%{release}
Requires: pypi-logilab_common-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(mypy_extensions)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(typing_extensions)
BuildRequires : pytest

%description
Logilab's common library
========================
What's this ?
-------------
This package contains some modules used by different Logilab projects.

%package bin
Summary: bin components for the pypi-logilab_common package.
Group: Binaries
Requires: pypi-logilab_common-license = %{version}-%{release}

%description bin
bin components for the pypi-logilab_common package.


%package license
Summary: license components for the pypi-logilab_common package.
Group: Default

%description license
license components for the pypi-logilab_common package.


%package python
Summary: python components for the pypi-logilab_common package.
Group: Default
Requires: pypi-logilab_common-python3 = %{version}-%{release}

%description python
python components for the pypi-logilab_common package.


%package python3
Summary: python3 components for the pypi-logilab_common package.
Group: Default
Requires: python3-core
Provides: pypi(logilab_common)
Requires: pypi(mypy_extensions)
Requires: pypi(setuptools)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-logilab_common package.


%prep
%setup -q -n logilab-common-1.9.1
cd %{_builddir}/logilab-common-1.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647986921
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-logilab_common
cp %{_builddir}/logilab-common-1.9.1/COPYING %{buildroot}/usr/share/package-licenses/pypi-logilab_common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/logilab-common-1.9.1/COPYING.LESSER %{buildroot}/usr/share/package-licenses/pypi-logilab_common/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}*/usr/bin/pytest

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/logilab-pytest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-logilab_common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/pypi-logilab_common/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
