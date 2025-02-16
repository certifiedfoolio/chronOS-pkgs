%global debug_package %{nil}

Name:           sysconf
Version:        1.0.0
Release:        1%{?dist}
Summary:        chronOS config

License:        CC-BY-CA
URL:           https://github.com/certifiedfoolio/chronOS-pkgs
VCS:           {{{ git_dir_vcs }}}
Source:        {{{ git_dir_pack }}}

%description
System configuration for chronOS

%prep
{{{ git_dir_setup_macro }}}

%install
mkdir -p -m0755 \
    %{buildroot}%{_bindir}
    %{buildroot}%{_sysconfdir}
    %{buildroot}%{_datadir}
mv firstsetup %{buildroot}%{_sysconfdir}/
mv skel %{buildroot}%{_sysconfdir}/
mv applications %{buildroot}%{_datadir}/
mv bin %{buildroot}/usr

%files
%{_datadir}/applications/*
%{_sysconfdir}/skel/*
%{_sysconfdir}/firstsetup/*
/usr/bin/*