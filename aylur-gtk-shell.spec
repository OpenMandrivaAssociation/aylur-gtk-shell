%global debug_package %{nil}

Name:       aylur-gtk-shell
Version:    3.1.0
Release:    1
URL:		https://github.com/aylur/ags
Source0:	%{url}/archive/v%{version}/ags-%{version}.tar.gz
Source1:    ags-%{version}-vendor.tar.gz
Source2:    ags-pnpm-offline-cache.tar.gz
Summary:    Building blocks for creating custom desktop shells
License:    LGPL-2.1-only
Group:      Graphical desktop/ Other

BuildRequires:	meson
BuildRequires:  go
BuildRequires:  pkgconfig(astal-gjs)
BuildRequires:	pkgconfig(gjs-1.0)
BuildRequires:	gjs
BuildRequires:  pnpm

Requires:       astal-gjs
Requires:       astal-libs
Requires:       pkgconfig(gtk4-layer-shell-0)

Supplements:    astal3
Recommends:     astal4

%description
%summary

%prep
%autosetup -n ags-%{version} -p1
tar -xzf %{SOURCE1} -C cli
tar -zxf %{S:2}
%build
pnpm install --offline --force
export GOFLAGS="-buildmode=pie -ldflags=-linkmode=external"
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/ags
%{_datadir}/ags
