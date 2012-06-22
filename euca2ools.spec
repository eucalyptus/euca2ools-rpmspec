# Use Python 2.6 on el5
%if 0%{?el5}
%global __python_ver 26
%global __python %{_bindir}/python2.6
%global __os_install_post %{?__python26_os_install_post}
%endif

%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:          euca2ools
Version:       2.1.0
Release:       0%{?build_id:.%build_id}%{?dist}
Summary:       Command line tools for Eucalyptus and AWS

Group:         Applications/System
License:       BSD
URL:           https://github.com/eucalyptus/euca2ools
Source:        %{name}-%{version}%{?tar_suffix}.tar.gz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:     noarch

BuildRequires:  python%{?__python_ver}-devel

# For doc-building
BuildRequires:  python%{?__python_ver}-boto >= 2.0
BuildRequires:  help2man
BuildRequires:  rsync
BuildRequires:  util-linux

Requires:       python%{?__python_ver}-boto >= 2.1
Requires:       rsync
Requires:       util-linux

# %%elseif behaves like %%endif followed by %%if.  Avoid it to reduce confusion.
%if 0%{?el5}
BuildRequires:  python%{?__python_ver}-m2crypto >= 0.20.2
Requires:       python%{?__python_ver}-m2crypto >= 0.20.2
%endif
%if 0%{?rhel} > 5 || 0%{?fedora}
BuildRequires:  m2crypto
Requires:       m2crypto
%endif
%if !0%{?rhel} && !0%{?fedora}
BuildRequires:  python-m2crypto >= 0.20.2
Requires:       python-m2crypto >= 0.20.2
%endif

Obsoletes:      euca2ools-eee < 1.3

%description
EUCALYPTUS is a service overlay that implements elastic computing
using existing resources. The goal of EUCALYPTUS is to allow sites
with existing clusters and server infrastructure to co-host an elastic
computing service that is interface-compatible with Amazon AWS.

This package contains the command line tools used to interact with
Eucalyptus.  These tools are also compatible with Amazon AWS.

%prep
%setup -q -n %{name}-%{version}%{?tar_suffix}


%build
%{__python} setup.py build
export PYTHON=%{__python}
sh -xe generate-manpages.sh


%install
rm -rf %{buildroot}
%{__python} setup.py install --prefix=%{_prefix} --skip-build --root %{buildroot}
%{__python} setup.py install -O1 --prefix=%{_prefix} --skip-build --root %{buildroot}

export DESTDIR=%{buildroot}
export PREFIX=%{_prefix}
sh -xe install-manpages.sh


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_bindir}/euare-*
%{_bindir}/euca-*
%{_bindir}/eustore-*
%{_mandir}/man1/euca*
%{_mandir}/man1/euare*
%{_mandir}/man1/eustore*
%{python_sitelib}/%{name}-*.egg-info
%{python_sitelib}/%{name}/
%doc CHANGELOG
%doc COPYING
%doc INSTALL
%doc README


%changelog
* Fri Jun 22 2012 Eucalyptus Release Engineering <support@eucalyptus.com> - 2.1.0-0
- Bumped to version 2.1.0

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
