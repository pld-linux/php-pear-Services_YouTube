%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Services_YouTube
Summary:	%{_pearname} - PHP Client for YouTube API
Summary(pl.UTF-8):	%{_pearname} - klient PHP do API YouTube
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	084ab1582098ce0550347642c5fcfbd5
URL:		http://pear.php.net/package/Services_YouTube/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-curl
Requires:	php-pear
Requires:	php-simplexml
Suggests:	php-pear-Cache_Lite
Suggests:	php-pear-XML_RPC2
Obsoletes:	php-pear-Services_YouTube-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdocdir		%{_docdir}/phpdoc

# exclude optional dependencies
%define		_noautoreq	pear(Cache/Lite.*) pear(XML/RPC2.*)

%description
PHP Client for YouTube API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klient PHP do API YouTube.

Ta klasa ma w PEAR status: %{_status}.

%package phpdoc
Summary:	Online manual for %{_pearname}
Summary(pl.UTF-8):	Dokumentacja online do %{_pearname}
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for %{_pearname}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{_pearname}.

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .
mv docs/%{_pearname}/ChangeLog .
mv docs/%{_pearname}/docs/* docs
mv docs/Documentation phpdoc

# This is just naughty, Smarty cache files packaged
find phpdoc -name 26d3399f63abd43a7d72f8c21440dcb0 | xargs rm -rv

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{_pearname}
cp -a phpdoc/* $RPM_BUILD_ROOT%{_phpdocdir}/%{_pearname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc ChangeLog
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/YouTube
%{php_pear_dir}/Services/YouTube.php

%{_examplesdir}/%{name}-%{version}

%files phpdoc
%defattr(644,root,root,755)
%doc docs/tutorials.html
%{_phpdocdir}/%{_pearname}
