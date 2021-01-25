# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

%global packname rlang
%global packver  0.4.10
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4.10
Release:          2%{?dist}
Summary:          Functions for Base Types and Core R and 'Tidyverse' Features

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz
Patch0001:        0001-Unbundle-libxxhash.patch
# https://github.com/r-lib/rlang/pull/1084
Patch0002:        0002-Add-test-hashes-for-big-endian-machines.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils
# Suggests:  R-cli, R-covr, R-crayon, R-glue, R-magrittr, R-methods, R-pak, R-pillar, R-rmarkdown, R-testthat >= 3.0.0, R-vctrs >= 0.2.3, R-withr
# LinkingTo:
# Enhances:

BuildRequires:    pkgconfig(libxxhash)
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils
%if %{without bootstrap}
BuildRequires:    R-cli
BuildRequires:    R-crayon
BuildRequires:    R-glue
BuildRequires:    R-magrittr
BuildRequires:    R-methods
BuildRequires:    R-pak
BuildRequires:    R-pillar
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 3.0.0
BuildRequires:    R-vctrs >= 0.2.3
BuildRequires:    R-withr
%endif

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
%patch0002 -p1

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION
popd


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%if %{without bootstrap}
%{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/backtrace-ver


%changelog
* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.10-1
- Update to latest version (#1911718)

* Sat Nov 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.9-1
- Update to latest version (#1901765)

* Sat Oct 10 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.8-1
- Update to latest version (#1886418)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.7-1
- Update to latest version

* Fri Jul  3 2020 José Matos <jamatos@fedoraproject.org> - 0.4.6-4
- skip check on bootstrap (testthat is required for tests)

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.4.6-3
- bootstrap off

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 0.4.6-2
- bootstrap on
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.6-1
- Update to latest version

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.5-1
- Update to latest version

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.2-1
- Update to latest version

* Fri Oct 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.0-1
- Update to latest version

* Sun Apr 07 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.4-1
- Update to latest version

* Mon Apr 01 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.3-1
- Update to latest version

* Fri Mar 22 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.2-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.3.1-1
- Update to latest version
- Enable tests

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.2-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.1-1
- Update to latest version

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.2.0-2
- rebuild for R 3.5.0

* Sun Mar 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.2.0-1
- initial package for Fedora
