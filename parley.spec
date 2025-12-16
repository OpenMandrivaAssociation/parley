#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 70 ] && echo -n un; echo -n stable)
Summary:	KDE Vocabulary training application
Name:		parley
Version:	25.12.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://edu.kde.org/parley
%if 0%{?git:1}
Source0:	https://invent.kde.org/education/parley/-/archive/%{gitbranch}/parley-%{gitbranchd}.tar.bz2#/parley-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/parley-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	%mklibname -d KEduVocDocument6
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	translate-shell
Requires:	translate-shell

%rename plasma6-parley

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Parley is a program to help you memorize things.

Parley supports many language specific features but can be used for other
learning tasks just as well. It uses the spaced repetition learning method,
also known as flash cards.

%files -f parley.lang
%doc AUTHORS
%{_datadir}/knsrcfiles/parley*.knsrc
%{_bindir}/parley
%{_datadir}/applications/org.kde.parley.desktop
%{_datadir}/metainfo/org.kde.parley.appdata.xml
%{_datadir}/config.kcfg/documentsettings.kcfg
%{_datadir}/config.kcfg/languagesettings.kcfg
%{_datadir}/config.kcfg/parley.kcfg
%{_iconsdir}/*/*/apps/*.*[gz]
%{_iconsdir}/*/*/actions/*.*[gz]
%{_datadir}/parley
