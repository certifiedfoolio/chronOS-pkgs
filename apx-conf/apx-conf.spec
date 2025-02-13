Name:           apx-conf
Version:        1.0.0
Release:        %autorelease
Summary:        Default configs for apx

License:        GPL-3.0-only
Source0:        https://github.com/Vanilla-OS/vanilla-apx-configs/archive/refs/tags/v%{version}.tar.gz

%description
Default configs for Vanilla-OS/apx.

%prep
mkdir -p %{?buildroot}/usr/share/apx

%build

%install
tar -xvf %{SOURCE0}
cp -r stacks %{?buildroot}/usr/share/apx
cp -r package-managers %{?buildroot}/usr/share/apx

%files
%{datadir}/apx/*

%changelog
%autochangelog