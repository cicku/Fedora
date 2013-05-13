%global oname lfcxml

Name:              liblfc-xml
Version:           1.0.27
Release:           1%{?dist}
Summary:           Lemke Foundation Classes XML extension
License:           GPLv2

URL:               http://www.lemke-it.com/litexec?request=publfcxml&user=&lang=en
Source0:           http://www.lemke-it.com/%{oname}-%{version}.tar.gz
BuildRequires:     liblfc-devel

%description
This C++ library provides an API for XML document handling. Similar to the 
JDOM Java interface, a XML document can be parsed, traced and generated by 
the provided methods.

%package           devel
Summary:	   Development files for %{name}
Requires:	   %{name} = %{version}-%{release}

%description	   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}
%configure --disable-static

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.a' -exec rm -f {} ';'
ln -s /usr/lib/liblfcxml.so.1 %{buildroot}/usr/lib/liblfcxml.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%doc COPYING
%{_includedir}/lfc/*
/usr/lib/*.so

%changelog
* Mon May 06 2013 Christopher Meng <rpm@cicku.me> - 1.0.27-1
- Initial Package.