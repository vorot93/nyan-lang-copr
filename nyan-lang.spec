%define original_name nyan
%define tag 0.2
%define add 12
%define commit g7e88374

Name:       %{original_name}-lang
Vendor:     SFTtech
Version:    %{tag}_%{add}_%{commit}
Release:    1
Summary:    Typesafe hierarchical key-value database with inheritance and dynamic patching for mod APIs

License:    LGPL-3.0-or-later
URL:        https://github.com/%{vendor}/%{original_name}
Source0:    https://github.com/%{vendor}/%{original_name}/archive/refs/heads/v%{tag}-%{add}-%{commit}.tar.gz

BuildRequires:  cmake, gcc, gcc-c++, binutils

%description
nyan is a data description language, It is a mixture of python, json, patch, wml, yaml and some new ideas.

It stores hierarchical objects with key-value pairs in a database with the key idea that changes in a parent affect all children.

We created nyan because there existed no suitable language to properly represent the enormous complexity of storing the data for openage.

The main focus is readability and moddability.

%build
%cmake .
%cmake_build

%install
%cmake_install

%files
%{_libdir}/%{original_name}.so

%changelog
* Tue Apr 04 2023 Artem Vorotnikov <artem@vorotnikov.me> - 0.2_12_g7e88374-1
- Initial specification file
