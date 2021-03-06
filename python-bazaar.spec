
%define	module	bazaar

Summary:	Abstraction layer between relational database and object oriented application
Summary(pl.UTF-8):	Warstwa abstrakcji między bazą relacyjną a aplikacją zorientowaną obiektowo
Name:		python-bazaar
Version:	0.99.6
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://savannah.nongnu.org/download/bazaar/%{module}-%{version}.tar.bz2
# Source0-md5:	e9808782a64e912c3a77d7e4c478637c
URL:		http://www.nongnu.org/bazaar/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful abstraction layer between relational database
and object oriented application.

%description -l pl.UTF-8
Łatwa w użyciu i potężna warstwa abstrakcji między relacyjną bazą
danych a aplikacją zorientowaną obiektowo.

%prep
%setup -q -n %{module}-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/html doc/pdf/api.pdf
%{py_sitescriptdir}/bazaar
