
%define module bazaar

Summary:	Abstraction layer between relational database and object oriented application
Summary(pl):	Warstwa abstrakcji miêdzy baz± relacyjn± a aplikacj± zorientowan± obiektowo
Name:		python-bazaar
Version:	0.99.4
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://savannah.nongnu.org/download/bazaar/%{module}-%{version}.tar.bz2
# Source0-md5:	c5f4e56d169066548db992ff090c1307
URL:		http://www.nongnu.org/bazaar/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful abstraction layer between relational database
and object oriented application.

%description -l pl
£atwa w u¿yciu i potê¿na warstwa abstrakcji miêdzy relacyjn± baz±
danych a aplikacj± zorientowan± obiektowo.

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
