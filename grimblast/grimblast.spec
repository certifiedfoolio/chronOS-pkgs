%define datadir /usr/share
%define debug_package %{nil}

Name:		grimblast
Version:	0.1
Release:	%autorelease
Summary:	Hyprland screenshot utility

License:	MIT
URL:		https://github.com/hyprwm/contrib
Source0:	https://github.com/hyprwm/contrib/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  scdoc
BuildRequires:  make

Requires:   grim
Requires:   slurp
Requires:   hyprctl
Requires:   hyprpicker
Requires:   wl-copy
Requires:   jq
Requires:   notify-send

%description
Hyprland screenshot utility using grim and slurp

%install
tar -xzf ${SOURCE0}
cd v%{version}
%make_install

%files
%{datadir}/man/man1/*
%{_bindir}/grimblast

%changelog
%autochangelog
