Summary:	Monitoring plugin for cellular modems
Name:		xfce4-cellmodem-plugin
Version:	0.0.5
Release:	10
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cellmodem-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-cellmodem-plugin/%{name}-%{version}.tar.bz2
Patch0:		xfce4-cellmodem-plugin-0.0.5-rosa-linkage.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	pkgconfig(libusb)
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(libxfcegui4-1.0)

# required for patch0
BuildRequires:	xfce4-dev-tools

%description
The cellmodem plugin is a monitoring plugin for cellular modems.

%prep
%setup -q
%patch0 -p1

%build
# required for patch0
xdt-autogen

%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_libdir}/xfce4/panel-plugins/xfce4-cellmodem-plugin
%{_datadir}/xfce4/panel-plugins/cellmodem.desktop


%changelog
* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.5-9mdv2010.1
+ Revision: 543419
- rebuild for mdv 2010.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.0.5-8mdv2010.0
+ Revision: 445978
- rebuild

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.5-7mdv2009.1
+ Revision: 360390
- use _disable_ld_as_needed to make it build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.0.5-3mdv2008.1
+ Revision: 171184
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.5-2mdv2008.1
+ Revision: 110101
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- use upstream name

* Fri Jun 01 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.0.5-1mdv2008.0
+ Revision: 33524
- Import xfce-cellmodem-plugin

