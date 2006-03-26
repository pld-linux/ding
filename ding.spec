Summary:	A Dictionary Lookup program
Name:		ding
Version:	1.4
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://wftp.tu-chemnitz.de/pub/Local/urz/ding/%{name}-%{version}.tar.gz
# Source0-md5:	d278c1026fe0f784ed7984721088dd23
URL:		http://www-user.tu-chemnitz.de/~fri/ding/
Requires:	/usr/bin/wish
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ding (DIctionary Nice Grep) is a tool to lookup words in dictionaries.
It uses tools like agrep, dict, ispell/aspell etc. It contains a program
(ding) written in Tcl/Tk and a German - English dictionary with about
180,000 translations.

%description -l de
Ding (DIctionary Nice Grep) ist ein Programm zur Suche in Wörterbüchern.
Es benutzt zur Suche Werkzeuge wie agrep bzw. egrep, dict, ispell/aspell.
Es basiert auf Tcl/Tk und enthält ein Deutsch- Englisches Wörterbuch mit
ca. 180.000 Einträgen.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/dict,%{_pixmapsdir},%{_desktopdir},%{_mandir}/man1}
install ding $RPM_BUILD_ROOT%{_bindir}
cp -a de-en.txt $RPM_BUILD_ROOT%{_datadir}/dict/de-en.txt
cp -a ding.png $RPM_BUILD_ROOT%{_pixmapsdir}/ding.png
cp -a ding.desktop $RPM_BUILD_ROOT%{_desktopdir}/ding.desktop
cp -a ding.1 $RPM_BUILD_ROOT%{_mandir}/man1/ding.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES COPYING
%attr(755,root,root) %{_bindir}/ding
%{_datadir}/dict/de-en.txt
%{_mandir}/man1/*
%{_desktopdir}/ding.desktop
%{_pixmapsdir}/ding.png
