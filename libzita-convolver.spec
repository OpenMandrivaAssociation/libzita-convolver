%define name_base       zita-convolver
%define name            libzita-convolver
%define version         3.1.0
%define release         1
%define lib_major       3
%define lib_name        %mklibname %name_base %{lib_major}
%define lib_name_devel  %mklibname %name_base -d

Name:           %{name}
Summary:        Audio convolution engine library needed by jconvolver
Version:        %{version}
Release:        %{release}

Source:         http://www.kokkinizita.net/linuxaudio/downloads/%name_base-%{version}.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio/
License:        LGPLv2
Group:          Sound
BuildRequires:  fftw3-devel

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

%build
cd libs
CPPFLAGS="%{optflags} -fPIC -mmmx -msse -mfpmath=sse -ffast-math" make

%install
rm -rf %{buildroot}
cd libs
PREFIX=%{buildroot}%{_prefix} make install

%clean
rm -rf %{buildroot}
