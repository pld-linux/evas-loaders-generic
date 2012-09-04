Summary:	Generic loaders for Evas library
Summary(pl.UTF-8):	Ogólne programy wczytujące dla biblioteki Evas
Name:		evas-loaders-generic
Version:	1.7.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/evas_generic_loaders-%{version}.tar.bz2
# Source0-md5:	64df7ed7b161b0cc3f37cf1ca20478cb
URL:		http://trac.enlightenment.org/e/wiki/Evas
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	gstreamer-devel >= 0.10.13
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.13
BuildRequires:	libraw-devel
BuildRequires:	librsvg-devel >= 2.14.0
BuildRequires:	libspectre-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-devel >= 0.20
BuildRequires:	zlib-devel
Requires:	cairo >= 1.0.0
Requires:	eina >= 1.7.0
Requires:	gstreamer >= 0.10.13
Requires:	gstreamer-plugins-base >= 0.10.13
Requires:	librsvg >= 2.14.0
Requires:	poppler >= 0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are additional "generic" loaders for Evas that are stand-alone
executables that evas may run from its generic loader module. This
means that if they crash, the application loading the image does not
crash also. In addition the licensing of these binaries will not
affect the license of any application that uses Evas as this uses a
completely generic execution system that allows anything to be plugged
in as a loader.

This package contains the following loaders:
- GST for multimedia files, using GStreamer
- PDF, using poppler
- PS for PhostScript files, using libspectre
- RAW for raw photos, using libraw
- SVG for SVG graphics, using librsvg
- XCF

%description -l pl.UTF-8
Ten pakiet zawiera dodatkowe "ogólne" moduły wczytujące dla biblioteki
Evas, będące samodzielnymi programami, które mogą być uruchamiane z
poziomu ogólnego modułu wczytującego. Oznacza to, że jeśli ulegną
awarii, nie pociągną za sobą aplikacji wczytującej obraz. Ponadto
licencja niniejszych programów nie wpływa na licencję aplikacji
wykorzystujących bibliotekę Evas, jako że używany jest całkowicie
ogólny mechanizm uruchamiania, pozwalający na podłączenie wszystkiego
jako programu wczytującego.

Ten pakiet zawiera następujące moduły wczytujące:
- GST do plików multimedialnych, wykorzystujący GStreamera
- PDF wykorzystujący popplera
- PS do plików PostScriptowych, wykorzystujący libspectre
- RAW do zdjęć w formacie surowym, wykorzystujący libraw
- SVG do rysunków SVG, wykorzystujący librsvg
- XCF

%prep
%setup -q -n evas_generic_loaders-%{version}

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/evas/utils/evas_image_loader.*
