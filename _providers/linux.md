---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 10
apis:
- description: The set of stable userspace-facing interfaces exposed by the Linux kernel, including system calls, ioctls, eBPF, futex2, and the netlink protocol.
  name: Linux Kernel Userspace API
  slug: linux-kernel-userspace-api
- description: Extended Berkeley Packet Filter (eBPF) userspace API for loading and interacting with sandboxed programs running in the kernel.
  name: eBPF Userspace API
  slug: ebpf-userspace-api
- description: Socket-based interface for communication between the kernel and userspace, used widely for networking, routing, and device configuration.
  name: Netlink API
  slug: netlink-api
- description: SECure COMPuting mode with BPF filters, used to restrict which system calls a process can make for sandboxing and hardening.
  name: Seccomp BPF
  slug: seccomp-bpf
- description: Unprivileged access-control framework allowing processes to restrict themselves and their descendants from filesystem and network operations.
  name: Landlock
  slug: landlock
- description: Virtual filesystem mounted at /proc that exposes process and kernel information through a file-based interface.
  name: procfs
  slug: procfs
- description: Virtual filesystem mounted at /sys that exports kernel object and device information to userspace.
  name: sysfs
  slug: sysfs
- description: The system and service manager API exposed by systemd over D-Bus for managing units, services, and the boot process.
  name: systemd D-Bus API
  slug: systemd-dbus
- description: Pluggable Authentication Modules providing flexible, configurable authentication mechanisms for Linux applications.
  name: Linux PAM
  slug: linux-pam
- description: Device manager for the Linux kernel handling device nodes and hotplug events under /dev.
  name: udev
  slug: udev
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kernel.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kernel.org/doc/html/latest/
- group: docs
  title: ''
  type: Reference
  url: https://man7.org/linux/man-pages/
- group: company
  title: ''
  type: Website
  url: https://www.linuxfoundation.org/
created: '2024-01-15'
description: Linux is an open-source Unix-like operating system kernel originally created by Linus Torvalds. This index catalogs the userspace and kernel programming interfaces exposed by Linux, including system calls, eBPF, ioctl, netlink, procfs, sysfs, GPIO, and security interfaces such as Seccomp, Landlock, and Linux Security Modules. It also covers ecosystem APIs for systemd and PAM.
finops:
- name: Linux Finops
  service_category: API
  slug: linux-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linux.png
layout: provider
modified: '2026-04-28'
name: Linux
nav: Providers
network: true
overview: 'Linux publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Kernel, Linux, Open Source, Operating System, and Unix.


  Linux''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Linux Plans Pricing
  plan_count: 3
  slug: linux-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 5
  name: Linux Rate Limits
  slug: linux-rate-limits
score:
  band: emerging
  composite: 14.0
  delta: 0.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linux/refs/heads/main/screenshots/linux-2026-06-20T184549.png
security:
- kind: domain-security
  name: Linux Domain Security
  slug: linux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linux
tags:
- Kernel
- Linux
- Open Source
- Operating System
- Unix
- Userspace API
website: https://www.kernel.org/
---
