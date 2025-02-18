%define debug_package %{nil}
%define datadir /usr/share

Name:		apx-gui
Version:	1.0.4
Release:	%autorelease
Summary:	A frontend in GTK 4 and Libadwaita for Apx

License:	GPL-3.0-only
URL:		https://github.com/Vanilla-OS/apx-gui
%if 0%{?shortcommit:1}
Source0:	https://github.com/Vanilla-OS/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/Vanilla-OS/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
%endif

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:  kernel-devel
BuildRequires:	meson
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconf-pkg-config
BuildRequires:	glib2-devel
BuildRequires:	gettext
BuildRequires:	gtk-update-icon-cache

Requires:	gettext
Requires:	python3
Requires:	python3-gobject
Requires:	python3-pyyaml
Requires:	python3-requests
Requires:	gobject-introspection
Requires:	vte291

%description
Libadwaita frontend for Vanilla-OS/apx.

%prep
%autosetup %{?commit:-n %{name}-%{commit}}

%files
%{datadir}/*
%{_bindir}/apx-gui

%build
%meson
%meson_build

%install
%meson_install

%changelog
%autochangelog
