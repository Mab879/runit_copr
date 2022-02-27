Name:		runit
Version:	2.1.2
Release:        1%{?dist}
Summary:	A UNIX init scheme with service supervision

License: BSD-3-Clause
URL: http://smarden.org/runit/
Source0: https://github.com/madscientist42/runit/archive/refs/tags/2.1.2.tar.gz


BuildRequires: glibc-static make gcc
#Requires:

%description
runit is a cross-platform Unix init scheme with service supervision,
a replacement for sysvinit, and other init schemes. It runs on GNU/Linux, 
*BSD, MacOSX, Solaris, and can easily be adapted to other Unix operating
systems.

%prep
%autosetup
pwd
ls

%build
package/compile


%install
mkdir -p /usr/local/bin
for i in `cat package/commands`; do
  cp command/$i /usr/local/bin/$i
done

%check
package/check

%files
%license
%doc


%changelog

