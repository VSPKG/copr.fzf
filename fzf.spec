Name:           fzf
Version:        0.54.3
Release:        1
Summary:        A command-line fuzzy finder

License:        MIT
URL:            https://github.com/junegunn/fzf
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  go

%define debug_package %{nil}

%description
fzf is a general-purpose command-line fuzzy finder.

%prep
%autosetup

%build
rm -rf ./* ./.*
git clone %{url} .
git checkout v%{version}
make

%install
mv target/fzf-* target/fzf
install -m 755 -Dp target/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat Apr 27 2024 Vineel Sai <mail@vineelsai.com> 0.50.0-1
- new package built with tito
