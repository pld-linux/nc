Summary:	Versatile network test and debugging tool
Summary(es.UTF-8):   Herramienta de prueba e depuración para servicios de red
Summary(pl.UTF-8):   Proste narzędzie do testowania sieci
Summary(pt_BR.UTF-8):   Ferramenta de teste e depuração para serviços de rede
Name:		nc
Version:	1.10
Release:	19
License:	Public Domain
Group:		Networking/Admin
Source0:	http://www.atstake.com/research/tools/network_utilities/%{name}110.tgz
# Source0-md5:	402632f2fe01c169ff19a0ad6e9d608c
Source1:	http://www.openbsd.org/src/usr.bin/%{name}.1
Patch0:		%{name}-arm.patch
Patch1:		%{name}-v6-20000918.patch.gz
Patch2:		%{name}-proto.patch
Patch3:		%{name}-halfclose.patch
Patch4:		%{name}-timeout.patch
URL:		http://www.atstake.com/research/tools/network_utilities/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es.UTF-8
NetCat es un cliente de red mínimo. Puede ser usado para crear
conexiones TCP a puertos arbitrarios y puede simular conexiones
sobre UDP. También puede oír puertos.

%description -l pl.UTF-8
Netcat to proste uniksowe narzędzie, które odbiera i wysyła dane
poprzez połączenia sieciowe protokołami TCP lub UDP. Jest
zaprojektowane jako wiarygodny "back-end", który może być używany
bezpośrednio albo sterowany przez inne programy i skrypty.
Jednocześnie może pomóc w wykrywaniu usterek w sieci albo poznawaniu
jej od środka, ponieważ może stworzyć prawie dowolny rodzaj
połączenia, jaki może być potrzebny, i ma wbudowanych kilka ciekawych
funkcji. Netcat - albo "nc", jak się nazywa właściwy program, powinien
był być dostarczany już dawno temu jako kolejne tajemnicze, ale
standardowe uniksowe narzędzie.

%description -l pt_BR.UTF-8
O NetCat é um cliente de rede mínimo. Pode ser usado para criar
conexões TCP para portas arbitrárias e pode simular conexões sobre
UDP. Também pode receber conexões.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  README Changelog scripts data
%attr(755,root,root) %{_bindir}/nc
%{_mandir}/man1/*
