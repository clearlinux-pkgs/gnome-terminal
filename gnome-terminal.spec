#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-terminal
Version  : 3.26.0
Release  : 8
URL      : https://download.gnome.org/sources/gnome-terminal/3.26/gnome-terminal-3.26.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-terminal/3.26/gnome-terminal-3.26.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: gnome-terminal-bin
Requires: gnome-terminal-config
Requires: gnome-terminal-lib
Requires: gnome-terminal-data
Requires: gnome-terminal-doc
Requires: gnome-terminal-locales
BuildRequires : dconf-dev
BuildRequires : desktop-file-utils
BuildRequires : gettext
BuildRequires : gnome-shell
BuildRequires : intltool
BuildRequires : itstool
BuildRequires : libxml2-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gconf-2.0)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gsettings-desktop-schemas)
BuildRequires : pkgconfig(libnautilus-extension)
BuildRequires : pkgconfig(libpcre2-8)
BuildRequires : pkgconfig(uuid)
BuildRequires : vte-dev

%description
No detailed description available

%package bin
Summary: bin components for the gnome-terminal package.
Group: Binaries
Requires: gnome-terminal-data
Requires: gnome-terminal-config

%description bin
bin components for the gnome-terminal package.


%package config
Summary: config components for the gnome-terminal package.
Group: Default

%description config
config components for the gnome-terminal package.


%package data
Summary: data components for the gnome-terminal package.
Group: Data

%description data
data components for the gnome-terminal package.


%package doc
Summary: doc components for the gnome-terminal package.
Group: Documentation

%description doc
doc components for the gnome-terminal package.


%package lib
Summary: lib components for the gnome-terminal package.
Group: Libraries
Requires: gnome-terminal-data
Requires: gnome-terminal-config

%description lib
lib components for the gnome-terminal package.


%package locales
Summary: locales components for the gnome-terminal package.
Group: Default

%description locales
locales components for the gnome-terminal package.


%prep
%setup -q -n gnome-terminal-3.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505318314
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-common -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-gterminal \
--disable-migration
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1505318314
rm -rf %{buildroot}
%make_install
%find_lang gnome-terminal

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-terminal
/usr/libexec/gnome-terminal-server

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-terminal-server.service

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Terminal.desktop
/usr/share/dbus-1/services/org.gnome.Terminal.service
/usr/share/glib-2.0/schemas/org.gnome.Terminal.gschema.xml
/usr/share/gnome-shell/search-providers/gnome-terminal-search-provider.ini
/usr/share/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml
/usr/share/metainfo/org.gnome.Terminal.appdata.xml

