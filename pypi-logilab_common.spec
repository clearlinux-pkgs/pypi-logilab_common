#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-logilab_common
Version  : 1.9.7
Release  : 100
URL      : https://files.pythonhosted.org/packages/f5/99/d0edc94e0742ca3423b48490c3905628239eec99f9b29d115ed7b578039a/logilab-common-1.9.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/99/d0edc94e0742ca3423b48490c3905628239eec99f9b29d115ed7b578039a/logilab-common-1.9.7.tar.gz
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
BuildRequires : pypi-pytest

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
%setup -q -n logilab-common-1.9.7
cd %{_builddir}/logilab-common-1.9.7
pushd ..
cp -a logilab-common-1.9.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395214
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-logilab_common
cp %{_builddir}/logilab-common-1.9.7/COPYING %{buildroot}/usr/share/package-licenses/pypi-logilab_common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/logilab-common-1.9.7/COPYING.LESSER %{buildroot}/usr/share/package-licenses/pypi-logilab_common/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
## Remove excluded files
rm -f %{buildroot}*/usr/bin/pytest
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
