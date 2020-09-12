Name:       wayland

Summary:    wayland compositor
Version:    1.18.0
Release:    1
License:    MIT
URL:        http://wayland.freedesktop.org/
Source0:    wayland-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  meson
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  expat-devel

%description
wayland is another window System

%package devel
Summary:    wayland devel library
Requires:   %{name} = %{version}-%{release}
Provides:   wayland-server
Provides:   wayland-client

%description devel
devel files for wayland

%package egl
Summary:    wayland-egl library
Requires:   %{name} = %{version}-%{release}
Obsoletes:  mesa-llvmpipe-libwayland-egl

%description egl
wayland-egl library

%package egl-devel
Summary:    wayland-egl devel library
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-egl = %{version}-%{release}
Obsoletes:  mesa-llvmpipe-libwayland-egl-devel

%description egl-devel
wayland-egl devel files

%prep
%autosetup -n %{name}-%{version}/wayland

%build
%meson -Ddocumentation=false

%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post egl -p /sbin/ldconfig
%postun egl -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/wayland-scanner
#%{_sysconfdir}/udev/*.rules
%{_libdir}/libwayland-client.so.0*
%{_libdir}/libwayland-cursor.so.0*
%{_libdir}/libwayland-server.so.0*

%files devel
%defattr(-,root,root,-)
%{_includedir}/wayland-client.h
%{_includedir}/wayland-client-core.h
%{_includedir}/wayland-client-protocol.h
%{_includedir}/wayland-cursor.h
%{_includedir}/wayland-egl.h
%{_includedir}/wayland-egl-core.h
%{_includedir}/wayland-server.h
%{_includedir}/wayland-server-core.h
%{_includedir}/wayland-server-protocol.h
%{_includedir}/wayland-util.h
%{_includedir}/wayland-version.h
%{_libdir}/pkgconfig/wayland-client.pc
%{_libdir}/pkgconfig/wayland-cursor.pc
%{_libdir}/pkgconfig/wayland-server.pc
%{_libdir}/pkgconfig/wayland-scanner.pc
%{_libdir}/libwayland-client.so
%{_libdir}/libwayland-cursor.so
%{_libdir}/libwayland-server.so
%{_datadir}/aclocal/wayland-scanner.m4
%{_datadir}/wayland/wayland-scanner.mk
%{_datadir}/wayland/wayland.xml
%{_datadir}/wayland/wayland.dtd

%files egl
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libwayland-egl.so.1*

%files egl-devel
%defattr(-,root,root,-)
%{_includedir}/wayland-egl-backend.h
%{_libdir}/pkgconfig/wayland-egl.pc
%{_libdir}/pkgconfig/wayland-egl-backend.pc
%{_libdir}/libwayland-egl.so
