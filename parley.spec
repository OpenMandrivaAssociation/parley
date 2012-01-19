Name: parley
Summary: KDE Vocabulary training application
Version: 4.8.0
Release: 1
Group: Graphical desktop/KDE
License: GPLv2 GFDL LGPLv2+ LGPLv2
URL: http://edu.kde.org/parley
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libkdeedu-devel >= %{version}
Requires: libkdeedu = %{version}
Requires: python-mwclient

%description
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%files
%doc COPYING COPYING.DOC AUTHORS
%_kde_bindir/parley
%_kde_appsdir/parley
%_kde_iconsdir/*/*/apps/parley*
%_kde_datadir/applications/kde4/parley.desktop
%_kde_services/plasma-dataengine-parley.desktop
%_kde_services/plasma_parley.desktop
%_kde_datadir/config.kcfg/parley.kcfg
%_kde_datadir/config.kcfg/languagesettings.kcfg
%_kde_datadir/config.kcfg/documentsettings.kcfg
%_kde_datadir/config/parley.knsrc
%_kde_libdir/kde4/plasma_applet_parley.so
%_kde_libdir/kde4/plasma_engine_parley.so
%_kde_appsdir/desktoptheme/default/widgets/parley_plasma_card.svg
%_kde_datadir/config/parley-themes.knsrc
%_kde_docdir/HTML/*/parley

#----------------------------------------------------------------------

%prep
%setup -q 
%apply_patches


%build
%cmake_kde4 
%make

%install
%makeinstall_std -C build

