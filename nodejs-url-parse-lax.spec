%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# xo and ava not in fedora yet
%global enable_tests 0
%global module_name url-parse-lax

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.0.0
Release:        4%{?dist}
Summary:        The url.parse() with support for protocol-less URLs & IPs

License:        MIT
URL:            https://github.com/sindresorhus/url-parse-lax
Source0:        https://github.com/sindresorhus/%{module_name}/archive/%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires: %{?scl_prefix}npm(ava)
BuildRequires: %{?scl_prefix}npm(xo)
%endif

%description
The url.parse() with support for protocol-less URLs & IPs.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
xo && ava
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-4
- rebuilt

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Enable scl macros, fix license macro for el6

* Sun Nov 29 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging
