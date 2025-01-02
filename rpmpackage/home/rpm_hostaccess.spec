Name:		rpm_hostaccess
Version:	1.0
Release:	1%{?dist}
Summary:	Проверка доступности хостов в ЛВС

Group:		Productivity/Networking/Diagnostic
License:	GPL
URL:		https://github.com/kievsan/bashTraining
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	/bin/rm, /bin/mkdir, /bin/cp
Requires:	/bin/bash

BuildArch:	noarch

%description
A diagnostic package

%prep
%autosetup

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}

%changelog
* Mon Dec 30 2024 Kievskiy Sergey kievsan@mail.ru
- Added %{_bindir}/%{name}
