Name:     hello
Version:  2.10
Release:  1%{?dist}
Summary:  The "Hello World" program from GNU
License:  GPLv3+
URL:      https://www.gnu.org/software/hello/
Source0:  https://ftp.gnu.org/gnu/hello/hello-%{version}.tar.gz

BuildRequires: make gcc gettext

Requires(post): info
Requires(preun): info

%description
The "Hello World" program, done with all bells and whistles of a proper FOSS
project, including configuration, build, internationalization, help files, etc.

%prep
%autosetup

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%find_lang %{name}
rm -f %{buildroot}%{_infodir}/dir

%post
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/hello
%{_infodir}/*
%{_mandir}/man1/*

%changelog
* Tue Oct 24 2017 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.10-1
- Initial packaging
