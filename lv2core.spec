Summary:	LV2 (LADSPA Version 2) Audio Plugin Standard
Summary(pl.UTF-8):	LV2 (LADSPA Version 2) - standard wtyczek dźwiękowych
Name:		lv2core
Version:	4.0
Release:	1
License:	LGPL v2.1+ (lv2 header file), BSD-like (lv2 data files)
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	5097d964f3559a1ecec2d2fc822ef53a
URL:		http://lv2plug.in/
# g++ only checked for, not used
BuildRequires:	libstdc++-devel
BuildRequires:	python
BuildRequires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 is a standard for plugins and matching host applications,
primarily targeted at audio processing and generation.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many applications have outgrown. Compared to LADSPA, all
plugin data is moved from the code to a separate data file, and the
code has been made as generic as possible. As a result, LV2 can be
independently extended (retaining compatibility wherever possible),
and virtually any feasible plugin features can be implemented in an
LV2 plugin.

%description -l pl.UTF-8
LV2 to standard dla wtyczek i aplikacji z nich korzystających. Jest
przeznaczony przede wszystkim do przetwarzania i generowania dźwięku.

LV2 to następca LADSPA, powstały w celu zniesienia ograniczeń
LADSPA, które napotkało wiele aplikacji. W porówaniu do LADSPA
wszystkie dane zostały przeniesione z kodu do osobnego pliku danych,
a kod stał się jak najbardziej ogólny. W efekcie LV2 może być
niezależnie rozszerzany (zachowując kompatybilność na ile to możliwe),
a we wtyczce LV2 mogą być zaimplementowane praktycznie wszystkie
wykonalne funkcje wtyczek.

%package devel
Summary:	LV2 API header file
Summary(pl.UTF-8):	Plik nagłówkowy API LV2
License:	LGPL v2.1+
Group:		Development/Libraries
# doesn't require base

%description devel
LV2 API header file.

%description devel -l pl.UTF-8
Plik nagłówkowy API LV2.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}
./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

# what for?
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lv2/lv2core.lv2/lv2.h

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/lv2config
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/lv2core.lv2
%{_libdir}/lv2/lv2core.lv2/lv2.ttl
%{_libdir}/lv2/lv2core.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_includedir}/lv2.h
%{_pkgconfigdir}/lv2core.pc
