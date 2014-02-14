Name:       wayland

Summary:    wayland compositor
Version:    1.2.1
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://wayland.freedesktop.org/
Source0:    wayland-%{version}.tar.xz
#already applied upstream
#Patch0:     0001-client-Add-acquire-fd-API-to-avoid-requiring-a-polli.patch
Patch1:     0002-wl_map_reserve_new-Work-around-client-thread-unsafet.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(libffi)
BuildRequires:  expat-devel

%description
wayland is another window System

%package devel
Summary:    wayland devel library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Provides:   wayland-server
Provides:   wayland-client

%description devel
devel files for wayland

%prep
%setup -q -n %{name}-%{version}/wayland

# 0001-client-Add-acquire-fd-API-to-avoid-requiring-a-polli.patch
#%patch0 -p1
# 0002-wl_map_reserve_new-Work-around-client-thread-unsafet.patch
%patch1 -p1

%build
%reconfigure --disable-static \
    --disable-documentation

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%{_bindir}/wayland-scanner
#%{_sysconfdir}/udev/*.rules
%{_libdir}/libwayland-client.so.0*
%{_libdir}/libwayland-cursor.so.0*
%{_libdir}/libwayland-server.so.0*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/wayland-client.h
%{_includedir}/wayland-client-protocol.h
%{_includedir}/wayland-cursor.h
%{_includedir}/wayland-egl.h
%{_includedir}/wayland-server.h
%{_includedir}/wayland-server-protocol.h
%{_includedir}/wayland-util.h
%{_includedir}/wayland-version.h
%{_libdir}/pkgconfig/wayland-client.pc
%{_libdir}/pkgconfig/wayland-cursor.pc
%{_libdir}/pkgconfig/wayland-server.pc
%{_datadir}/pkgconfig/wayland-scanner.pc
%{_libdir}/libwayland-client.so
%{_libdir}/libwayland-cursor.so
%{_libdir}/libwayland-server.so
%{_datadir}/aclocal/wayland-scanner.m4
%{_datadir}/wayland/wayland-scanner.mk

# << files devel
