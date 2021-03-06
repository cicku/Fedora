%global __requires_exclude perl\\(Monitorix\\)|perl\\(HTTPServer\\)
%global __provides_exclude perl\\(

Name:              monitorix
Version:           3.2.1
Release:           1%{?dist}
Summary:           A free, open source, lightweight system monitoring tool
License:           GPLv2+
URL:               http://www.monitorix.org
Source0:           http://www.monitorix.org/%{name}-%{version}.tar.gz

BuildArch:         noarch
BuildRequires:     perl
BuildRequires:     systemd
Requires:          logrotate
Requires:          perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:          perl(CGI)
Requires:          perl(Config::General)
Requires:          perl(DBD::mysql)
Requires:          perl(DBI)
Requires:          perl(HTTP::Server::Simple::CGI)
Requires:          perl(XML::Simple)
Requires(post):    systemd
Requires(preun):   systemd
Requires(postun):  systemd

%description
Monitorix is a free, open source, lightweight system monitoring tool designed
to monitor as many services and system resources as possible. It has been
created to be used under production Linux/UNIX servers, but due to its
simplicity and small size may also be used on embedded devices as well.

%prep
%setup -q

sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{name}
sed -i 's|#!/usr/bin/env perl|#!/usr/bin/perl|' %{name}.cgi

%build

%install
install -p -D -m 644 docs/%{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf
install -p -D -m 755 %{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}/usr/lib/%{name}
install -p -D -m 644 lib/*.pm %{buildroot}/usr/lib/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -D -m 644 logo_top.png %{buildroot}%{_datadir}/%{name}
install -p -D -m 644 logo_bot.png %{buildroot}%{_datadir}/%{name}
install -p -D -m 644 %{name}ico.png %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}/imgs
mkdir -p %{buildroot}%{_datadir}/%{name}/cgi
install -p -D -m 755 %{name}.cgi %{buildroot}%{_datadir}/%{name}/cgi
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/reports
install -p -D -m 644 reports/*.html %{buildroot}%{_localstatedir}/lib/%{name}/reports
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/usage
mkdir -p %{buildroot}%{_mandir}/man5
mkdir -p %{buildroot}%{_mandir}/man8
install -p -D -m 644 man/man5/%{name}.conf.5 %{buildroot}%{_mandir}/man5
install -p -D -m 644 man/man8/%{name}.8 %{buildroot}%{_mandir}/man8
install -p -D -m 644 docs/%{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -p -D -m 644 docs/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%post
%systemd_post %{buildroot}%{_unitdir}/%{name}.service

%preun
%systemd_preun %{buildroot}%{_unitdir}/%{name}.service

%postun
%systemd_postun_with_restart %{buildroot}%{_unitdir}/%{name}.service

%files
%doc Changes COPYING README README.nginx docs/%{name}-alert.sh docs/%{name}-apache.conf docs/%{name}-lighttpd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/cgi
%dir %{_localstatedir}/lib/%{name}/
%dir %{_localstatedir}/lib/%{name}/reports
%{_localstatedir}/lib/%{name}/reports/*.html
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*
%{_unitdir}/%{name}.service
%{_bindir}/%{name}
/usr/lib/%{name}/
%{_datadir}/%{name}/logo_top.png
%{_datadir}/%{name}/logo_bot.png
%{_datadir}/%{name}/%{name}ico.png
%{_datadir}/%{name}/cgi/%{name}.cgi
%attr(755,nobody,nobody) %{_datadir}/%{name}/imgs
%attr(755,root,root) %{_localstatedir}/lib/%{name}/usage

%changelog
* Wed Jun 05 2013 Christopher Meng <rpm@cicku.me> - 3.2.1-1
- New release.

* Tue May 21 2013 Christopher Meng <rpm@cicku.me> - 3.2.0-2
- Fixes.

* Tue May 14 2013 Christopher Meng <rpm@cicku.me> - 3.2.0-1
- New release.

* Tue Apr 30 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-4
- libdir fixed.

* Sat Apr 06 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-3
- Errors fixed.

* Tue Apr 02 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-2
- Fixed review bugs(BZ#947071)

* Mon Apr 01 2013 Christopher Meng <rpm@cicku.me> - 3.1.0-1
- Initial Package.
