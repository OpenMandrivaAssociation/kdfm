%define oname kdfm-code 

%define git 20210108

Name:           kdfm
Version:        0
Release:        0.git.1
Summary:        File Manager
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://kdfm.sourceforge.io
Source:         %{oname}.tar.xz

BuildRequires:  cmake
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)

Recommends:     styleproject
Recommends:     kio-extras5

%description
kdfm is a filemanager written in C++/Qt. kdfm offers a Cover Flow navigation add-on.

%prep
%autosetup -n %{oname}
sed -i 's/\(Icon=\).*/\1system-file-manager/;s/\(GenericName=\).*/\1File Browser/' src/%{name}.desktop
sed -i "s/\(Exec=\).*/\1env QT_STYLE_OVERRIDE=Styleproject %{name}/" src/%{name}.desktop

%build
%cmake
%make_build

%install
%make_install -C build

%files
%license src/COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/kxmlgui5/%{name}
%{_datadir}/kxmlgui5/%{name}/%{name}ui.rc
