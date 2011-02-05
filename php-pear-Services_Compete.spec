%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Services_Compete
Summary:	%{_pearname} - Compete API
Summary(pl.UTF-8):	%{_pearname} - API Compete
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	4
License:	The BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2182c9b6c2e0ab651b386b622e3479fe
URL:		http://pear.php.net/package/Services_Compete/
BuildRequires:	php-pear-PEAR >= 1:1.4.6
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTTP_Request >= 1.4.0
Requires:	php-pear-PEAR-core >= 1:1.4.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Access wrapper class for Compete SnapShop API.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa dostępu do API Compete SnapShop.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Services_Compete/examples/test_Services_Compete.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Compete.php
