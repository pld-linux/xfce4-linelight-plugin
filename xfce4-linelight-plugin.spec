Summary:	Simple frontend for the locate search
Summary(pl.UTF-8):	Prosty interfejs do wyszukiwania przy pomocy locate
Name:		xfce4-linelight-plugin
Version:	0.1.6
Release:	9
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-linelight-plugin/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	796ea4e795089a10525b8b70a0291e03
Patch0:		includes.patch
Patch1:		%{name}-gio.patch
Patch2:		%{name}-ui.patch
Patch3:		%{name}-xfcerc.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-linelight-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	xfce4-panel-devel >= 4.10.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple frontend for the locate search.

%description -l pl.UTF-8
Prosty interfejs do wyszukiwania przy pomocy locate.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/xfce4/panel-plugins/xfce4-linelight-plugin
%{_datadir}/xfce4/panel-plugins/linelight.desktop
%{_iconsdir}/hicolor/*/apps/*
