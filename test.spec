Name:	    dummy	
Version:	0.0.1
Release:	1%{?dist}
Summary:	

Group:		test
License:	GPL
URL:		http://test.com
Source0:	file.txt

BuildRequires:	
Requires:	

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc



%changelog

