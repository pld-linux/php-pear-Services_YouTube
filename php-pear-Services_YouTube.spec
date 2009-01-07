%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	YouTube
%define		_status		alpha
%define		_pearname	Services_YouTube
Summary:	%{_pearname} - PHP Client for YouTube API
Summary(pl.UTF-8):	%{_pearname} - klient PHP do API YouTube
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	084ab1582098ce0550347642c5fcfbd5
URL:		http://pear.php.net/package/Services_YouTube/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP Client for YouTube API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klient PHP do API YouTube.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/Services_YouTube/{docs,examples,ChangeLog}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/YouTube
%{php_pear_dir}/Services/YouTube.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_YouTube
