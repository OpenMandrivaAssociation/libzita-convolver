%define name_base       zita-convolver
%define lib_major       3
%define lib_name        %mklibname %name_base %{lib_major}
%define lib_name_devel  %mklibname %name_base -d

Name:           libzita-convolver
Summary:        Audio convolution engine library needed by jconvolver
Version:        4.0.3
Release:        1

Source:         https://kokkinizita.linuxaudio.org/linuxaudio/downloads/zita-convolver-%{version}.tar.bz2
URL:            https://kokkinizita.linuxaudio.org/linuxaudio/
License:        LGPLv2
Group:          Sound
BuildRequires:  pkgconfig(fftw3)

%description
Convolution engine library for use with jconvolver. Jconvolver is a
Convolution Engine for JACK using FFT-based partitioned convolution with
multiple partition sizes. It is mainly used to create realistic acoustic
environments for sounds sent to its input. Jconvolver uses a configurable
smallest partition size at the start of the impulse response, and longer
ones further on. This it allows long impulse responses along with minimal
or even zero delay at a reasonable CPU load.

#-----------------------------------
%package -n %{lib_name}

Summary:        Audio convolution engine library needed by jconvolver
Group:          Sound

%description -n %{lib_name}
Convolution engine library for use with jconvolver. Jconvolver is a
Convolution Engine for JACK using FFT-based partitioned convolution with
multiple partition sizes. It is mainly used to create realistic acoustic
environments for sounds sent to its input. Jconvolver uses a configurable
smallest partition size at the start of the impulse response, and longer
ones further on. This it allows long impulse responses along with minimal
or even zero delay at a reasonable CPU load.

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so.*

#-----------------------------------
%package -n %{lib_name_devel}

Summary:        The zita-convolver library development headers
Group:          Sound
Requires:       %{lib_name} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development files needed to build applications against libzita-convolver.

%files -n %{lib_name_devel}
%defattr(-,root,root,-)
%{_libdir}/%{name}.so
%{_includedir}/*.h

#-----------------------------------

%prep
%setup -q -n %name_base-%{version}
cd libs
perl -pi -e 's/PREFIX =/#PREFIX =/g' Makefile
perl -pi -e 's/CPPFLAGS \+=/#CPPFLAGS \+=/g' Makefile
perl -pi -e 's/ldconfig//g' Makefile
perl -pi -e 's/-march=native//g' Makefile

%build
cd libs
CPPFLAGS="%{optflags} -fPIC -mmmx -msse -mfpmath=sse -ffast-math" make

%install
rm -rf %{buildroot}
cd libs
PREFIX=%{buildroot}%{_prefix} make install

%clean
rm -rf %{buildroot}


%changelog
* Sun Apr 15 2012 Frank Kober <emuse@mandriva.org> 3.1.0-1
+ Revision: 791105
- removed march CXX flag from Makefile
- update to new version 3.1.0
  o major is 3

* Thu Mar 04 2010 Frank Kober <emuse@mandriva.org> 2.0.0-2mdv2011.0
+ Revision: 514246
- rebuild
- use optimization flags

* Tue Mar 02 2010 Frank Kober <emuse@mandriva.org> 2.0.0-1mdv2010.1
+ Revision: 513698
- import libzita-convolver
- import libzita-convolver


