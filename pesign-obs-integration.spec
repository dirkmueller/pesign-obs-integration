#
# spec file for package pesign-obs-integration
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
# needssslcertforbuild


Name:           pesign-obs-integration
Summary:        Macros and scripts to sign the kernel and bootloader
License:        GPL-2.0
Group:          Development/Tools/Other
Version:        6.0
Release:        0.<RELEASE15>
Requires:       openssl mozilla-nss-tools
%ifarch %ix86 x86_64 ia64
Requires:       pesign
%endif
BuildRequires:  openssl
Url:            http://en.opensuse.org/openSUSE:UEFI_Image_File_Sign_Tools
Source2:        pesign-repackage.spec.in
Source3:        pesign-gen-repackage-spec
Source4:        brp-99-pesign
Source5:        COPYING
Source6:        README
Source7:        kernel-sign-file
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides scripts and rpm macros to automate signing of the
boot loader, kernel and kernel modules in the openSUSE Buildservice.

%prep
%setup -cT
cp %_sourcedir/{COPYING,README} .

%build

%install

mkdir -p %buildroot/usr/lib/rpm/brp-suse.d %buildroot/usr/lib/rpm/pesign
cd %_sourcedir
install  pesign-gen-repackage-spec kernel-sign-file %buildroot/usr/lib/rpm/pesign
install  brp-99-pesign %buildroot/usr/lib/rpm/brp-suse.d
install -m644 pesign-repackage.spec.in %buildroot/usr/lib/rpm/pesign
if test -e _projectcert.crt; then
	openssl x509 -inform PEM -in _projectcert.crt \
		-outform DER -out %buildroot/usr/lib/rpm/pesign/pesign-cert.x509
else
	echo "No buildservice project certificate available"
fi

%files
%defattr(-,root,root)
%doc COPYING README
/usr/lib/rpm/*

%changelog
