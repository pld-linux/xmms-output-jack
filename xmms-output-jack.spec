%define		_rnam xmms-jack
Summary:	JACK output plugin for XMMS
Summary(pl):	Wtyczka dla XMMSa odtwarzaj±ca d¼wiêk przez JACKa
Name:		xmms-output-jack
Version:	0.8.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/xmms-jack/%{_rnam}-%{version}.tar.gz
# Source0-md5:	9af42722f8381f4b7a7171cf2a48f845
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
This plugin allows xmms to play sounds though JACK.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê poprzez JACKa.

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
