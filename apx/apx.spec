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

BuildArch:	noarch

BuildRequires:	go 
BuildRequires:	git
BuildRequires:  make

Requires:	podman

%description
Apx is the default package manager in Vanilla OS, now availble on Fedora Copr repositories. It is a wrapper around multiple package managers to install packages and run commands inside a managed container.

%prep
%autosetup %{?commit:-n %{name}-%{commit}}

%build
%make_build

%install
%make_install
make install-manpages

%changelog
%autochangelog
