%define		_rnam xmms-jack
Summary:	JACK output plugin for XMMS
Summary(pl):	Wtyczka wyj¶ciowa dla XMMS-a odtwarzaj±ca d¼wiêk przez JACK-a
Name:		xmms-output-jack
Version:	0.10
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/xmms-jack/%{_rnam}-%{version}.tar.gz
# Source0-md5:	40ab4a8c5929eda9c6547faa624686c7
URL:		http://xmms-jack.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel >= 1.2.7
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play sounds though JACK.

%description -l pl
Ta wtyczka pozwala XMMS-owi odtwarzaæ muzykê poprzez JACK-a.

%prep
%setup -qn %{_rnam}

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

rm -f $RPM_BUILD_ROOT%{xmms_output_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{xmms_output_plugindir}/*.so
