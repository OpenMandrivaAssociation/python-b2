Name:		python-b2
Version:	4.7.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/b/b2/b2-%{version}.tar.gz
Summary:	Command Line Tool for Backblaze B2
URL:		https://pypi.org/project/b2/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildArch:	noarch
# The executable is probably more relevant than the python lib,
# so people may look for it by that name
Provides:	b2 = %{EVRD}

%patchlist
# Upstream pins docutils<0.22; cooker has 0.23 and b2 only uses it via rst2ansi
b2-relax-docutils-dep.patch

%description
Command Line Tool for Backblaze B2

%files
%{_bindir}/b2
%{_bindir}/b2v3
%{_bindir}/b2v4
%{py_sitedir}/b2
%{py_sitedir}/b2-*.*-info
