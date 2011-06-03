#define _disable_ld_no_undefined 1

# For library,
# See http://iut-tice.ujf-grenoble.fr/cao/how_to_download_sources.txt
# bzr branch lp:~kicad-lib-committers/kicad/library
#
# You can get the date by querying:
# $ bzr log -r-1 --line library/
# 109: xtony 2010-12-08 Add various modules.
#
# $ bzr export --format=tbz2 --root=kicad-library kicad-library-bzr$(bzr revno library/).tar.bz2 library/

%define name kicad-library
%define date 20101208
%define revision 109
%define version 1.1.%{date}.bzr%{revision}
%define release %mkrel 1

Name:     	%{name}
Summary:  	Library for kicad (creation of electronic schematic diagrams)
Version:  	%{version}
Release:  	%{release}
Source0:  	%{name}-bzr%{revision}.tar.bz2
License:  	GPL
Group:    	Sciences/Computer science
Url:      	http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildArch:	noarch

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
