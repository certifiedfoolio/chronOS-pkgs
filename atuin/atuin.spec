%global debug_package %{nil}

Name:           atuin
Version:        18.4.0
Release:        1%{?dist}
Summary:        Magical shell history

License:        MIT
URL:            https://github.com/ellie/atuin
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pkgconfig(protobuf) protobuf-compiler

%description
Atuin replaces your existing shell history with a SQLite database, and
records additional context for your commands. Additionally, it provides
optional and fully encrypted synchronisation of your history between
machines, via an Atuin server.

%prep
%autosetup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y
source ~/.cargo/env
cargo +stable build --release
for SHELL in "bash" "fish" "zsh"; do
    target/release/%{name} gen-completions --shell $SHELL -o .
done

%check
source ~/.cargo/env
cargo +stable test --workspace --all-features --lib

%install
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
%autochangelog
