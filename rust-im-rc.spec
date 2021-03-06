# Generated by rust2rpm 10
# * metrohash and proptest-derive are not packaged
%bcond_with check
%global debug_package %{nil}

%global crate im-rc

Name:           rust-%{crate}
Version:        13.0.0
Release:        4%{?dist}
Summary:        Immutable collection datatypes (the fast but not thread safe version)

# Upstream license specification: MPL-2.0+
License:        MPLv2.0
URL:            https://crates.io/crates/im-rc
Source:         %{crates_source}
# Initial patched metadata
# - Bump quickcheck to 0.9 (upstreamed)
Patch0:         im-rc-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Immutable collection datatypes (the fast but not thread safe version).}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENCE.md
%doc README.md CHANGELOG.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+proptest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proptest-devel %{_description}

This package contains library source intended for building other packages
which use "proptest" feature of "%{crate}" crate.

%files       -n %{name}+proptest-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+quickcheck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quickcheck-devel %{_description}

This package contains library source intended for building other packages
which use "quickcheck" feature of "%{crate}" crate.

%files       -n %{name}+quickcheck-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages
which use "rayon" feature of "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 20:38:23 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 13.0.0-3
- Bump quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 09 18:38:02 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 13.0.0-1
- Initial package
