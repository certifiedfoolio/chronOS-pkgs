%define debug_package %{nil}
%define datadir /usr/share

Name:           grimblast
Version:        0.1
Release:        %autorelease
Summary:        Hyprland screenshot utility

License:        MIT
Source0:        https://github.com/hyprwm/contrib/archive/refs/tags/v%{version}.tar.gz

%description
Hyprland screenshot utility using grim and slurp

%build
tar -xvf %{SOURCE0}
cd contrib-%{version}
%make_build

%install
%make_install

%files
%{datadir}/man/man1/*
%{_bindir}/grimblast

%changelog
%autochangelog
