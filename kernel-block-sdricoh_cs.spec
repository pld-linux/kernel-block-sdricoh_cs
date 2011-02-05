#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_with	verbose		# verbose build (V=1)

%define		modname	sdricoh_cs
%define		_rel	1
Summary:	Linux kernel module for Ricoh Bay1Controller SD Cardreaders
Summary(pl.UTF-8):	Moduł jądra Linuksa dla Ricoh Bay1Controller SD Cardreaders
Name:		kernel%{_alt_kernel}-block-%{modname}
Version:	0.1.3
Release:	%{_rel}@%{_kernel_ver_str}
License:	GPL v2
Group:		Base/Kernel
Source0:	http://prdownloads.sourceforge.net/sdricohcs/%{modname}-%{version}.tar.gz
# Source0-md5:	f65e891a13ea7469fe8122ad32977588
URL:		http://sdricohcs.sourceforge.net/
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.18}
BuildRequires:	rpmbuild(macros) >= 1.330
%{?with_dist_kernel:%requires_releq_kernel}
Requires(post,postun):	/sbin/depmod
Requires:	module-init-tools >= 3.2.2-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux kernel module for the Ricoh Bay1Controller SD Cardreaders.

%description -l pl
Moduł jądra Linuksa dla Ricoh Bay1Controller SD Cardreaders.

%package -n kernel%{_alt_kernel}-smp-block-%{modname}
Summary:	Linux SMP kernel module for Ricoh Bay1Controller SD Cardreaders
Summary(pl.UTF-8):	Moduł jądra Linuksa SMP dla Ricoh Bay1Controller SD Cardreaders
Release:	%{_rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod
Requires:	module-init-tools >= 3.2.2-2

%description -n kernel%{_alt_kernel}-smp-block-%{modname}
Linux SMP kernel module for Ricoh Bay1Controller SD Cardreaders.

%description -n kernel%{_alt_kernel}-smp-block-%{modname} -l pl
Moduł jądra Linuksa SMP dla Ricoh Bay1Controller SD Cardreaders

%prep
%setup -q -n %{modname}-%{version}

cat > Makefile << EOF
obj-m += sdricoh_cs.o

EOF

%build
%build_kernel_modules -m %{modname}

%install
rm -rf $RPM_BUILD_ROOT

%install_kernel_modules -m %{modname} -d block

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{_alt_kernel}-block-%{modname}
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-block-%{modname}
%depmod %{_kernel_ver}

%files -n kernel%{_alt_kernel}-block-%{modname}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/block/sdricoh_cs.ko.gz
