%define upstream_name    strictures
%define upstream_version 1.002002

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
I've been writing the equivalent of this module at the top of my code for
about a year now. I figured it was time to make it shorter.

Things like the importer in 'use Moose' don't help me because they turn
warnings on but don't make them fatal - which from my point of view is
useless because I want an exception to tell me my code isn't warnings
clean.

Any time I see a warning from my code, that indicates a mistake.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*


