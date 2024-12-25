%define _unpackaged_files_terminate_build 1

Name: alterator-icons
Version: 0.1
Release: alt1

Summary: Icons for alterator applications
License: GPLv3+
Group:   Other
Url:     https://github.com/LenkaDEA/alterator-icons
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

%description
Icons for alterator applications.

%prep

%setup

%install
mkdir -p %buildroot%_alterator_datadir/icons
cp -R %name/* %buildroot%_alterator_datadir/icons

%files
%doc LICENSE.md README.md
%_alterator_datadir/icons/alterator

%changelog
* Wed Dec 25 2024 Elena Dyatlenko <lenka@altlinux.org> 0.1-alt1
- Create icons for alterator applications

