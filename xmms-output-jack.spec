%define		_rnam xmms-jack
%define		_snap 20040119
Summary:	JACK output plugin for XMMS
Summary(pl):	Wtyczka dla XMMSa odtwarzaj±ca d¼wiêk przez JACKa
Name:		xmms-output-jack
Version:	0.7
Release:	0.%{_snap}.1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	%{_rnam}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	e3eb3b37e63b2c6beb68a6cdfc1e746b
URL:		http://xmms-jack.sf.net/
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	xmms-devel >= 1.2.7
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows xmms to play sounds though JACK.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê poprzez JACKa.

%prep
%setup -qn %{_rnam}-%{version}-%{_snap}

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
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_output_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{xmms_output_plugindir}/*
