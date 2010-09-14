Summary:	A Dictionary Lookup program
Summary(pl.UTF-8):	Program do wyszukiwania słów w słownikach
Name:		ding
Version:	1.7
Release:	0.1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://wftp.tu-chemnitz.de/pub/Local/urz/ding/%{name}-%{version}.tar.gz
# Source0-md5:	f021c0cb21105cf0ccd38330c2598ed1
Patch0:		%{name}-desktop.patch
URL:		http://www-user.tu-chemnitz.de/~fri/ding/
Requires:	/usr/bin/wish
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ding (DIctionary Nice Grep) is a tool to lookup words in dictionaries.
It uses tools like agrep, dict, ispell/aspell etc. It contains a
program (ding) written in Tcl/Tk and a German - English dictionary
with about 180,000 translations.

%description -l de.UTF-8
Ding (DIctionary Nice Grep) ist ein Programm zur Suche in
Wörterbüchern. Es benutzt zur Suche Werkzeuge wie agrep bzw. egrep,
dict, ispell/aspell. Es basiert auf Tcl/Tk und enthält ein Deutsch-
Englisches Wörterbuch mit ca. 180.000 Einträgen.

%description -l pl.UTF-8
Ding (DIctionary Nice Grep) to narzędzie do wyszukiwania słów w
słownikach. Używa narzędzi takich jak agrep, dict, ispell/aspell itp.
Zawiera program (ding) napisany w języku Tcl/Tk i słownik
niemiecko-angielski zawierający około 180000 tłumaczeń.

%prep
%setup -q
%patch0 -p1

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
%{_mandir}/man1/ding.1*
%{_desktopdir}/ding.desktop
%{_pixmapsdir}/ding.png
