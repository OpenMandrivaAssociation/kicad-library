#define _disable_ld_no_undefined 1

%define name kicad-library
%define version 1.0
%define release %mkrel 1

Summary:  Library for kicad (creation of electronic schematic diagrams)
Name:     %{name}
Version:  %{version}
Release:  %{release}
Source0:  %{name}-%{version}.tar.bz2
License:  GPL
Group:    Sciences/Computer science
Url:      http://www.lis.inpg.fr/realise_au_lis/kicad/
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
