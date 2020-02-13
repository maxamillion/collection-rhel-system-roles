Name: rhel-system-roles
Summary: Set of interfaces for unified system management
Version: 1.0
Release: 10.0000001%{?dist}

#Group: Development/Libraries
License: GPLv3+ and MIT and BSD

%global roleprefix rhel-system-roles.
%global collection_namespace redhat
%global collection_name rhel_system_roles

%global collection_dir %{_datadir}/ansible/collections/ansible_collections/%{collection_namespace}/%{collection_name}

Source0: redhat-rhel_system_roles-1.0.0.tar.gz

Url: https://github.com/maxamillion/collection-rhel-system-roles
BuildArch: noarch

BuildRequires: asciidoc
BuildRequires: pandoc
BuildRequires: highlight

Requires: python3-jmespath

Obsoletes: rhel-system-roles-techpreview < 1.0-3

# We need to put %%description within the if block to avoid empty
# lines showing up.
%if 0%{?rhel}
%description
Collection of Ansible roles and modules that provide a stable and
consistent configuration interface for managing multiple versions
of Red Hat Enterprise Linux.
%else
%description
Collection of Ansible roles and modules that provide a stable and
consistent configuration interface for managing multiple versions
of Fedora, Red Hat Enterprise Linux & CentOS.
%endif

%prep
%setup -qc

%build

%install

mkdir -p $RPM_BUILD_ROOT%{collection_dir}
cp -r ./* $RPM_BUILD_ROOT%{collection_dir}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles
for role in $RPM_BUILD_ROOT%{collection_dir}/roles/*
do
    cp -pR ${role} $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}$(basename ${role})

    mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}/$(basename ${role})
    for docfile in README.md COPYING LICENSE
    do
        if [ -f ${role}/${docfile} ]
        then
            cp -p ${role}/${docfile} $RPM_BUILD_ROOT%{_pkgdocdir}/$(basename ${role})/${docfile}
        fi
    done
done

mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}selinux/selinux-playbook.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/selinux/example-selinux-playbook.yml

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}timesync/examples
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}timesync/examples/multiple-ntp-servers.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/timesync/example-timesync-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}timesync/examples/single-pool.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/timesync/example-timesync-pool-playbook.yml

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/bond-with-vlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-bond-with-vlan-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/bridge-with-vlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-bridge-with-vlan-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/eth-simple-auto.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-eth-simple-auto-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/eth-with-vlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-eth-with-vlan-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/infiniband.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-infiniband-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/macvlan.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-macvlan-playbook.yml
cp -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/remove-profile.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-remove-profile-playbook.yml
rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/remove-profile.yml
cp -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/down-profile.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-down-profile-playbook.yml
rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/down-profile.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/inventory \
   $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-inventory
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/ethtool-features.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-ethtool-features-playbook.yml
mv $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples/ethtool-features-default.yml \
    $RPM_BUILD_ROOT%{_pkgdocdir}/network/example-ethtool-features-default-playbook.yml


rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}*/semaphore
rm -r $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}*/molecule
rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}*/.travis.yml
rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}*/.ansible-lint

rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/.gitignore
rm $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/tests/.gitignore
rmdir $RPM_BUILD_ROOT%{_datadir}/ansible/roles/%{roleprefix}network/examples

%files
%dir %{_datadir}/ansible
%dir %{_datadir}/ansible/roles
%if 0%{?rolealtprefix:1}
%{_datadir}/ansible/roles/%{rolealtprefix}kdump
%{_datadir}/ansible/roles/%{rolealtprefix}postfix
%{_datadir}/ansible/roles/%{rolealtprefix}selinux
%{_datadir}/ansible/roles/%{rolealtprefix}timesync
%{_datadir}/ansible/roles/%{rolealtprefix}network
%{_datadir}/ansible/roles/%{rolealtprefix}storage
%endif
%{_datadir}/ansible/roles/%{roleprefix}kdump
%{_datadir}/ansible/roles/%{roleprefix}postfix
%{_datadir}/ansible/roles/%{roleprefix}selinux
%{_datadir}/ansible/roles/%{roleprefix}timesync
%{_datadir}/ansible/roles/%{roleprefix}network
%{_datadir}/ansible/roles/%{roleprefix}storage
%doc %{_pkgdocdir}/*/example-*-playbook.yml
%doc %{_pkgdocdir}/network/example-inventory
%doc %{_pkgdocdir}/*/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}kdump/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}postfix/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}selinux/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}timesync/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}network/README.md
%doc %{_datadir}/ansible/roles/%{roleprefix}storage/README.md

