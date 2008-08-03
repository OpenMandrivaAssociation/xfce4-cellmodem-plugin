Summary:	Monitoring plugin for cellular modems
Name:		xfce4-cellmodem-plugin
Version:	0.0.5
Release:	%mkrel 6
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cellmodem-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-cellmodem-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libusb-devel
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-cellmodem-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
The cellmodem plugin is a monitoring plugin for cellular modems.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README ChangeLog
%{_libdir}/xfce4/panel-plugins/xfce4-cellmodem-plugin
%{_datadir}/xfce4/panel-plugins/cellmodem.desktop
