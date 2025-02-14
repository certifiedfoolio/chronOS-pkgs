%define debug_package %{nil}
%define datadir /usr/share

Name:           grimblast
Version:        0.1
Release:        %autorelease
Summary:        Hyprland screenshot utility

License:        MIT
Source0:        https://github.com/hyprwm/contrib/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  scdoc
BuildRequires:  make

Requires:   grim
Requires:   slurp
Requires:   hyprctl
Requires:   hyprpicker
Requires:   wl-clipboard
Requires:   jq
Requires:   notify-send

%description
Hyprland screenshot utility using grim and slurp

%build
tar -xvf %{SOURCE0}
cd contrib-%{version}/grimblast
%make_build

%install
ls -lah
cd contrib-%{version}/grimblast
install -v -D -m 0644 grimblast.1 --target-directory "%{buildroot}/usr/share/man/man1/"
install -v -D -m 0755 grimblast --target-directory "%{buildroot}/usr/bin/"

%files
%{datadir}/man/man1/*
%{_bindir}/grimblast

%changelog
%autochangelog
