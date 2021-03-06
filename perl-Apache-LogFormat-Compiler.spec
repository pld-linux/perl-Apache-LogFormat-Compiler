#
# Conditional build:
%bcond_without	tests		# build without tests

%define		pdir	Apache
%define		pnam	LogFormat-Compiler
Summary:	Apache::LogFormat::Compiler - Compile a log format string to perl-code
Name:		perl-Apache-LogFormat-Compiler
Version:	0.35
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cbb0bf041ade8a39f65eadbdf8a346c1
URL:		http://search.cpan.org/dist/Apache-LogFormat-Compiler/
BuildRequires:	perl-Module-Build-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{with tests}
BuildRequires:	perl-HTTP-Message
BuildRequires:	perl-Test-MockTime
BuildRequires:	perl-POSIX-strftime-Compiler
BuildRequires:	perl-Try-Tiny
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compile a log format string to Perl-code. For faster generation of
access_log lines.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
		--destdir=$RPM_BUILD_ROOT \
		--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/%{pdir}/LogFormat
%{perl_vendorlib}/%{pdir}/LogFormat/*.pm
%{_mandir}/man3/*.3*
