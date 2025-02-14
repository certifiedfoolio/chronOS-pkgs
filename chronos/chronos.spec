%global debug_package %{nil}
%global vendor chronos

Name:           chronos
Version:        0.1.4
Release:        1%{?dist}
Summary:        chronOS branding

License:        CC-BY-CA
URL:            https://github.com/ublue-os/packages
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

%description
Branding for chronOS

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_datadir}/pixmaps \
    %{buildroot}%{_datadir}/ublue-os \
    %{buildroot}%{_sysconfdir}
mv logos/* %{buildroot}%{_datadir}/pixmaps
mv fastfetch/fastfetch.jsonc %{buildroot}%{_datadir}/ublue-os/fastfetch.jsonc
mv plymouth %{buildroot}%{_datadir}

%files
%{_datadir}/pixmaps/fedora*
%{_datadir}/pixmaps/system-*
%{_datadir}/pixmaps/ublue-*
%{_datadir}/ublue-os/fastfetch.jsonc
%{_datadir}/plymouth