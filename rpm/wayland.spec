Name:       wayland

# >> macros
# << macros

Summary:    wayland compositor
Version:    1.1.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://wayland.freedesktop.org/
Source0:    wayland-%{version}.tar.xz
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

# >> setup
# << setup

%build
# >> build pre
# << build pre

%reconfigure --disable-static \
    --disable-documentation

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post

# << install post

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
%{_datadir}/wayland/wayland.xml

# << files devel
