%global debug_package %{nil}

Name:           sysconf
Version:        1.0.0
Release:        1%{?dist}
Summary:        chronOS config

License:        CC-BY-CA
URL:            https://github.com/certifiedfoolio/chronOS-pkgs
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

Provides: sudo
Obsoletes: sudo

%description
System configuration for chronOS

%prep
{{{ git_dir_setup_macro }}}

%install
chmod +x bin/* -R
mv bin %{buildroot}/
mv etc %{buildroot}/
mv usr %{buildroot}/

%files
%{_datadir}/applications/*
%{_sysconfdir}/skel/*
%{_sysconfdir}/skel/.local/*
%{_sysconfdir}/firstsetup/*
/bin/*