%files doc
%defattr(-,root,root,-)
/usr/share/help/C/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/C/gnome-terminal/app-colors.page
/usr/share/help/C/gnome-terminal/app-cursor.page
/usr/share/help/C/gnome-terminal/app-fonts.page
/usr/share/help/C/gnome-terminal/app-fullscreen.page
/usr/share/help/C/gnome-terminal/app-terminal-sizes.page
/usr/share/help/C/gnome-terminal/app-zoom.page
/usr/share/help/C/gnome-terminal/figures/gnome-terminal-icon.png
/usr/share/help/C/gnome-terminal/figures/gnome-terminal.png
/usr/share/help/C/gnome-terminal/gs-execute-commands.page
/usr/share/help/C/gnome-terminal/gs-tabs.page
/usr/share/help/C/gnome-terminal/index.page
/usr/share/help/C/gnome-terminal/introduction.page
/usr/share/help/C/gnome-terminal/legal.xml
/usr/share/help/C/gnome-terminal/overview.page
/usr/share/help/C/gnome-terminal/pref-bell.page
/usr/share/help/C/gnome-terminal/pref-custom-command.page
/usr/share/help/C/gnome-terminal/pref-custom-exit.page
/usr/share/help/C/gnome-terminal/pref-encoding.page
/usr/share/help/C/gnome-terminal/pref-keyboard-access.page
/usr/share/help/C/gnome-terminal/pref-menubar.page
/usr/share/help/C/gnome-terminal/pref-profile-char-width.page
/usr/share/help/C/gnome-terminal/pref-profile-encoding.page
/usr/share/help/C/gnome-terminal/pref-profiles.page
/usr/share/help/C/gnome-terminal/pref-scrolling.page
/usr/share/help/C/gnome-terminal/pref-tab-window.page
/usr/share/help/C/gnome-terminal/pref-user-input.page
/usr/share/help/C/gnome-terminal/pref.page
/usr/share/help/C/gnome-terminal/prob-reset.page
/usr/share/help/C/gnome-terminal/profile.page
/usr/share/help/C/gnome-terminal/txt-copy-paste.page
/usr/share/help/C/gnome-terminal/txt-links.page
/usr/share/help/C/gnome-terminal/txt-search.page
/usr/share/help/C/gnome-terminal/txt-select-text.page
/usr/share/help/ca/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/ca/gnome-terminal/app-colors.page
/usr/share/help/ca/gnome-terminal/app-cursor.page
/usr/share/help/ca/gnome-terminal/app-fonts.page
/usr/share/help/ca/gnome-terminal/app-fullscreen.page
/usr/share/help/ca/gnome-terminal/app-terminal-sizes.page
/usr/share/help/ca/gnome-terminal/app-zoom.page
/usr/share/help/ca/gnome-terminal/gs-execute-commands.page
/usr/share/help/ca/gnome-terminal/gs-tabs.page
/usr/share/help/ca/gnome-terminal/index.page
/usr/share/help/ca/gnome-terminal/introduction.page
/usr/share/help/ca/gnome-terminal/legal.xml
/usr/share/help/ca/gnome-terminal/overview.page
/usr/share/help/ca/gnome-terminal/pref-bell.page
/usr/share/help/ca/gnome-terminal/pref-custom-command.page
/usr/share/help/ca/gnome-terminal/pref-custom-exit.page
/usr/share/help/ca/gnome-terminal/pref-encoding.page
/usr/share/help/ca/gnome-terminal/pref-keyboard-access.page
/usr/share/help/ca/gnome-terminal/pref-menubar.page
/usr/share/help/ca/gnome-terminal/pref-profile-char-width.page
/usr/share/help/ca/gnome-terminal/pref-profile-encoding.page
/usr/share/help/ca/gnome-terminal/pref-profiles.page
/usr/share/help/ca/gnome-terminal/pref-scrolling.page
/usr/share/help/ca/gnome-terminal/pref-tab-window.page
/usr/share/help/ca/gnome-terminal/pref-user-input.page
/usr/share/help/ca/gnome-terminal/pref.page
/usr/share/help/ca/gnome-terminal/prob-reset.page
/usr/share/help/ca/gnome-terminal/profile.page
/usr/share/help/ca/gnome-terminal/txt-copy-paste.page
/usr/share/help/ca/gnome-terminal/txt-links.page
/usr/share/help/ca/gnome-terminal/txt-search.page
/usr/share/help/ca/gnome-terminal/txt-select-text.page
/usr/share/help/cs/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/cs/gnome-terminal/app-colors.page
/usr/share/help/cs/gnome-terminal/app-cursor.page
/usr/share/help/cs/gnome-terminal/app-fonts.page
/usr/share/help/cs/gnome-terminal/app-fullscreen.page
/usr/share/help/cs/gnome-terminal/app-terminal-sizes.page
/usr/share/help/cs/gnome-terminal/app-zoom.page
/usr/share/help/cs/gnome-terminal/gs-execute-commands.page
/usr/share/help/cs/gnome-terminal/gs-tabs.page
/usr/share/help/cs/gnome-terminal/index.page
/usr/share/help/cs/gnome-terminal/introduction.page
/usr/share/help/cs/gnome-terminal/legal.xml
/usr/share/help/cs/gnome-terminal/overview.page
/usr/share/help/cs/gnome-terminal/pref-bell.page
/usr/share/help/cs/gnome-terminal/pref-custom-command.page
/usr/share/help/cs/gnome-terminal/pref-custom-exit.page
/usr/share/help/cs/gnome-terminal/pref-encoding.page
/usr/share/help/cs/gnome-terminal/pref-keyboard-access.page
/usr/share/help/cs/gnome-terminal/pref-menubar.page
/usr/share/help/cs/gnome-terminal/pref-profile-char-width.page
/usr/share/help/cs/gnome-terminal/pref-profile-encoding.page
/usr/share/help/cs/gnome-terminal/pref-profiles.page
/usr/share/help/cs/gnome-terminal/pref-scrolling.page
/usr/share/help/cs/gnome-terminal/pref-tab-window.page
/usr/share/help/cs/gnome-terminal/pref-user-input.page
/usr/share/help/cs/gnome-terminal/pref.page
/usr/share/help/cs/gnome-terminal/prob-reset.page
/usr/share/help/cs/gnome-terminal/profile.page
/usr/share/help/cs/gnome-terminal/txt-copy-paste.page
/usr/share/help/cs/gnome-terminal/txt-links.page
/usr/share/help/cs/gnome-terminal/txt-search.page
/usr/share/help/cs/gnome-terminal/txt-select-text.page
/usr/share/help/de/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/de/gnome-terminal/app-colors.page
/usr/share/help/de/gnome-terminal/app-cursor.page
/usr/share/help/de/gnome-terminal/app-fonts.page
/usr/share/help/de/gnome-terminal/app-fullscreen.page
/usr/share/help/de/gnome-terminal/app-terminal-sizes.page
/usr/share/help/de/gnome-terminal/app-zoom.page
/usr/share/help/de/gnome-terminal/gs-execute-commands.page
/usr/share/help/de/gnome-terminal/gs-tabs.page
/usr/share/help/de/gnome-terminal/index.page
/usr/share/help/de/gnome-terminal/introduction.page
/usr/share/help/de/gnome-terminal/legal.xml
/usr/share/help/de/gnome-terminal/overview.page
/usr/share/help/de/gnome-terminal/pref-bell.page
/usr/share/help/de/gnome-terminal/pref-custom-command.page
/usr/share/help/de/gnome-terminal/pref-custom-exit.page
/usr/share/help/de/gnome-terminal/pref-encoding.page
/usr/share/help/de/gnome-terminal/pref-keyboard-access.page
/usr/share/help/de/gnome-terminal/pref-menubar.page
/usr/share/help/de/gnome-terminal/pref-profile-char-width.page
/usr/share/help/de/gnome-terminal/pref-profile-encoding.page
/usr/share/help/de/gnome-terminal/pref-profiles.page
/usr/share/help/de/gnome-terminal/pref-scrolling.page
/usr/share/help/de/gnome-terminal/pref-tab-window.page
/usr/share/help/de/gnome-terminal/pref-user-input.page
/usr/share/help/de/gnome-terminal/pref.page
/usr/share/help/de/gnome-terminal/prob-reset.page
/usr/share/help/de/gnome-terminal/profile.page
/usr/share/help/de/gnome-terminal/txt-copy-paste.page
/usr/share/help/de/gnome-terminal/txt-links.page
/usr/share/help/de/gnome-terminal/txt-search.page
/usr/share/help/de/gnome-terminal/txt-select-text.page
/usr/share/help/el/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/el/gnome-terminal/app-colors.page
/usr/share/help/el/gnome-terminal/app-cursor.page
/usr/share/help/el/gnome-terminal/app-fonts.page
/usr/share/help/el/gnome-terminal/app-fullscreen.page
/usr/share/help/el/gnome-terminal/app-terminal-sizes.page
/usr/share/help/el/gnome-terminal/app-zoom.page
/usr/share/help/el/gnome-terminal/gs-execute-commands.page
/usr/share/help/el/gnome-terminal/gs-tabs.page
/usr/share/help/el/gnome-terminal/index.page
/usr/share/help/el/gnome-terminal/introduction.page
/usr/share/help/el/gnome-terminal/legal.xml
/usr/share/help/el/gnome-terminal/overview.page
/usr/share/help/el/gnome-terminal/pref-bell.page
/usr/share/help/el/gnome-terminal/pref-custom-command.page
/usr/share/help/el/gnome-terminal/pref-custom-exit.page
/usr/share/help/el/gnome-terminal/pref-encoding.page
/usr/share/help/el/gnome-terminal/pref-keyboard-access.page
/usr/share/help/el/gnome-terminal/pref-menubar.page
/usr/share/help/el/gnome-terminal/pref-profile-char-width.page
/usr/share/help/el/gnome-terminal/pref-profile-encoding.page
/usr/share/help/el/gnome-terminal/pref-profiles.page
/usr/share/help/el/gnome-terminal/pref-scrolling.page
/usr/share/help/el/gnome-terminal/pref-tab-window.page
/usr/share/help/el/gnome-terminal/pref-user-input.page
/usr/share/help/el/gnome-terminal/pref.page
/usr/share/help/el/gnome-terminal/prob-reset.page
/usr/share/help/el/gnome-terminal/profile.page
/usr/share/help/el/gnome-terminal/txt-copy-paste.page
/usr/share/help/el/gnome-terminal/txt-links.page
/usr/share/help/el/gnome-terminal/txt-search.page
/usr/share/help/el/gnome-terminal/txt-select-text.page
/usr/share/help/es/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/es/gnome-terminal/app-colors.page
/usr/share/help/es/gnome-terminal/app-cursor.page
/usr/share/help/es/gnome-terminal/app-fonts.page
/usr/share/help/es/gnome-terminal/app-fullscreen.page
/usr/share/help/es/gnome-terminal/app-terminal-sizes.page
/usr/share/help/es/gnome-terminal/app-zoom.page
/usr/share/help/es/gnome-terminal/gs-execute-commands.page
/usr/share/help/es/gnome-terminal/gs-tabs.page
/usr/share/help/es/gnome-terminal/index.page
/usr/share/help/es/gnome-terminal/introduction.page
/usr/share/help/es/gnome-terminal/legal.xml
/usr/share/help/es/gnome-terminal/overview.page
/usr/share/help/es/gnome-terminal/pref-bell.page
/usr/share/help/es/gnome-terminal/pref-custom-command.page
/usr/share/help/es/gnome-terminal/pref-custom-exit.page
/usr/share/help/es/gnome-terminal/pref-encoding.page
/usr/share/help/es/gnome-terminal/pref-keyboard-access.page
/usr/share/help/es/gnome-terminal/pref-menubar.page
/usr/share/help/es/gnome-terminal/pref-profile-char-width.page
/usr/share/help/es/gnome-terminal/pref-profile-encoding.page
/usr/share/help/es/gnome-terminal/pref-profiles.page
/usr/share/help/es/gnome-terminal/pref-scrolling.page
/usr/share/help/es/gnome-terminal/pref-tab-window.page
/usr/share/help/es/gnome-terminal/pref-user-input.page
/usr/share/help/es/gnome-terminal/pref.page
/usr/share/help/es/gnome-terminal/prob-reset.page
/usr/share/help/es/gnome-terminal/profile.page
/usr/share/help/es/gnome-terminal/txt-copy-paste.page
/usr/share/help/es/gnome-terminal/txt-links.page
/usr/share/help/es/gnome-terminal/txt-search.page
/usr/share/help/es/gnome-terminal/txt-select-text.page
/usr/share/help/fi/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/fi/gnome-terminal/app-colors.page
/usr/share/help/fi/gnome-terminal/app-cursor.page
/usr/share/help/fi/gnome-terminal/app-fonts.page
/usr/share/help/fi/gnome-terminal/app-fullscreen.page
/usr/share/help/fi/gnome-terminal/app-terminal-sizes.page
/usr/share/help/fi/gnome-terminal/app-zoom.page
/usr/share/help/fi/gnome-terminal/gs-execute-commands.page
/usr/share/help/fi/gnome-terminal/gs-tabs.page
/usr/share/help/fi/gnome-terminal/index.page
/usr/share/help/fi/gnome-terminal/introduction.page
/usr/share/help/fi/gnome-terminal/legal.xml
/usr/share/help/fi/gnome-terminal/overview.page
/usr/share/help/fi/gnome-terminal/pref-bell.page
/usr/share/help/fi/gnome-terminal/pref-custom-command.page
/usr/share/help/fi/gnome-terminal/pref-custom-exit.page
/usr/share/help/fi/gnome-terminal/pref-encoding.page
/usr/share/help/fi/gnome-terminal/pref-keyboard-access.page
/usr/share/help/fi/gnome-terminal/pref-menubar.page
/usr/share/help/fi/gnome-terminal/pref-profile-char-width.page
/usr/share/help/fi/gnome-terminal/pref-profile-encoding.page
/usr/share/help/fi/gnome-terminal/pref-profiles.page
/usr/share/help/fi/gnome-terminal/pref-scrolling.page
/usr/share/help/fi/gnome-terminal/pref-tab-window.page
/usr/share/help/fi/gnome-terminal/pref-user-input.page
/usr/share/help/fi/gnome-terminal/pref.page
/usr/share/help/fi/gnome-terminal/prob-reset.page
/usr/share/help/fi/gnome-terminal/profile.page
/usr/share/help/fi/gnome-terminal/txt-copy-paste.page
/usr/share/help/fi/gnome-terminal/txt-links.page
/usr/share/help/fi/gnome-terminal/txt-search.page
/usr/share/help/fi/gnome-terminal/txt-select-text.page
/usr/share/help/fr/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/fr/gnome-terminal/app-colors.page
/usr/share/help/fr/gnome-terminal/app-cursor.page
/usr/share/help/fr/gnome-terminal/app-fonts.page
/usr/share/help/fr/gnome-terminal/app-fullscreen.page
/usr/share/help/fr/gnome-terminal/app-terminal-sizes.page
/usr/share/help/fr/gnome-terminal/app-zoom.page
/usr/share/help/fr/gnome-terminal/gs-execute-commands.page
/usr/share/help/fr/gnome-terminal/gs-tabs.page
/usr/share/help/fr/gnome-terminal/index.page
/usr/share/help/fr/gnome-terminal/introduction.page
/usr/share/help/fr/gnome-terminal/legal.xml
/usr/share/help/fr/gnome-terminal/overview.page
/usr/share/help/fr/gnome-terminal/pref-bell.page
/usr/share/help/fr/gnome-terminal/pref-custom-command.page
/usr/share/help/fr/gnome-terminal/pref-custom-exit.page
/usr/share/help/fr/gnome-terminal/pref-encoding.page
/usr/share/help/fr/gnome-terminal/pref-keyboard-access.page
/usr/share/help/fr/gnome-terminal/pref-menubar.page
/usr/share/help/fr/gnome-terminal/pref-profile-char-width.page
/usr/share/help/fr/gnome-terminal/pref-profile-encoding.page
/usr/share/help/fr/gnome-terminal/pref-profiles.page
/usr/share/help/fr/gnome-terminal/pref-scrolling.page
/usr/share/help/fr/gnome-terminal/pref-tab-window.page
/usr/share/help/fr/gnome-terminal/pref-user-input.page
/usr/share/help/fr/gnome-terminal/pref.page
/usr/share/help/fr/gnome-terminal/prob-reset.page
/usr/share/help/fr/gnome-terminal/profile.page
/usr/share/help/fr/gnome-terminal/txt-copy-paste.page
/usr/share/help/fr/gnome-terminal/txt-links.page
/usr/share/help/fr/gnome-terminal/txt-search.page
/usr/share/help/fr/gnome-terminal/txt-select-text.page
/usr/share/help/gl/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/gl/gnome-terminal/app-colors.page
/usr/share/help/gl/gnome-terminal/app-cursor.page
/usr/share/help/gl/gnome-terminal/app-fonts.page
/usr/share/help/gl/gnome-terminal/app-fullscreen.page
/usr/share/help/gl/gnome-terminal/app-terminal-sizes.page
/usr/share/help/gl/gnome-terminal/app-zoom.page
/usr/share/help/gl/gnome-terminal/gs-execute-commands.page
/usr/share/help/gl/gnome-terminal/gs-tabs.page
/usr/share/help/gl/gnome-terminal/index.page
/usr/share/help/gl/gnome-terminal/introduction.page
/usr/share/help/gl/gnome-terminal/legal.xml
/usr/share/help/gl/gnome-terminal/overview.page
/usr/share/help/gl/gnome-terminal/pref-bell.page
/usr/share/help/gl/gnome-terminal/pref-custom-command.page
/usr/share/help/gl/gnome-terminal/pref-custom-exit.page
/usr/share/help/gl/gnome-terminal/pref-encoding.page
/usr/share/help/gl/gnome-terminal/pref-keyboard-access.page
/usr/share/help/gl/gnome-terminal/pref-menubar.page
/usr/share/help/gl/gnome-terminal/pref-profile-char-width.page
/usr/share/help/gl/gnome-terminal/pref-profile-encoding.page
/usr/share/help/gl/gnome-terminal/pref-profiles.page
/usr/share/help/gl/gnome-terminal/pref-scrolling.page
/usr/share/help/gl/gnome-terminal/pref-tab-window.page
/usr/share/help/gl/gnome-terminal/pref-user-input.page
/usr/share/help/gl/gnome-terminal/pref.page
/usr/share/help/gl/gnome-terminal/prob-reset.page
/usr/share/help/gl/gnome-terminal/profile.page
/usr/share/help/gl/gnome-terminal/txt-copy-paste.page
/usr/share/help/gl/gnome-terminal/txt-links.page
/usr/share/help/gl/gnome-terminal/txt-search.page
/usr/share/help/gl/gnome-terminal/txt-select-text.page
/usr/share/help/hu/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/hu/gnome-terminal/app-colors.page
/usr/share/help/hu/gnome-terminal/app-cursor.page
/usr/share/help/hu/gnome-terminal/app-fonts.page
/usr/share/help/hu/gnome-terminal/app-fullscreen.page
/usr/share/help/hu/gnome-terminal/app-terminal-sizes.page
/usr/share/help/hu/gnome-terminal/app-zoom.page
/usr/share/help/hu/gnome-terminal/figures/gnome-terminal.png
/usr/share/help/hu/gnome-terminal/gs-execute-commands.page
/usr/share/help/hu/gnome-terminal/gs-tabs.page
/usr/share/help/hu/gnome-terminal/index.page
/usr/share/help/hu/gnome-terminal/introduction.page
/usr/share/help/hu/gnome-terminal/legal.xml
/usr/share/help/hu/gnome-terminal/overview.page
/usr/share/help/hu/gnome-terminal/pref-bell.page
/usr/share/help/hu/gnome-terminal/pref-custom-command.page
/usr/share/help/hu/gnome-terminal/pref-custom-exit.page
/usr/share/help/hu/gnome-terminal/pref-encoding.page
/usr/share/help/hu/gnome-terminal/pref-keyboard-access.page
/usr/share/help/hu/gnome-terminal/pref-menubar.page
/usr/share/help/hu/gnome-terminal/pref-profile-char-width.page
/usr/share/help/hu/gnome-terminal/pref-profile-encoding.page
/usr/share/help/hu/gnome-terminal/pref-profiles.page
/usr/share/help/hu/gnome-terminal/pref-scrolling.page
/usr/share/help/hu/gnome-terminal/pref-tab-window.page
/usr/share/help/hu/gnome-terminal/pref-user-input.page
/usr/share/help/hu/gnome-terminal/pref.page
/usr/share/help/hu/gnome-terminal/prob-reset.page
/usr/share/help/hu/gnome-terminal/profile.page
/usr/share/help/hu/gnome-terminal/txt-copy-paste.page
/usr/share/help/hu/gnome-terminal/txt-links.page
/usr/share/help/hu/gnome-terminal/txt-search.page
/usr/share/help/hu/gnome-terminal/txt-select-text.page
/usr/share/help/ko/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/ko/gnome-terminal/app-colors.page
/usr/share/help/ko/gnome-terminal/app-cursor.page
/usr/share/help/ko/gnome-terminal/app-fonts.page
/usr/share/help/ko/gnome-terminal/app-fullscreen.page
/usr/share/help/ko/gnome-terminal/app-terminal-sizes.page
/usr/share/help/ko/gnome-terminal/app-zoom.page
/usr/share/help/ko/gnome-terminal/figures/gnome-terminal.png
/usr/share/help/ko/gnome-terminal/gs-execute-commands.page
/usr/share/help/ko/gnome-terminal/gs-tabs.page
/usr/share/help/ko/gnome-terminal/index.page
/usr/share/help/ko/gnome-terminal/introduction.page
/usr/share/help/ko/gnome-terminal/legal.xml
/usr/share/help/ko/gnome-terminal/overview.page
/usr/share/help/ko/gnome-terminal/pref-bell.page
/usr/share/help/ko/gnome-terminal/pref-custom-command.page
/usr/share/help/ko/gnome-terminal/pref-custom-exit.page
/usr/share/help/ko/gnome-terminal/pref-encoding.page
/usr/share/help/ko/gnome-terminal/pref-keyboard-access.page
/usr/share/help/ko/gnome-terminal/pref-menubar.page
/usr/share/help/ko/gnome-terminal/pref-profile-char-width.page
/usr/share/help/ko/gnome-terminal/pref-profile-encoding.page
/usr/share/help/ko/gnome-terminal/pref-profiles.page
/usr/share/help/ko/gnome-terminal/pref-scrolling.page
/usr/share/help/ko/gnome-terminal/pref-tab-window.page
/usr/share/help/ko/gnome-terminal/pref-user-input.page
/usr/share/help/ko/gnome-terminal/pref.page
/usr/share/help/ko/gnome-terminal/prob-reset.page
/usr/share/help/ko/gnome-terminal/profile.page
/usr/share/help/ko/gnome-terminal/txt-copy-paste.page
/usr/share/help/ko/gnome-terminal/txt-links.page
/usr/share/help/ko/gnome-terminal/txt-search.page
/usr/share/help/ko/gnome-terminal/txt-select-text.page
/usr/share/help/pt_BR/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/pt_BR/gnome-terminal/app-colors.page
/usr/share/help/pt_BR/gnome-terminal/app-cursor.page
/usr/share/help/pt_BR/gnome-terminal/app-fonts.page
/usr/share/help/pt_BR/gnome-terminal/app-fullscreen.page
/usr/share/help/pt_BR/gnome-terminal/app-terminal-sizes.page
/usr/share/help/pt_BR/gnome-terminal/app-zoom.page
/usr/share/help/pt_BR/gnome-terminal/figures/gnome-terminal.png
/usr/share/help/pt_BR/gnome-terminal/gs-execute-commands.page
/usr/share/help/pt_BR/gnome-terminal/gs-tabs.page
/usr/share/help/pt_BR/gnome-terminal/index.page
/usr/share/help/pt_BR/gnome-terminal/introduction.page
/usr/share/help/pt_BR/gnome-terminal/legal.xml
/usr/share/help/pt_BR/gnome-terminal/overview.page
/usr/share/help/pt_BR/gnome-terminal/pref-bell.page
/usr/share/help/pt_BR/gnome-terminal/pref-custom-command.page
/usr/share/help/pt_BR/gnome-terminal/pref-custom-exit.page
/usr/share/help/pt_BR/gnome-terminal/pref-encoding.page
/usr/share/help/pt_BR/gnome-terminal/pref-keyboard-access.page
/usr/share/help/pt_BR/gnome-terminal/pref-menubar.page
/usr/share/help/pt_BR/gnome-terminal/pref-profile-char-width.page
/usr/share/help/pt_BR/gnome-terminal/pref-profile-encoding.page
/usr/share/help/pt_BR/gnome-terminal/pref-profiles.page
/usr/share/help/pt_BR/gnome-terminal/pref-scrolling.page
/usr/share/help/pt_BR/gnome-terminal/pref-tab-window.page
/usr/share/help/pt_BR/gnome-terminal/pref-user-input.page
/usr/share/help/pt_BR/gnome-terminal/pref.page
/usr/share/help/pt_BR/gnome-terminal/prob-reset.page
/usr/share/help/pt_BR/gnome-terminal/profile.page
/usr/share/help/pt_BR/gnome-terminal/txt-copy-paste.page
/usr/share/help/pt_BR/gnome-terminal/txt-links.page
/usr/share/help/pt_BR/gnome-terminal/txt-search.page
/usr/share/help/pt_BR/gnome-terminal/txt-select-text.page
/usr/share/help/ru/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/ru/gnome-terminal/app-colors.page
/usr/share/help/ru/gnome-terminal/app-cursor.page
/usr/share/help/ru/gnome-terminal/app-fonts.page
/usr/share/help/ru/gnome-terminal/app-fullscreen.page
/usr/share/help/ru/gnome-terminal/app-terminal-sizes.page
/usr/share/help/ru/gnome-terminal/app-zoom.page
/usr/share/help/ru/gnome-terminal/figures/gnome-terminal.png
/usr/share/help/ru/gnome-terminal/gs-execute-commands.page
/usr/share/help/ru/gnome-terminal/gs-tabs.page
/usr/share/help/ru/gnome-terminal/index.page
/usr/share/help/ru/gnome-terminal/introduction.page
/usr/share/help/ru/gnome-terminal/legal.xml
/usr/share/help/ru/gnome-terminal/overview.page
/usr/share/help/ru/gnome-terminal/pref-bell.page
/usr/share/help/ru/gnome-terminal/pref-custom-command.page
/usr/share/help/ru/gnome-terminal/pref-custom-exit.page
/usr/share/help/ru/gnome-terminal/pref-encoding.page
/usr/share/help/ru/gnome-terminal/pref-keyboard-access.page
/usr/share/help/ru/gnome-terminal/pref-menubar.page
/usr/share/help/ru/gnome-terminal/pref-profile-char-width.page
/usr/share/help/ru/gnome-terminal/pref-profile-encoding.page
/usr/share/help/ru/gnome-terminal/pref-profiles.page
/usr/share/help/ru/gnome-terminal/pref-scrolling.page
/usr/share/help/ru/gnome-terminal/pref-tab-window.page
/usr/share/help/ru/gnome-terminal/pref-user-input.page
/usr/share/help/ru/gnome-terminal/pref.page
/usr/share/help/ru/gnome-terminal/prob-reset.page
/usr/share/help/ru/gnome-terminal/profile.page
/usr/share/help/ru/gnome-terminal/txt-copy-paste.page
/usr/share/help/ru/gnome-terminal/txt-links.page
/usr/share/help/ru/gnome-terminal/txt-search.page
/usr/share/help/ru/gnome-terminal/txt-select-text.page
/usr/share/help/sv/gnome-terminal/adv-keyboard-shortcuts.page
/usr/share/help/sv/gnome-terminal/app-colors.page
/usr/share/help/sv/gnome-terminal/app-cursor.page
/usr/share/help/sv/gnome-terminal/app-fonts.page
/usr/share/help/sv/gnome-terminal/app-fullscreen.page
/usr/share/help/sv/gnome-terminal/app-terminal-sizes.page
/usr/share/help/sv/gnome-terminal/app-zoom.page
/usr/share/help/sv/gnome-terminal/gs-execute-commands.page
/usr/share/help/sv/gnome-terminal/gs-tabs.page
/usr/share/help/sv/gnome-terminal/index.page
/usr/share/help/sv/gnome-terminal/introduction.page
/usr/share/help/sv/gnome-terminal/legal.xml
/usr/share/help/sv/gnome-terminal/overview.page
/usr/share/help/sv/gnome-terminal/pref-bell.page
/usr/share/help/sv/gnome-terminal/pref-custom-command.page
/usr/share/help/sv/gnome-terminal/pref-custom-exit.page
/usr/share/help/sv/gnome-terminal/pref-encoding.page
/usr/share/help/sv/gnome-terminal/pref-keyboard-access.page
/usr/share/help/sv/gnome-terminal/pref-menubar.page
/usr/share/help/sv/gnome-terminal/pref-profile-char-width.page
/usr/share/help/sv/gnome-terminal/pref-profile-encoding.page
/usr/share/help/sv/gnome-terminal/pref-profiles.page
/usr/share/help/sv/gnome-terminal/pref-scrolling.page
/usr/share/help/sv/gnome-terminal/pref-tab-window.page
/usr/share/help/sv/gnome-terminal/pref-user-input.page
/usr/share/help/sv/gnome-terminal/pref.page
/usr/share/help/sv/gnome-terminal/prob-reset.page
/usr/share/help/sv/gnome-terminal/profile.page
/usr/share/help/sv/gnome-terminal/txt-copy-paste.page
/usr/share/help/sv/gnome-terminal/txt-links.page
/usr/share/help/sv/gnome-terminal/txt-search.page
/usr/share/help/sv/gnome-terminal/txt-select-text.page

%files lib
%defattr(-,root,root,-)
/usr/lib64/nautilus/extensions-3.0/libterminal-nautilus.so

%files locales -f gnome-terminal.lang
%defattr(-,root,root,-)

