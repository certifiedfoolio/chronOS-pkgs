%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define pythons python3
%global debug_package %{nil}
Name:           python-materialyoucolor
Version:        2.0.10
Release:        1%{?dist}
Summary:        Material You color algorithms for Python
License:        MIT
URL:            https://github.com/T-Dynamos/materialyoucolor-python
Source0:        %{url}/archive/v%{version}/materialyoucolor-python-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel >= 0.37.1}
BuildRequires:  %{python_module regex}
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
Requires:       python3-pillow

%description
Python port of material-color-utilities used for Material You colors.

%prep
%autosetup -p1 -n materialyoucolor-python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{$python3_sitearch}/materialyoucolor/

%files
%license LICENSE
%{python3_sitearch}/materialyoucolor/
%{python3_sitearch}/materialyoucolor-%{version}*.*-info/

%changelog
%autochangelog
