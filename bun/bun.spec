%define debug_package %{nil}
%define datadir /usr/share

Name:           bun
Version:        1.2.2
Release:        %autorelease
Summary:        Javascript/Typescript toolkit

License:        MIT
Source0:        https://github.com/oven-sh/bun/releases/download/bun-v%{version}/bun-linux-x64.zip

%description
Bun is an all-in-one toolkit for JavaScript and TypeScript apps. It ships as a single executable called bun.

%install
unzip %{SOURCE0}
install -v -D -m 0755 bun-linux-x64/bun --target-directory "%{buildroot}/usr/bin/"

%files
%{_bindir}/bun

%changelog
%autochangelog
