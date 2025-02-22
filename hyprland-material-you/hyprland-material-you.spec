%define debug_package %{nil}
%define datadir /usr/share

Name:           hyprland-material-you
Version:        0.1
Release:        %autorelease
Summary:        Material you configuration for agsv1

License:        MIT
URL:            https://github.com/koeqaife/hyprland-material-you
Source0:        https://github.com/koeqaife/hyprland-material-you/archive/refs/heads/main.zip

Requires:   aylurs-gtk-shell hyprland hyprshot hyprcursor hypridle hyprlang hyprpaper hyprpicker hyprlock hyprutils hyprwayland-scanner xdg-dbus-proxy xdg-desktop-portal xdg-desktop-portal-gtk xdg-desktop-portal-hyprland xdg-user-dirs xdg-utils libxdg-basedir python-pyxdg swww gtk3 gtk4 adw-gtk3-theme libdbusmenu-gtk3 python-pip python-pillow nm-connection-editor network-manager-applet NetworkManager gnome-bluetooth wl-gammarelay-rs bluez bluez-libs wl-clipboard libadwaita swappy nwg-look pavucontrol brightnessctl man-pages gvfs xarchiver zip ImageMagick blueman fastfetch gum python-pywayland dbus libdrm mesa fwupd bun pipewire wireplumber udiskie lm_sensors gnome-system-monitor playerctl google-noto-sans-fonts fontawesome-fonts open-sans-fonts google-roboto-fonts lshw material-icons-fonts fontconfig rubygem-sass cpio meson cmake python-materialyoucolor gtksourceview3 gtksourceviewmm cairomm gtkmm3.0 tinyxml2 python-requests python-numpy

%description
Material you configuration for agsv1, from https://github.com/koeqaife/hyprland-material-you

%prep
%autosetup -n %{name}-main

%install
mkdir -p %{buildroot}%{datadir}/hyprmaterial
sed -i 's/python/python3/g' ags/scripts/wayland-idle-inhibitor.py
sed -i '1i #!/usr/bin/bash' scripts/filemanager.sh
sed -i '1i #!/usr/bin/bash' scripts/update_timer.sh
rm ags/types
cp -r scripts %{buildroot}%{datadir}/hyprmaterial/
cp -r ags %{buildroot}%{datadir}/hyprmaterial/

%posttrans
ln -s /usr/share/com.github.Aylur.ags/types /usr/share/hyprmaterial/ags/types

%files
%{datadir}/hyprmaterial/*

%changelog
%autochangelog