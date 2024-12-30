Name:           rpm_hostaccess
Version:        1.0
Release:        1%{?dist}
Summary:	    Проверка доступности хостов в ЛВС
Group:		    Testing
License:	    GPL
URL:		    https://github.com/kievsan/bashTraining
Source0:	    %{name}-%{version}.tar.gz
BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp
Requires:	    /bin/bash

BuildArch:	    x86_64

%description
A test package

%prepare
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 ~/rpmbuild/SOURCES/%{name}-%{version}/%{name}.sh %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}.sh

%changelog
* Mon Dec 30 2024 Sergey Kievskiy kievsan@mail.ru
- Added %{_bindir}/%{name}.sh
