%define debug_package %{nil}
%define datadir /usr/share

Name:           grimblast
Version:        0.1
Release:        %autorelease
Summary:        Hyprland screenshot utility

License:        MIT
Source0:        https://github.com/koeqaife/contrib/archive/refs/tags/v%{version}.tar.gz

BuildRequires:   hyprland hyprshot hyprcursor hypridle hyprlang hyprpaper hyprpicker hyprlock hyprutils hyprwayland-scanner xdg-dbus-proxy xdg-desktop-portal xdg-desktop-portal-gtk xdg-desktop-portal-hyprland xdg-user-dirs xdg-utils libxdg-basedir python-pyxdg swww gtk3 gtk4 adw-gtk3-theme libdbusmenu-gtk3 python-pip python-pillow nm-connection-editor network-manager-applet NetworkManager gnome-bluetooth wl-gammarelay-rs bluez bluez-libs wl-clipboard libadwaita swappy nwg-look pavucontrol brightnessctl man-pages gvfs xarchiver zip ImageMagick blueman fastfetch gum python-pywayland dbus libdrm mesa fwupd bun pipewire wireplumber udiskie lm_sensors gnome-system-monitor playerctl google-noto-sans-fonts fontawesome-fonts open-sans-fonts google-roboto-fonts lshw material-icons-fonts fontconfig rubygem-sass cpio meson cmake python-materialyoucolor gtksourceview3 gtksourceviewmm cairomm gtkmm3.0 tinyxml2 python-requests python-numpy

%description
Hyprland screenshot utility using grim and slurp

%build

%install
ls -lah

%files

%changelog
%autochangelog