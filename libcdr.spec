%define name libcdr
%define version 0.1.7
%define RELEASE 1
%define release     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Name: %{name}
Summary: Library for importing and converting Corel Draw Documents
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.gz
Group: System Environment/Libraries
URL: http://libcdr.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: librevenge-devel >= 0.9.0, gcc-c++, libstdc++-devel, pkgconfig >= 0.9.0
License: MPL-2.0
Prefix: %{prefix}

%description
libcdr is a library for reading and converting CDR images

%package tools
Requires: libcdr
Summary: Tools to convert CDR images into other formats
Group: Applications/Publishing

%description tools
Tools to convert CDR images into other formats.
Currently supported: raw svg

%package devel
Requires: %{name} >= %{version}
Requires: librevenge-devel >= 0.9.0
Summary: Files for developing with libcdr.
Group: Development/Libraries

%description devel
Includes and definitions for developing with libcdr.

%if %{!?_without_docs:1}%{?_without_docs:0}
%package docs
Requires: %{name} >= %{version}
BuildRequires: doxygen
Summary: Documentation of libcdr API
Group: Development/Documentation

%description docs
Documentation of libcdr API for developing with libcdr
%endif

%prep
%__rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{version}

%build
%configure --prefix=%{_prefix} --libdir=%{_libdir} \
        %{?_with_debug:--enable-debug}  \

%__make

%install
umask 022

%__make DESTDIR=$RPM_BUILD_ROOT install
%__rm -rf $RPM_BUILD_ROOT/%{_libdir}/libcdr*.la

%clean
%__rm -rf $RPM_BUILD_ROOT $RPM_BUILD_DIR/file.list.%{name}

%files
%defattr(644,root,root,755)
%{_libdir}/libcdr*.so.*
%doc ChangeLog README COPYING AUTHORS

%files tools
%defattr(755,root,root,755)
%{_bindir}/cdr2*
%{_bindir}/cmx2*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libcdr*.so
%{_libdir}/pkgconfig/libcdr*.pc
%{_includedir}/libcdr-0.1/libcdr

%if %{!?_without_docs:1}%{?_without_docs:0}
%files docs
%{_datadir}/*
%endif

%changelog
* Fri Apr 20 2007 Fridrich Strba <fridrich.strba@bluewin.ch>
- Add documentation packaging
- Make doc and stream optional

* Tue Jan 27 2004 Fridrich Strba <fridrich.strba@bluewin.ch>
- Create rpm spec according to the rpm spec of libwpD
- of Rui M. Seabra
