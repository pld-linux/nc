Summary:	Versatile network test and debugging tool
Summary(pl):	Proste narzêdzie do testowania sieci
Name:		nc
Version:	1.10
Release:	9
Copyright:	None, see README
Group:		Networking/Admin
Group(pl):	Sieciowe/Administacyjne
Source0:	ftp://ftp.avian.org/src/hacks/%{name}110.tgz
Source1:	http://www.openbsd.org/src/usr.bin/nc.1
Patch:		nc-arm.patch
Icon:		netcat.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	netcat

%description 
Netcat is a simple Unix utility which reads and writes data across network
connections, using TCP or UDP protocol. It is designed to be a reliable
"back-end" tool that can be used directly or easily driven by other programs
and scripts. At the same time, it is a feature-rich network debugging and
exploration tool, since it can create almost any kind of connection you
would need and has several interesting built-in capabilities. Netcat, or
"nc" as the actual program is named, should have been supplied long ago as
another one of those cryptic but standard Unix tools.

%description -l pl
Netcat to proste uniksowe narzêdzie, które odbiera i wysy³a dane poprzez
po³±czenia sieciowe protoko³ami TCP lub UDP. Jest zaprojektowane jako
wiarygodny "back-end", który mo¿e byæ u¿ywany bezpo¶rednio albo sterowany
przez inne programy i skrypty. Jednocze¶nie mo¿e pomóc w wykrywaniu usterek
w sieci albo poznawaniu jej od ¶rodka, poniewa¿ mo¿e stworzyæ prawie
dowolny rodzaj po³±czenia, jaki mo¿e byæ potrzebny, i ma wbudowanych kilka
ciekawych funkcji. Netcat - albo "nc", jak siê nazywa w³a¶ciwy program,
powinien by³ byæ dostarczany ju¿ dawno temu jako kolejne tajemnicze, ale
standardowe uniksowe narzêdzie.

%prep
%setup -c -n nc -q
%patch -p1

%build
# 'make linux' works too, but builds a static binary. 
make generic DFLAGS="-DTELNET -DGAPING_SECURITY_HOLE" CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install nc $RPM_BUILD_ROOT%{_bindir}/nc
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README Changelog data/* \
	$RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz scripts data
%attr(755,root,root) %{_bindir}/nc
%{_mandir}/man1/*
