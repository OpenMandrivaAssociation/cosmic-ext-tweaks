%undefine _debugsource_packages
%define         appname dev.edfloreshz.CosmicTweaks
Name:           cosmic-ext-tweaks
Version:        0.1.0+git20240929
Release:        0
Summary:        A tweaking tool for the COSMIC DE
License:        GPL-3.0-only
Group:          Utility/COSMIC
URL:            https://github.com/edfloreshz/cosmic-tweaks
Source0:        https://github.com/cosmic-utils/tweaks/archive/refs/heads/tweaks-main.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xkbcommon)

Provides:  cosmic-tweaks

%description
This is a tool which gives you advanced tweaking options for the Cosmic Desktop

%prep
%autosetup -n tweaks-main -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_iconsdir}/hicolor/scalable/apps/dev.edfloreshz.CosmicTweaks.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml
