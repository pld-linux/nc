Summary:	Versatile network test and debugging tool
Summary(pl):	Proste narzêdzie do testowania sieci
Name:		nc
Version:	1.10
Release:	15
License:	None, see README
Group:		Networking/Admin
Group(de):	Netzwerkwesen/Administration
Group(pl):	Sieciowe/Administacyjne
Source0:	http://www.l0pht.com/users/10pht/%{name}110.tgz
Source1:	http://www.openbsd.org/src/usr.bin/%{name}.1
Patch0:		%{name}-arm.patch
Patch1:		%{name}-v6-20000918.patch.gz
Patch2:		%{name}-proto.patch
Patch3:		%{name}-halfclose.patch
Patch4:		%{name}-timeout.patch
URL:		http://www.l0pht.com/~weld/netcat/
Icon:		netcat.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	netcat

%description 
Netcat is a simple Unix utility which reads and writes data across
network connections, using TCP or UDP protocol. It is designed to be a
reliable "back-end" tool that can be used directly or easily driven by
other programs and scripts. At the same time, it is a feature-rich
network debugging and exploration tool, since it can create almost any
kind of connection you would need and has several interesting built-in
capabilities. Netcat, or "nc" as the actual program is named, should
have been supplied long ago as another one of those cryptic but
standard Unix tools.

%description -l pl
Netcat to proste uniksowe narzêdzie, które odbiera i wysy³a dane
poprzez po³±czenia sieciowe protoko³ami TCP lub UDP. Jest
zaprojektowane jako wiarygodny "back-end", który mo¿e byæ u¿ywany
bezpo¶rednio albo sterowany przez inne programy i skrypty.
Jednocze¶nie mo¿e pomóc w wykrywaniu usterek w sieci albo poznawaniu
jej od ¶rodka, poniewa¿ mo¿e stworzyæ prawie dowolny rodzaj
po³±czenia, jaki mo¿e byæ potrzebny, i ma wbudowanych kilka ciekawych
funkcji. Netcat - albo "nc", jak siê nazywa w³a¶ciwy program, powinien
by³ byæ dostarczany ju¿ dawno temu jako kolejne tajemnicze, ale
standardowe uniksowe narzêdzie.

%prep
%setup -c -n nc -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# 'make linux' works too, but builds a static binary. 
%{__make} generic \
	DFLAGS="-DINET6 -DTELNET -DGAPING_SECURITY_HOLE" \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install nc $RPM_BUILD_ROOT%{_bindir}/nc
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README Changelog data/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz scripts data
%attr(755,root,root) %{_bindir}/nc
%{_mandir}/man1/*
