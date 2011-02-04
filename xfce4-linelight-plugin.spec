Summary:	Simple frontend for the locate search
Summary(pl.UTF-8):	Prosty interfejs do wyszukiwania przy pomocy locate
Name:		xfce4-linelight-plugin
Version:	0.1.6
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-linelight-plugin/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	796ea4e795089a10525b8b70a0291e03
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-linelight-plugin
BuildRequires:	libxfcegui4-devel >= 4.4.0
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple frontend for the locate search.

%description -l pl.UTF-8
Prosty interfejs do wyszukiwania przy pomocy locate.

%prep
%setup -q

%build
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
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-linelight-plugin
%{_datadir}/xfce4/panel-plugins/linelight.desktop
%{_iconsdir}/hicolor/*/apps/*
