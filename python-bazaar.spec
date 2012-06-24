
%define module bazaar

Summary:	Abstraction layer between relational database and object oriented application
Summary(pl):	Warstwa abstrakcji mi�dzy baz� relacyjn� a aplikacj� zorientowan� obiektowo
Name:		python-bazaar
Version:	0.99.3
Release:	1
License:	LGPL
Group:		Python/Libraries
Source0:	http://savannah.nongnu.org/download/bazaar/%{module}-%{version}.tar.bz2
# Source0-md5:	6cf4f4d3fbdd14818a204a82319359f1
URL:		http://www.nongnu.org/bazaar/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful abstraction layer between relational database
and object oriented application.

%description -l pl
�atwa w u�yciu i pot�na warstwa abstrakcji mi�dzy relacyjn� baz�
danych a aplikacj� zorientowan� obiektowo.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/html doc/pdf/api.pdf
%{py_sitedir}/bazaar
