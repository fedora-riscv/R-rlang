%global packname  rlang
%global rlibdir  %{_libdir}/R/library

# rmarkdown is not available.
%global with_doc 0
# pillar and testthat requires rlang.
%global with_loop 0

Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Functions for Base Types and Core R and 'Tidyverse' Features

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-crayon, R-knitr, R-methods, R-pillar, R-rmarkdown >= 0.2.65, R-testthat, R-covr
# LinkingTo:
# Enhances:

Suggests:         R-crayon
Suggests:         R-methods
Suggests:         R-pillar
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-crayon
BuildRequires:    R-methods
%if %{with_doc}
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown >= 0.2.65
%endif
%if %{with_loop}
BuildRequires:    R-testthat >= 2.0.0
BuildRequires:    R-pillar
%endif

%description
A toolbox for working with base types, core R features like the condition
system, and core 'Tidyverse' features like tidy evaluation.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if !%{with_doc} || !%{with_loop}
export _R_CHECK_FORCE_SUGGESTS_=0
%endif
%if !%{with_doc}
args=--ignore-vignettes
%endif
%if !%{with_loop}
args="$args --no-tests"
%endif
%{_bindir}/R CMD check %{packname} ${args}


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
