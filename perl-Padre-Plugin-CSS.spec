%define upstream_name    Padre-Plugin-CSS
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.14
Release:	2

Summary:	Padre and CSS
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Padre/Padre-Plugin-CSS-0.14.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CSS::Minifier::XS)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Padre)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(WebService::Validator::CSS::W3C)

BuildArch:	noarch

%description
From Padre:
- use CSS::Minifier::XS to minify css
- use WebService::Validator::CSS::W3C to validate the CSS

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
#./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 655605
- rebuild for updated spec-helper

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 572321
- skip tests (all padre tests are failing on bs)
- update to 0.10

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 444010
- import perl-Padre-Plugin-CSS


* Thu Sep 17 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

