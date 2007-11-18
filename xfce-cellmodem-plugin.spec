%define oname xfce4-cellmodem-plugin

Summary:	The cellmodem plugin is a monitoring plugin for cellular modems
Name:		xfce-cellmodem-plugin
Version:	0.0.5
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cellmodem-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-cellmodem-plugin/%{oname}-%{version}.tar.bz2
Requires:	xfce-panel >= 4.4.1
BuildRequires:	xfce-panel-devel >= 4.4.1
BuildRequires:	libusb-devel
BuildRequires:	perl(XML::Parser)
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The cellmodem plugin is a monitoring plugin for cellular modems.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{oname}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/xfce4/panel-plugins/xfce4-cellmodem-plugin
%{_datadir}/xfce4/panel-plugins/cellmodem.desktop
