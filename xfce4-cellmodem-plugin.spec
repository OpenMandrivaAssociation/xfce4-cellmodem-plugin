Summary:	Monitoring plugin for cellular modems
Name:		xfce4-cellmodem-plugin
Version:	0.0.5
Release:	13.1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://goodies.xfce.org/projects/panel-plugins/xfce4-cellmodem-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-cellmodem-plugin/%{name}-%{version}.tar.bz2
Patch0:		xfce4-cellmodem-plugin-0.0.5-rosa-linkage.patch
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	pkgconfig(libxfce4panel-1.0)
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
sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

# required for patch0
xdt-autogen

%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_libexecdir}/xfce4/panel-plugins/xfce4-cellmodem-plugin
%{_datadir}/xfce4/panel-plugins/cellmodem.desktop
