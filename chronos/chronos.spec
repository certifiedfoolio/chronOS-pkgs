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
%attr(0755,root,root) %{_datadir}/pixmaps/fedora*
%attr(0755,root,root) %{_datadir}/pixmaps/system-*
%attr(0755,root,root) %{_datadir}/pixmaps/ublue-*

%package fastfetch
Summary:        Fastfetch configuration for chronOS
License:        CC-BY-CA

%description fastfetch
Fastfetch configuration for chronOS

%files fastfetch
%attr(0755,root,root) %{_datadir}/ublue-os/fastfetch.jsonc

%package plymouth
Summary:        Plymouth customization for chronOS
License:        CC-BY-CA

%description plymouth
Plymouth logo customization for chronOS

%files plymouth
%attr(0755,root,root) %{_datadir}/plymouth
