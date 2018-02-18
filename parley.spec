%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Vocabulary training application
Name:		parley
Version:	 17.12.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://edu.kde.org/parley
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
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
BuildRequires:	cmake(LibKEduVocDocument)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngineWidgets)
%description
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%files -f %{name}.lang
%doc COPYING AUTHORS
%{_sysconfdir}/xdg/parley*.knsrc
%{_bindir}/parley
%{_datadir}/applications/org.kde.parley.desktop
%{_datadir}/metainfo/org.kde.parley.appdata.xml
%{_datadir}/config.kcfg/documentsettings.kcfg
%{_datadir}/config.kcfg/languagesettings.kcfg
%{_datadir}/config.kcfg/parley.kcfg
%{_iconsdir}/*/*/apps/*.*[gz]
%{_iconsdir}/*/*/actions/*.*[gz]
%{_datadir}/kxmlgui5/parley
%{_datadir}/parley

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
