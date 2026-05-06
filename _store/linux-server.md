---
aid: linux-server
name: Linux Server
description: Linux Server is a topic catalog covering management, administration, and monitoring interfaces used to operate Linux servers in production. It organizes references to systemd, cockpit, the Linux audit framework, package managers (apt, dnf, rpm), configuration management and provisioning tooling, and remote administration protocols commonly used on Linux servers.
type: Topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Infrastructure
  - Linux
  - Server
  - System Administration
  - DevOps
url: https://raw.githubusercontent.com/api-evangelist/linux-server/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: linux-server:systemd
    name: systemd
    description: System and service manager for Linux, providing process supervision, socket activation, journaled logging, and a D-Bus management API.
    humanURL: https://systemd.io/
    tags:
      - Service Management
      - Init
      - D-Bus
    properties:
      - type: Documentation
        url: https://www.freedesktop.org/software/systemd/man/
      - type: Reference
        url: https://www.freedesktop.org/wiki/Software/systemd/dbus/
      - type: SourceCode
        url: https://github.com/systemd/systemd
  - aid: linux-server:cockpit
    name: Cockpit
    description: Web-based graphical interface for Linux server administration, providing tools for managing services, storage, networking, and accounts.
    humanURL: https://cockpit-project.org/
    tags:
      - Administration
      - Web UI
      - Remote
    properties:
      - type: Documentation
        url: https://cockpit-project.org/documentation.html
      - type: SourceCode
        url: https://github.com/cockpit-project/cockpit
  - aid: linux-server:linux-audit
    name: Linux Audit
    description: The Linux audit subsystem and userspace tools for tracking security-relevant events on a Linux server.
    humanURL: https://github.com/linux-audit/audit-documentation
    tags:
      - Security
      - Auditing
      - Compliance
    properties:
      - type: Documentation
        url: https://github.com/linux-audit/audit-documentation/wiki
      - type: SourceCode
        url: https://github.com/linux-audit/audit-userspace
  - aid: linux-server:apt
    name: APT
    description: The Advanced Package Tool used by Debian, Ubuntu, and derivatives for installing, upgrading, and removing software packages.
    humanURL: https://wiki.debian.org/Apt
    tags:
      - Package Management
      - Debian
      - Ubuntu
    properties:
      - type: Documentation
        url: https://manpages.debian.org/bookworm/apt/apt.8.en.html
  - aid: linux-server:dnf
    name: DNF
    description: The Dandified YUM package manager used on Fedora, RHEL, CentOS Stream, and related distributions.
    humanURL: https://dnf.readthedocs.io/
    tags:
      - Package Management
      - Fedora
      - RHEL
    properties:
      - type: Documentation
        url: https://dnf.readthedocs.io/en/latest/
      - type: SourceCode
        url: https://github.com/rpm-software-management/dnf
  - aid: linux-server:openssh
    name: OpenSSH
    description: The de facto standard suite for secure remote login, command execution, and file transfer on Linux servers.
    humanURL: https://www.openssh.com/
    tags:
      - Remote Access
      - Security
      - SSH
    properties:
      - type: Documentation
        url: https://www.openssh.com/manual.html
      - type: SourceCode
        url: https://github.com/openssh/openssh-portable
  - aid: linux-server:journald
    name: systemd-journald
    description: The systemd journal daemon, providing structured, indexed logs for the Linux server with a query API via journalctl and libsystemd.
    humanURL: https://www.freedesktop.org/software/systemd/man/systemd-journald.service.html
    tags:
      - Logging
      - Observability
    properties:
      - type: Documentation
        url: https://www.freedesktop.org/software/systemd/man/systemd-journald.service.html
common:
  - type: Website
    name: Linux Foundation
    description: The Linux Foundation hosts the Linux kernel project.
    url: https://www.linuxfoundation.org/
  - type: Documentation
    name: Linux Kernel Documentation
    description: Official kernel documentation tree.
    url: https://www.kernel.org/doc/html/latest/
  - type: Reference
    name: Linux man-pages
    description: The Linux man-pages project.
    url: https://man7.org/linux/man-pages/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