%{collection_dir}
%doc %{collection_dir}/roles/*/README.md


%license %{_pkgdocdir}/*/COPYING
%license %{_pkgdocdir}/*/LICENSE
%license %{_datadir}/ansible/roles/%{roleprefix}kdump/COPYING
%license %{_datadir}/ansible/roles/%{roleprefix}postfix/COPYING
%license %{_datadir}/ansible/roles/%{roleprefix}selinux/COPYING
%license %{_datadir}/ansible/roles/%{roleprefix}timesync/COPYING
%license %{_datadir}/ansible/roles/%{roleprefix}network/LICENSE
%license %{_datadir}/ansible/roles/%{roleprefix}storage/LICENSE

%changelog
* Thu Feb 13 2020 Adam Miller <admiller@redhat.com> - 1.0-10.0000001
- Example port to Collections with downstream packaging to offer backwards compat

* Mon Oct 21 2019 Pavel Cahyna <pcahyna@redhat.com> - 1.0-10
- Add the storage_safe_mode option, true by default, to prevent accidental
  data removal: rhbz#1763242, issue #42, PR #43 and #51.

* Thu Aug 15 2019 Pavel Cahyna <pcahyna@redhat.com> - 1.0-9
- Add the storage role

* Thu Jun 13 2019 Pavel Cahyna <pcahyna@redhat.com> - 1.0-7
- Update tests for the network role
- Fix typo in a test for the timesync role
- Tag tests suitable for Tier1 testing
- Rebase the network role to add support for device features (PR#115,
  rhbz#1696703) and atomic changes (PR#119, rhbz#1695161)
- network: apply upstream PR#121: allow modifying interface attributes
  without disrupting services (rhbz#1695157)

* Wed May 29 2019 Pavel Cahyna <pcahyna@redhat.com> - 1.0-6
- Rebase the selinux role, fixes typo in tests, uncovered by Ansible 2.7,
  (rhbz#1677743) and lists all input variables in defaults
  to make Satellite aware of them (rhbz#1674004, PR#43)
- Rebase the kdump role to fix check mode problems: rhbz#1685904
- Rebase the timesync role: fixes check mode problems (rhbz#1685904)
  and lists all input variables in defaults (rhbz#1674004)
- Rebase the network role: keeps the interface up for state: up
  if persistent_state is absent and solves problems with defining
  VLAN and MACVLAN interface types (issue #19) (rhbz#1685902)

* Sat Jan 12 2019 Pavel Cahyna <pcahyna@redhat.com> - 1.0-5
- spec file improvement: Unify the source macros with deftag() and defcommit()
- Update to upstream released versions and drop unnecessary patches.
- Unify the spec file with Fedora (no functional changes intended).
- Misc spec file comments fixes (by Mike DePaulo)
- Fix rpmlint error by escaping a previous changelog entry with a macro (by Mike DePaulo)
- Comply with Fedora guidelines by always using "cp -p" in %%install (by Mike DePaulo)
- Rebase network role - doc improvements, Fedora 29 and Ansible 2.7 support
- Regenerate network role patch to apply without offset
- Rebase kdump role to fix a forgotten edit, rhbz#1645633
- Update timesync examples: add var prefix (rhbz#1642152), correct role prefix
- Add Obsoletes for the -techpreview subpackage
- Add warnings to role READMEs and other doc updates, rhbz#1616018
- network: split the state setting into state and persistent_state, rhbz#1616014
- depend on python-jmespath as Ansible will not ship it, rhbz#1660559

* Tue Aug 14 2018 Pavel Cahyna <pcahyna@redhat.com> - 1.0-4
- Format the READMEs as html, by vdolezal, with changes to use highlight
  (source-highlight does not understand YAML)

* Thu Aug  9 2018 Pavel Cahyna <pcahyna@redhat.com> - 1.0-3
- Rebase the network role to the last revision (d866422).
  Many improvements to tests, introduces autodetection of the current provider
  and defaults to using profile name as interface name.
- Rebase the selinux, timesync and kdump roles to their 1.0rc1 versions.
  Many changes to the role interfaces to make them more consistent
  and conforming to Ansible best practices.
- Update the description.

* Fri May 11 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-4
- Fix complaints about /usr/bin/python during RPM build by making the affected scripts non-exec
- Fix merge botch

* Mon Mar 19 2018 Troy Dawson <tdawson@redhat.com> - 0.6-3.1
- Use -a (after cd) instead of -b (before cd) in %setup

* Wed Mar 14 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-3
- Minor corrections of the previous change by Till Maas.

* Fri Mar  9 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-2
- Document network role options: static routes, ethernet, dns
  Upstream PR#36, bz1550128, documents bz1487747 and bz1478576

* Tue Jan 30 2018 Pavel Cahyna <pcahyna@redhat.com> - 0.6-1
- Drop hard dependency on ansible (#1525655), patch from Yaakov Selkowitz
- Update the network role to version 0.4, solves bz#1487747, bz#1478576

* Tue Dec 19 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.5-3
- kdump: fix the wrong conditional for ssh checking and improve test (PR#10)

* Tue Nov 07 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.5-2
- kdump: add ssh support. upstream PR#9, rhbz1478707

* Tue Oct 03 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.5-1
- SELinux: fix policy reload when SELinux is disabled on CentOS/RHEL 6
  (bz#1493574)
- network: update to b856c7481bf5274d419f71fb62029ea0044b3ec1 :
  makes the network role idempotent (bz#1476053) and fixes manual
  network provider selection (bz#1485074).

* Mon Aug 28 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.4-1
- network: update to b9b6f0a7969e400d8d6ba0ac97f69593aa1e8fa5:
  ensure that state:absent followed by state:up works (bz#1478910), and change
  the example IP adresses to the IANA-assigned ones.
- SELinux: fix the case when SELinux is disabled (bz#1479546).

* Tue Aug 8 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.3-2
- We can't change directories to symlinks (rpm bug #447156) so keep the old
  names and create the new names as symlinks.

* Tue Aug 8 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.3-1
- Change the prefix to linux-system-roles., keeping compatibility
  symlinks.
- Update the network role to dace7654feb7b5629ded0734c598e087c2713265:
  adds InfiniBand support and other fixes.
- Drop a patch included upstream.

* Mon Jun 26 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.2-2
- Leave a copy of README and COPYING in every role's directory, as suggested by T. Bowling.
- Move the network example inventory to the documentation directory together.
  with the example playbooks and delete the now empty "examples" directory.
- Use proper reserved (by RFC 7042) MAC addresses in the network examples.

* Tue Jun 6 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.2-1
- Update the networking role to version 0.2 (#1459203)
- Version every role and the package separately. They live in separate repos
  and upstream release tags are not coordinated.

* Mon May 22 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.1-2
- Prefix the roles in examples and documentation with rhel-system-roles.

* Thu May 18 2017 Pavel Cahyna <pcahyna@redhat.com> - 0.1-1
- Update to 0.1 (first upstream release).
- Remove the tuned role, it is not ready yet.
- Move the example playbooks to /usr/share/doc/rhel-system-roles/$SUBSYSTEM
  directly to get rid of an extra directory.
- Depend on ansible.

* Thu May 4 2017  Pavel Cahyna <pcahyna@redhat.com> - 0-0.1.20170504
- Initial release.
- kdump r. fe8bb81966b60fa8979f3816a12b0c7120d71140
- postfix r. 43eec5668425d295dce3801216c19b1916df1f9b
- selinux r. 1e4a21f929455e5e76dda0b12867abaa63795ae7
- timesync r. 33a1a8c349de10d6281ed83d4c791e9177d7a141
- tuned r. 2e8bb068b9815bc84287e9b6dc6177295ffdf38b
- network r. 03ff040df78a14409a0d89eba1235b8f3e50a750

