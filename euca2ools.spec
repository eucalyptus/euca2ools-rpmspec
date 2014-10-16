%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:          euca2ools
Version:       3.1.1
Release:       0%{?build_id:.%build_id}%{?dist}
Summary:       Eucalyptus/AWS-compatible command line tools

Group:         Applications/Internet
License:       BSD
URL:           http://www.eucalyptus.com/
Source0:       %{tarball_basedir}.tar.xz

Requires:       gdisk
Requires:       gzip
Requires:       kpartx
Requires:       openssl
Requires:       parted
Requires:       python-argparse
Requires:       python-lxml
Requires:       python-progressbar >= 2.3
Requires:       python-requestbuilder >= 0.2.0-0.4.pre3
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-six >= 1.4
Requires:       rsync
Requires:       util-linux

# eucalyptus-nc < 4 requires NC-specific commands that were removed in
# euca2ools 3.1.
Conflicts:      eucalyptus-nc < 4

BuildRequires:  python-devel
BuildRequires:  python-setuptools

BuildArch:      noarch


%description
Euca2ools are command line tools used to interact with Amazon
Web Services (AWS) as well as other compatible services, such as
Eucalyptus.  They aim to use the same input as similar tools provided
by AWS for each service individually along with several enhancements
that make them easier to use.


%prep
%setup -q -n %{tarball_basedir}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

mkdir -p %{buildroot}/etc/euca2ools
cp -Rp conf/* %{buildroot}/etc/euca2ools
mkdir -p %{buildroot}/%{_datadir}/euca2ools/certs
cp -p certs/* %{buildroot}/%{_datadir}/euca2ools/certs


%files
%{_bindir}/euare-*
%{_bindir}/euca-*
%{_bindir}/euform-*
%{_bindir}/eulb-*
%{_bindir}/euscale-*
%{_bindir}/euwatch-*
%{_mandir}/man1/euare*
%{_mandir}/man1/euca*
%{_mandir}/man1/euform*
%{_mandir}/man1/eulb*
%{_mandir}/man1/euscale*
%{_mandir}/man1/euwatch*
%{python_sitelib}/%{name}-*.egg-info
%{python_sitelib}/%{name}/
%dir /etc/euca2ools
%dir /etc/euca2ools/bundle-vol
%config(noreplace) /etc/euca2ools/bundle-vol/excludes
%config(noreplace) /etc/euca2ools/bundle-vol/fstab
%dir /etc/euca2ools/conf.d
%config(noreplace) /etc/euca2ools/euca2ools.ini
%config(noreplace) /etc/euca2ools/conf.d/*
%{_datadir}/euca2ools/certs
%doc COPYING
%doc INSTALL
%doc README



%changelog
* Thu Oct 16 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.1
- Version bump (3.1.1)

* Mon Oct  6 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.1
- Added missing deps for euca-bundle-vol (TOOLS-520)

* Mon Sep 22 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0
- Added euform-* man pages

* Fri Jun 20 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.0.3-0
- Switched to xz-compressed sources

* Tue Jun 17 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Switched to xz-compressed sources

* Wed May 28 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Pull in python-six >= 1.4

* Fri May 23 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.0.3-0
- Updated to 3.0.3

* Mon May  5 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Added /etc/euca2ools/conf.d

* Fri May  2 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Added new bundle-vol config files

* Tue Apr 17 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Added euform-* commands
- Updated for 3.1.0-pre3

* Tue Apr  8 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Updated for 3.1.0-pre2

* Wed Mar 19 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Updated for 3.1.0-pre1

* Mon Feb 24 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.1.0-0
- Dropped eustore client tools (TOOLS-423)

* Mon Sep 30 2013 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.0.2-0
- Updated to 3.0.2
- Make tarball_basedir a single macro rather than assembling it ourselves

* Fri Aug 23 2013 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.0.1-0
- Updated to 3.0.1

* Thu May 30 2013 Eucalyptus Release Engineering <support@eucalyptus.com> - 3.0.0-0
- Updated to 3.0.0

* Fri Apr 26 2013 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.1.4-0
- Changed to a more sane version

* Wed Jun  6 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.1.9999-0
- Updated to post-2.1 mainline

* Tue May 22 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.1-0
- Update to 2.1 pre-releases
- Generate man pages at build time

* Fri May 11 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.0.999-0
- Update to post-2.0 mainline

* Thu Mar 15 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.0.1-0.1
- Update to 2.0.1

* Tue Feb 14 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.0-0.2
- Fix euare-usercreate convenience options with --delegate

* Thu Feb  2 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.0-0.1
- Update to 2.0

* Thu Apr 21 2011 Eucalyptus Release Engineering <support@eucalyptus.com> - 1.4-0.1.alpha1
- Update to 1.4 alpha 1 (bzr rev 399)

* Thu Jan 20 2011 Eucalyptus Release Engineering <support@eucalyptus.com> - 1.3.2-0
- Update to nightly builds of 1.3.2

* Wed Aug 18 2010 Eucalyptus Systems <support@eucalyptus.com>
- Don't build m2crypto on fedora

* Wed Mar 17 2010 Eucalyptus Systems <support@eucalyptus.com>
- Added support for fedora

* Fri Feb 12 2010 Eucalyptus Systems <support@eucalyptus.com>
- Version 1.2

* Sun Nov 1 2009 Eucalyptus Systems <support@eucalyptus.com>
- Version 1.1

* Sat Jun 27 2009 Eucalyptus Systems <support@open.eucalyptus.com>
- First public release.
