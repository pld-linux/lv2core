Summary:	Audio Plugin Standard
Summary(pl.UTF-8):	Audio Plugin Standard
Name:		lv2core
Version:	3.0
Release:	1
License:	LGPL v2.1+ or BSD-like (see COPYING)
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	382f7d96ff0374c0c495336e1c8bb999
URL:		http://lv2plug.in
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

%package devel
Summary:	Header files for lv2core library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki lv2core
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for lv2core library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki lv2core.

%prep
%setup -q
sed -i 's|/lib|/%{_lib}|' autowaf.py

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}/
./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/lv2core.lv2
%{_libdir}/lv2/lv2core.lv2/lv2.ttl
%{_libdir}/lv2/lv2core.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_includedir}/lv2.h
%{_pkgconfigdir}/lv2core.pc
