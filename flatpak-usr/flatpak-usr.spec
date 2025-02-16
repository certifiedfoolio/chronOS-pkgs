%global debug_package %{nil}

Name:           flatpak-usr
Version:        1.0.0
Release:        1%{?dist}
Summary:        Flatpak user setup

License:        CC-BY-CA
URL:            https://github.com/certifiedfoolio/chronOS-pkgs
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

%description
Setup Flatpak user repositories and remove flatpak system repositories

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
     %{buildroot}%{_sysconfdir}/systemd/
mv services %{buildroot}%{_sysconfdir}/systemd/system

%files
%{_sysconfdir}/systemd/system/*