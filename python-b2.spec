Name:		python-b2
Version:	4.3.0
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

%description
Command Line Tool for Backblaze B2

%files
%{_bindir}/b2
%{_bindir}/b2v3
%{_bindir}/b2v4
%{py_sitedir}/b2
%{py_sitedir}/b2-*.*-info
