Name:		apx-conf
Version:	1.0.0
Release:	%autorelease
Summary:	Default configs for apx

License:	GPL-3.0-only
URL:		https://github.com/Vanilla-OS/vanilla-apx-configs
%if 0%{?shortcommit:1}
Source0:	https://github.com/Vanilla-OS/vanilla-apx-configs/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:	https://github.com/Vanilla-OS/vanilla-apx-configs/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
%endif

%description
Apx is the default package manager in Vanilla OS, now availble on Fedora Copr repositories. These are the default configs for it.

%prep
%autosetup %{?commit:-n %{name}-%{commit}}
mkdir -p %{?buildroot}/usr/share/apx

%build

%install
cp -r package-managers %{?buildroot}/usr/share/apx

%files
%{datadir}/apx/*

%changelog
%autochangelog