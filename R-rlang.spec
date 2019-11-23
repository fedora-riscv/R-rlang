# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%bcond_with bootstrap

%global packname  rlang
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Functions for Base Types and Core R and 'Tidyverse' Features

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-cli, R-covr, R-crayon, R-magrittr, R-methods, R-pillar, R-rmarkdown, R-testthat >= 2.3.0
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-cli
BuildRequires:    R-crayon
BuildRequires:    R-magrittr
BuildRequires:    R-methods
%if %{without bootstrap}
BuildRequires:    R-pillar
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 2.3.0
%endif

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


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
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --no-tests
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
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
