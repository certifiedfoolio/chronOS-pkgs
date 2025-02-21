%define debug_package %{nil}
%define datadir /usr/share

Name:           grimblast
Version:        0.1
Release:        %autorelease
Summary:        Hyprland screenshot utility

License:        MIT
Source0:        https://github.com/koeqaife/contrib/archive/refs/tags/v%{version}.tar.gz

BuildRequires:   hyprland hyprshot hyprcursor hypridle hyprlang hyprpaper hyprpicker hyprlock hyprutils hyprwayland-scanner xdg-dbus-proxy xdg-desktop-portal xdg-desktop-portal-gtk xdg-desktop-portal-hyprland xdg-user-dirs xdg-utils libxdg-basedir python-pyxdg swww gtk3 gtk4 adw-gtk3 adw-gtk-theme libdbusmenu-gtk3 python-pip python-pillow sddm sddm-theme-corners-git nm-connection-editor network-manager-applet networkmanager gnome-bluetooth-3.0 wl-gammarelay-rs bluez bluez-libs bluez-utils cliphist wl-clipboard libadwaita swappy nwg-look pavucontrol polkit-gnome brightnessctl man-pages gvfs xarchiver zip imagemagick blueman fastfetch bibata-cursor-theme gum python-pywayland dbus libdrm mesa fwupd bun-bin pipewire wireplumber udiskie lm_sensors gnome-system-monitor playerctl ttf-meslo-nerd ttf-google-sans ttf-font-awesome ttf-opensans ttf-roboto lshw ttf-material-symbols-variable-git fontconfig dart-sass ttf-meslo-nerd-font-powerlevel10k cpio meson cmake python-materialyoucolor gtksourceview3 gtksourceviewmm cairomm gtkmm3 tinyxml2 python-requests python-numpy

%description
Hyprland screenshot utility using grim and slurp

%build

%install
ls -lah

%files

%changelog
%autochangelog