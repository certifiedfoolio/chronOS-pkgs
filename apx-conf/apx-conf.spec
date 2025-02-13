%define debug_package %{nil}
%define datadir /usr/share

Name:           apx-conf
Version:        1.0.0
Release:        %autorelease
Summary:        Default configs for apx

License:        GPL-3.0-only
Source0:        https://github.com/Vanilla-OS/vanilla-apx-configs/archive/refs/tags/v%{version}.tar.gz

%description
Default configs for Vanilla-OS/apx.

%install
mkdir -p %{?buildroot}/usr/share/apx
tar -xvf %{SOURCE0}
cp -r vanilla-apx-configs-%{version}/stacks %{?buildroot}/usr/share/apx
cp -r vanilla-apx-configs-%{version}/package-managers %{?buildroot}/usr/share/apx

%files
%{datadir}/apx/*

%changelog
%autochangelog