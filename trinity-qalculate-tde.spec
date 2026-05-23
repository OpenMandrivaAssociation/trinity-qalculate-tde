%bcond clang 1

# TDE variables
%define tde_pkg qalculate-tde
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	Powerful and easy to use desktop calculator - TDE version
Group:		Applications/Multimedia
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/utilities/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:  pkgconfig(libqalculate)

BuildRequires:  pkgconfig(cln)


BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Qalculate! is small and simple to use but with much power and versatility
underneath.  Features include customizable functions, units, arbitrary
precision, plotting, and a graphical interface that uses a one-line
fault-tolerant expression entry (although it supports optional traditional
buttons).

This package contains the TDE user interface of qalculate.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%find_lang qalculate_tde


%files -f qalculate_tde.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/qalculate-tde
%{tde_prefix}/share/apps/qalculate_tde/
%{tde_prefix}/share/applications/tde/qalculate_tde.desktop
%{tde_prefix}/share/doc/tde/HTML/en/qalculate_tde/
%{tde_prefix}/share/icons/hicolor/*/apps/qalculate_tde.png
%{tde_prefix}/share/icons/hicolor/*/actions/qalculate_convert.png
%{tde_prefix}/share/man/man1/qalculate-tde.1*

