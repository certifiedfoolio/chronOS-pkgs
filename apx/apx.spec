%define _distrobox_gitref 3b9f0e8d3d8bd102e1636a22afffafe00777d30b
%define datadir /usr/share
%define debug_package %{nil}

Name:		apx
Version:	2.4.4
Release:	%autorelease
Summary:	Wrapper for multiple package managers based on distrobox

License:	GPL-3.0-only
URL:		https://github.com/Vanilla-OS/apx
%if 0%{?shortcommit:1}
Source0:	https://github.com/Vanilla-OS/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/Vanilla-OS/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
%endif
Source1:    https://github.com/89luca89/distrobox/archive/%{_distrobox_gitref}/distrobox-%{_distrobox_gitref}.tar.gz

BuildRequires:	go 
BuildRequires:	git
BuildRequires:  make

Requires:	podman

%description
Apx is the default package manager in Vanilla OS, now availble on Fedora Copr repositories. It is a wrapper around multiple package managers to install packages and run commands inside a managed container.

%prep
%autosetup %{?commit:-n %{name}-%{commit}}
mkdir -p distrobox
tar -xvf %{SOURCE1}
mv distrobox-*/* distrobox

%build
%make_build

%install
%make_install
make install-manpages DESTDIR=%{?buildroot}

%files
%{datadir}/%{name}/distrobox/*
%{datadir}/man/man1/apx.1.gz
%{_bindir}/apx
/etc/apx/apx.json

%changelog
%autochangelog
