#define _disable_ld_no_undefined 1

%define name kicad-library
%define version 1.0
%define release %mkrel 4

Summary:  Library for kicad (creation of electronic schematic diagrams)
Name:     %{name}
Version:  %{version}
Release:  %{release}
Source0:  %{name}-%{version}.tar.bz2
License:  GPL
Group:    Sciences/Computer science
Url:      https://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake

%description
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-library is a set of library needed by kicad.

%prep
%setup -q -n %{name} 

%build
export LC_ALL=C
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%make

%install
rm -rf %{buildroot}
make -C build DESTDIR=%buildroot install

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%endif

%if %mdkversion < 200900
%postun
%endif

%files
%defattr(-,root,root)
%{_datadir}/kicad/library
%{_datadir}/kicad/modules


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-4mdv2011.0
+ Revision: 619966
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2010.0
+ Revision: 429687
- rebuild

* Tue Aug 26 2008 trem <trem@mandriva.org> 1.0-2mdv2009.0
+ Revision: 276412
- bump new release because last release was eaten by the bs

* Thu Aug 21 2008 trem <trem@mandriva.org> 1.0-1mdv2009.0
+ Revision: 274947
- import kicad-library


