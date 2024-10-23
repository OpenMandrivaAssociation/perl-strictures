%define upstream_name    strictures

Name:		perl-%{upstream_name}
Version:	2.000006
Release:	3

Summary:	strictures perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/strictures
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
Provides:	perl(strictures)
BuildArch:	noarch

%description
I've been writing the equivalent of this module at the top of my code for
about a year now. I figured it was time to make it shorter.

Things like the importer in 'use Moose' don't help me because they turn
warnings on but don't make them fatal - which from my point of view is
useless because I want an exception to tell me my code isn't warnings
clean.

Any time I see a warning from my code, that indicates a mistake.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make test

%install
%make_install

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
