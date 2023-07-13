#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-logilab_common
Version  : 1.10.0
Release  : 105
URL      : https://files.pythonhosted.org/packages/cb/65/69b03e6fd83e2c2a29b991db5f22b1cbe0a9dc6fd297cf4a7972c97ff613/logilab-common-1.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/65/69b03e6fd83e2c2a29b991db5f22b1cbe0a9dc6fd297cf4a7972c97ff613/logilab-common-1.10.0.tar.gz
Summary  : collection of low-level Python packages and modules used by Logilab projects
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: pypi-logilab_common-bin = %{version}-%{release}
Requires: pypi-logilab_common-license = %{version}-%{release}
Requires: pypi-logilab_common-python = %{version}-%{release}
Requires: pypi-logilab_common-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: pypi(importlib_metadata)
Requires: pypi(mypy_extensions)
Requires: pypi(setuptools)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-logilab_common package.


%prep
%setup -q -n logilab-common-1.10.0
cd %{_builddir}/logilab-common-1.10.0
pushd ..
cp -a logilab-common-1.10.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689261150
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-logilab_common
cp %{_builddir}/logilab-common-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-logilab_common/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/logilab-common-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/pypi-logilab_common/9a1929f4700d2407c70b507b3b2aaf6226a9543c || :
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
