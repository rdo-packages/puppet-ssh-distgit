%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-ssh
%global commit 8c871493260ff1a7027684c88b61a8b3e172d334
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-ssh
Version:        10.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Manage SSH client and server via Puppet.
License:        ASL 2.0

URL:            https://github.com/saz/puppet-ssh

Source0:        https://github.com/saz/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet-concat
Requires:       puppet >= 2.7.0

%description
Manage SSH client and server via Puppet.

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/ssh/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/ssh/



%files
%{_datadir}/openstack-puppet/modules/ssh/


%changelog
* Mon Mar 13 2023 RDO <dev@lists.rdoproject.org> 10.0.0-1.8c87149git
- Update to post 10.0.0 (8c871493260ff1a7027684c88b61a8b3e172d334)



