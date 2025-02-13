Name:		grimblast
Version:	2.4.4
Release:	%autorelease
Summary:	Hyprland screenshot utility

License:	MIT
URL:		https://github.com/hyprwm/contrib
%if 0%{?shortcommit:1}
Source0:	https://github.com/hyprwm/contrib/archive/%{commit}/contrib-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/hyprwm/contrib/archive/v%{version}.tar.gz#/contrib-v%{version}.tar.gz
%endif

BuildRequires:  scdoc

Requires:   

%description
Hyprland screenshot utility using grim and slurp

%prep
%autosetup %{?commit:-n contrib-%{commit}}

%build

%install
%make_install

%files
%{datadir}/man/man1/*
%{_bindir}/grimblast

%changelog
%autochangelog
