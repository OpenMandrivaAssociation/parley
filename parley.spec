Summary:	KDE Vocabulary training application
Name:		parley
Version:	15.04.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/parley
Source0:	http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdeedu-devel >= %{version}
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Kross)
BuildRequires:	cmake(KF5KrossUi)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Notifications)

%description
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%files
%doc COPYING COPYING.DOC AUTHORS
%doc %{_kde_docdir}/HTML/*/parley
%{_kde_applicationsdir}/parley.desktop
%{_kde_appsdir}/parley
%{_kde_appsdir}/desktoptheme/default/widgets/parley_plasma_card.svg
%{_kde_bindir}/parley
%{_kde_configdir}/parley.knsrc
%{_kde_configdir}/parley-themes.knsrc
%{_kde_datadir}/appdata/parley.appdata.xml
%{_kde_datadir}/config.kcfg/parley.kcfg
%{_kde_datadir}/config.kcfg/languagesettings.kcfg
%{_kde_datadir}/config.kcfg/documentsettings.kcfg
%{_kde_iconsdir}/*/*/apps/parley*
%{_kde_libdir}/kde4/plasma_applet_parley.so
%{_kde_libdir}/kde4/plasma_engine_parley.so
%{_kde_services}/plasma-dataengine-parley.desktop
%{_kde_services}/plasma_parley.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
