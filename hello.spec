Name:     hello
Version:  2.10
Release:  2%{?dist}
Summary:  A simple "Hello World" script for testing tito-based RPM builds
License:  GPLv3+
URL:      https://github.com/abn/hello-rpm-tito

BuildArch: noarch

%description
A simple "Hello World" shell script for testing tito-based RPM builds.

%prep
%setup -q

%install
install -D -m 755 hello %{buildroot}%{_bindir}/hello

%files
%{_bindir}/hello

%changelog
* Tue May 12 2026 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.10-2
- Switch to ReleaseTagger and reset spec for clean tito release
  (arun.neelicattu@gmail.com)
- fix: convert to noarch shell script for tito build compatibility
  (arun.neelicattu@gmail.com)
- Add README with tito usage instructions (arun.neelicattu@gmail.com)

* Tue Oct 24 2017 Arun Babu Neelicattu <arun.neelicattu@gmail.com> 2.10-1
- Initial packaging
