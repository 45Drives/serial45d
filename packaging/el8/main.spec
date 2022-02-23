%global debug_package %{nil}
%define _datadir /opt/45drives
%define _build_id_links none

Name: ::package_name::
Version: ::package_version::
Release: ::package_build_version::%{?dist}
Summary: ::package_description_short::
License: ::package_licence::
URL: ::package_url::
Source0: %{name}-%{version}.tar.gz
BuildArch: ::package_architecture_el::
Requires: ::package_dependencies_el::

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
::package_title::
::package_description_long::

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} SERIAL_VERSION="%{version}-::package_build_version::" install


%postun
if [ $1 == 0 ];then
    rm -rf /opt/45drives/serial45d
    rm -f /usr/bin/serial45d
    rmdir /opt/45drives --ignore-fail-on-non-empty
fi

%files
%dir %{_datadir}/serial45d
%defattr(-,root,root,-)
%{_datadir}/serial45d/*
%{_bindir}/*

%changelog
* Wed Feb 23 2022 Mark Hooper <mhooper@45drives.com> 1.0.2-2
- added the ability to serialize 2U Stornado servers
* Thu Feb 10 2022 Mark Hooper <mhooper@45drives.com> 1.0.2-1
- added options for 2U Stornado
* Wed Sep 15 2021 Mark Hooper <mhooper@45drives.com> 1.0.1-5
- added support for X11SPi-TF Motherboards
* Mon Aug 30 2021 Mark Hooper <mhooper@45drives.com> 1.0.1-4
- added 45drives-tools > 2.0.1 as a dependency
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.1-3
- updated welcome message
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.1-2
- second stable build of serial45d
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.1-1
- First stable release
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-13
- made version output in welcome message conditional
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-12
- updated serial version welcome text
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-11
- removed extra newline characters in backup files
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-10
- added skip dialogue
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-9
- fixed indentation
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-8
- removed build id links in .spec file
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-7
- removed build id links in .spec file
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-6
- added _datadir definition in .spec files
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-5
- updated copyright file
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-4
- updated the package dependencies in manifest
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-3
- added required entries to manifest for el7 packaging
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-2
- added el7 packaging
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-1
- first release of serial45d
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 0.1.0-4
- updated architecture
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 0.1.0-3
- updated .gitignore
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 0.1.0-2
- updated makefile
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 0.1.0-1
- first build of serial45d