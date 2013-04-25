%define	pkgname	require_all
Summary:	A wonderfully simple way to load your code
Name:		ruby-%{pkgname}
Version:	1.2.1
Release:	1
License:	GPL or MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	e1b78e9e38833e514bbd323e8e377917
URL:		http://github.com/jarmo/require_all
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A wonderfully simple way to load your code.

The easiest way to use require_all is to just point it at a directory
containing a bunch of .rb files. These files can be nested under
subdirectories as well:

require_all 'lib'

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{_bindir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile CHANGES LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
