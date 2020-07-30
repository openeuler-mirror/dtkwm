Name:           dtkwm
Version:        2.0.12
Release:        2
Summary:        Deepin graphical user interface library
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkwm
Source0:        %{name}_%{version}.orig.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-static
BuildRequires:  dtkcore2-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
DtkWm is used to handle double screen for deepin desktop development.
This package contains the shared libraries.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_libdir}/libdtkwm.so.2*

%files devel
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_dtkwm.pri
%dir %{_libdir}/cmake/DtkWm/
%{_libdir}/cmake/DtkWm/DtkWmConfig.cmake
%{_libdir}/pkgconfig/dtkwm.pc
%{_libdir}/libdtkwm.so

%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 2.0.12-2
- Package init
