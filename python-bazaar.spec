Summary:	Easy to use and powerful abstraction layer between relational database and object oriented application
Name:		bazaar
Version:	0.99.0
Release:	1
License:	LGPL
Group:		Python/Libraries
Source0:	http://savannah.nongnu.org/download/bazaar/%{name}-%{version}.tar.bz2
# Source0-md5:	b6a5b87cc6aad61c53657a481ae767b1
URL:		http://www.nongnu.org/bazaar/
BuildRequires:	python-devel >= 2.3
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use and powerful abstraction layer between relational database and
object oriented application.

%prep
%setup -q

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
