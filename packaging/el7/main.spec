%global debug_package %{nil}

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
make DESTDIR=%{buildroot} SERIAL_VERSION="%{version}-::package_build_version::" install


%postun
if [ $1 == 0 ];then
    rm -rf /opt/45drives/serial45d
    rm -f /usr/bin/serial45d
    rmdir /opt/45drives --ignore-fail-on-non-empty
fi

%files
%dir /opt/45drives/serial45d
%defattr(-,root,root,-)
/opt/45drives/serial45d/*
%{_bindir}/*

%changelog
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-4
- updated the package dependencies in manifest
* Wed Aug 25 2021 Mark Hooper <mhooper@45drives.com> 1.0.0-3
- added required entries to manifest for el7 packaging
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