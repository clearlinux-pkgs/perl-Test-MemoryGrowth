#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-MemoryGrowth
Version  : 0.04
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-MemoryGrowth-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Test-MemoryGrowth-0.04.tar.gz
Summary  : 'assert that code does not cause growth in memory usage'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Test-MemoryGrowth-license = %{version}-%{release}
Requires: perl-Test-MemoryGrowth-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Test::MemoryGrowth - assert that code does not cause growth in memory
usage

%package dev
Summary: dev components for the perl-Test-MemoryGrowth package.
Group: Development
Provides: perl-Test-MemoryGrowth-devel = %{version}-%{release}
Requires: perl-Test-MemoryGrowth = %{version}-%{release}

%description dev
dev components for the perl-Test-MemoryGrowth package.


%package license
Summary: license components for the perl-Test-MemoryGrowth package.
Group: Default

%description license
license components for the perl-Test-MemoryGrowth package.


%package perl
Summary: perl components for the perl-Test-MemoryGrowth package.
Group: Default
Requires: perl-Test-MemoryGrowth = %{version}-%{release}

%description perl
perl components for the perl-Test-MemoryGrowth package.


%prep
%setup -q -n Test-MemoryGrowth-0.04
cd %{_builddir}/Test-MemoryGrowth-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-MemoryGrowth
cp %{_builddir}/Test-MemoryGrowth-0.04/LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-MemoryGrowth/7e88e362b09da4b18d7e611c14945b5734383496
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::MemoryGrowth.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-MemoryGrowth/7e88e362b09da4b18d7e611c14945b5734383496

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/Test/MemoryGrowth.pm
