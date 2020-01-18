%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name netifaces

Name:           python-netifaces
Version:        0.10.4
Release:        3%{?dist}
Summary:        Python library to retrieve information about network interfaces 

Group:          Development/Libraries
License:        MIT
URL:            https://pypi.python.org/pypi/netifaces
Source0:        https://pypi.python.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python-setuptools


%description
This package provides a cross platform API for getting address information
from network interfaces.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        Python library to retrieve information about network interfaces
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
This package provides a cross platform API for getting address information
from network interfaces.
%endif


%prep
%setup -q -n %{pypi_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif


%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif


%install
%{__python2} setup.py install --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --root $RPM_BUILD_ROOT
popd
%endif


%files
%doc README.rst
%{python2_sitearch}/%{pypi_name}-%{version}-*.egg-info/
%{python2_sitearch}/%{pypi_name}.so

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-*.egg-info/
%{python3_sitearch}/%{pypi_name}*.so
%endif

%changelog
* Tue Oct 20 2015 Jon Schlueter <jschluet@redhat.com> 0.10.4-3
- fix bad case on build section

* Tue Jun 16 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.4-2
- Add python3 subpackage

* Mon Feb 23 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.4-1
- Upstream 0.10.4
- Packaging cleanups

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5-7
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 1 2011 Ryan Rix <ry@n.rix.si> 0.5-1
- Initial packaging effort
