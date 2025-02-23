Name:		python-b2
Version:	4.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/b/b2/b2-%{version}.tar.gz
Summary:	Command Line Tool for Backblaze B2
URL:		https://pypi.org/project/b2/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	python3.11dist(pdm-backend)
BuildArch:	noarch
# The executable is probably more relevant than the python lib,
# so people may look for it by that name
Provides:	b2 = %{EVRD}

%patchlist
# b2 meets all the requirements listed at
# https://class-registry.readthedocs.io/en/latest/upgrading_to_v5.html
# So let's allow phx-class-registry 5.x
b2-relax-phx-class-registry-dep.patch

%description
Command Line Tool for Backblaze B2

%files
%{_bindir}/b2
%{_bindir}/b2v3
%{_bindir}/b2v4
%{py_sitedir}/b2
%{py_sitedir}/b2-*.*-info
