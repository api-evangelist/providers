---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 69
  human_in_the_loop: 10
  name: Systemd Agentic Access
  operation_count: 90
  slug: systemd-agentic-access
  summary_line: 90 operations · 69 acting · 10 human-in-the-loop
api_count: 34
apis:
- description: D-Bus API of systemd-localed for getting and setting the system locale, X11 keymap, and console keymap.
  name: systemd-localed (org.freedesktop.locale1)
  slug: org-freedesktop-locale1
- description: D-Bus API of systemd-timedated for getting and setting the system time, timezone, NTP enablement, and RTC-in-local-time policy.
  name: systemd-timedated (org.freedesktop.timedate1)
  slug: org-freedesktop-timedate1
- description: D-Bus API of systemd-timesyncd exposing the current NTP server, peers, root delay/dispersion, and synchronization status.
  name: systemd-timesyncd (org.freedesktop.timesync1)
  slug: org-freedesktop-timesync1
- description: D-Bus API of systemd-homed for managing portable, encrypted user home directories (LUKS, btrfs subvol, fscrypt, CIFS, directory) including create/remove/update/list operations, activation, authenticat
  name: systemd-homed (org.freedesktop.home1)
  slug: org-freedesktop-home1
- description: D-Bus API of systemd-importd for importing, exporting, downloading, listing, and removing container/VM machine images (tar, raw, dkr/OCI, qcow2) used by machined and portable services.
  name: systemd-importd (org.freedesktop.import1)
  slug: org-freedesktop-import1
- description: D-Bus API of systemd-oomd, the userspace out-of-memory killer that uses cgroup v2 PSI signals to kill cgroups under memory or swap pressure. Exposes per-slice/cgroup state and policy.
  name: systemd-oomd (org.freedesktop.oom1)
  slug: org-freedesktop-oom1
- description: D-Bus API of systemd-portabled for attaching/detaching portable service images, listing attached images, inspecting them, and managing their lifecycle on the host.
  name: systemd-portabled (org.freedesktop.portable1)
  slug: org-freedesktop-portable1
- description: D-Bus API of systemd-sysupdated for transactional A/B updates of system/host/portable/container images using systemd-sysupdate transfers, including target enumeration, version listing, and update jobs
  name: systemd-sysupdated (org.freedesktop.sysupdate1)
  slug: org-freedesktop-sysupdate1
- description: Generic D-Bus interface that systemd daemons (and other services) implement to expose runtime log level and log target configuration. Allows tools like systemd-analyze to change verbosity without rest
  name: LogControl1 (org.freedesktop.LogControl1)
  slug: org-freedesktop-logcontrol1
- description: The Boot API from systemd — 1 operation(s) for boot.
  name: systemd Boot API
  slug: systemd-boot-api
- description: The Cache API from systemd — 2 operation(s) for cache.
  name: systemd Cache API
  slug: systemd-cache-api
- description: Transient unit creation and cgroup-backed resource control.
  name: systemd Cgroups API
  slug: systemd-cgroups-api
- description: The Configuration API from systemd — 11 operation(s) for configuration.
  name: systemd Configuration API
  slug: systemd-configuration-api
- description: The Credentials API from systemd — 2 operation(s) for credentials.
  name: systemd Credentials API
  slug: systemd-credentials-api
- description: The Hostname API from systemd — 3 operation(s) for hostname.
  name: systemd Hostname API
  slug: systemd-hostname-api
- description: The Image API from systemd — 1 operation(s) for image.
  name: systemd Image API
  slug: systemd-image-api
- description: The Images API from systemd — 4 operation(s) for images.
  name: systemd Images API
  slug: systemd-images-api
- description: The Inhibitors API from systemd — 1 operation(s) for inhibitors.
  name: systemd Inhibitors API
  slug: systemd-inhibitors-api
- description: Pending and active jobs scheduled by the Manager.
  name: systemd Jobs API
  slug: systemd-jobs-api
- description: The Links API from systemd — 7 operation(s) for links.
  name: systemd Links API
  slug: systemd-links-api
- description: The Machine Info API from systemd — 4 operation(s) for machine info.
  name: systemd Machine Info API
  slug: systemd-machine-info-api
- description: The Machines API from systemd — 7 operation(s) for machines.
  name: systemd Machines API
  slug: systemd-machines-api
- description: The Manager API from systemd — 12 operation(s) for manager.
  name: systemd Manager API
  slug: systemd-manager-api
- description: The PCR API from systemd — 1 operation(s) for pcr.
  name: systemd PCR API
  slug: systemd-pcr-api
- description: The Power API from systemd — 5 operation(s) for power.
  name: systemd Power API
  slug: systemd-power-api
- description: The Resolution API from systemd — 4 operation(s) for resolution.
  name: systemd Resolution API
  slug: systemd-resolution-api
- description: The Resolve API from systemd — 1 operation(s) for resolve.
  name: systemd Resolve API
  slug: systemd-resolve-api
- description: The Seats API from systemd — 1 operation(s) for seats.
  name: systemd Seats API
  slug: systemd-seats-api
- description: The Sessions API from systemd — 5 operation(s) for sessions.
  name: systemd Sessions API
  slug: systemd-sessions-api
- description: System state introspection.
  name: systemd Snapshots API
  slug: systemd-snapshots-api
- description: The Unit API from systemd — 2 operation(s) for unit.
  name: systemd Unit API
  slug: systemd-unit-api
- description: Unit lifecycle and enumeration.
  name: systemd Units API
  slug: systemd-units-api
- description: The UserDatabase API from systemd — 3 operation(s) for userdatabase.
  name: systemd UserDatabase API
  slug: systemd-userdatabase-api
- description: The Users API from systemd — 3 operation(s) for users.
  name: systemd Users API
  slug: systemd-users-api
artifact_total: 63
collections:
- collection_type: open
  name: systemd-hostnamed (org.freedesktop.hostname1)
  slug: open-hostname1
- collection_type: open
  name: systemd-logind (org.freedesktop.login1)
  slug: open-login1
- collection_type: open
  name: systemd-machined (org.freedesktop.machine1)
  slug: open-machine1
- collection_type: open
  name: systemd-networkd (org.freedesktop.network1)
  slug: open-network1
- collection_type: open
  name: systemd-resolved (org.freedesktop.resolve1)
  slug: open-resolve1
- collection_type: open
  name: systemd Manager (org.freedesktop.systemd1)
  slug: open-systemd1
- collection_type: open
  name: systemd Varlink Interfaces (io.systemd.*)
  slug: open-varlink
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/systemd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/systemd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://systemd.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.freedesktop.org/software/systemd/man/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/systemd
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/systemd/systemd
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/systemd/systemd
- group: commercial
  title: ''
  type: License
  url: https://github.com/systemd/systemd/blob/main/LICENSES/LGPL-2.1-or-later.txt
- group: commercial
  title: ''
  type: License
  url: https://github.com/systemd/systemd/blob/main/LICENSES/GPL-2.0-or-later.txt
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/systemd/systemd/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/systemd/systemd/blob/main/NEWS
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/systemd/systemd/issues
- group: other
  title: ''
  type: PullRequests
  url: https://github.com/systemd/systemd/pulls
- group: other
  title: ''
  type: MailingList
  url: https://lists.freedesktop.org/mailman/listinfo/systemd-devel
- group: company
  title: ''
  type: Mastodon
  url: https://mastodon.social/@pid_eins
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/systemctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/networkctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/resolvectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/loginctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/machinectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/hostnamectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/timedatectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/localectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/busctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/varlinkctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/bootctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/homectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/coredumpctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/oomctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/portablectl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/importctl.html
- group: build
  title: ''
  type: Tools
  url: https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html
- group: build
  title: ''
  type: SDKs
  url: https://www.freedesktop.org/software/systemd/man/latest/sd-bus.html
- group: build
  title: ''
  type: SDKs
  url: https://www.freedesktop.org/software/systemd/man/latest/sd-varlink.html
- group: build
  title: ''
  type: SDKs
  url: https://www.freedesktop.org/software/systemd/man/latest/sd-journal.html
- group: build
  title: ''
  type: SDKs
  url: https://www.freedesktop.org/software/systemd/man/latest/sd-event.html
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/systemd-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/systemd-context.jsonld
created: '2026-05-23'
description: systemd is a suite of basic building blocks for a Linux system. It runs as PID 1 and is the system and service manager that bootstraps the rest of the userspace, supervises long-running services, and exposes a coordinated set of D-Bus and Varlink IPC interfaces for managing services (systemd1), users and sessions (logind), network interfaces (networkd), name resolution (resolved), containers/VMs (machined), home directories (homed), boot entries (boot1/sysupdate1), system hostname/locale/timedate, OOM protection (oomd), portable services, and image imports. The project also publishes a stable command-line surface (systemctl, journalctl, networkctl, resolvectl, loginctl, machinectl, hostnamectl, timedatectl, localectl, busctl, varlinkctl, bootctl, homectl, coredumpctl, oomctl, portablectl, importctl, systemd-analyze and more). systemd is dual-licensed (LGPL-2.1-or-later for libraries and most code, GPL-2.0-or-later for select tools) and developed openly on GitHub at systemd/systemd.
examples:
- key_count: 4
  name: Login1 Inhibit Example
  slug: login1-inhibit-example
- key_count: 3
  name: Login1 Listsessions Example
  slug: login1-listsessions-example
- key_count: 3
  name: Machine1 Listmachines Example
  slug: machine1-listmachines-example
- key_count: 3
  name: Network1 Listlinks Example
  slug: network1-listlinks-example
- key_count: 4
  name: Resolve1 Resolvehostname Example
  slug: resolve1-resolvehostname-example
- key_count: 3
  name: Systemd1 Listunits Example
  slug: systemd1-listunits-example
- key_count: 4
  name: Systemd1 Starttransient Example
  slug: systemd1-starttransient-example
- key_count: 4
  name: Systemd1 Startunit Example
  slug: systemd1-startunit-example
- key_count: 4
  name: Varlink Credentials Encrypt Example
  slug: varlink-credentials-encrypt-example
- key_count: 4
  name: Varlink Userdb Getuser Example
  slug: varlink-userdb-getuser-example
image: https://systemd.io/assets/systemd-logo.svg
json_schemas:
- name: logind Session
  property_count: 10
  slug: login1-session
- name: machined Machine
  property_count: 7
  slug: machine1-machine
- name: networkd Link
  property_count: 8
  slug: network1-link
- name: systemd Job
  property_count: 6
  slug: systemd1-job
- name: systemd Unit
  property_count: 10
  slug: systemd1-unit
- name: systemd JSON User Record (partial)
  property_count: 19
  slug: varlink-user-record
json_structures:
- name: Systemd Structure
  property_count: 1
  slug: systemd-structure
jsonld:
- class_count: 32
  name: Systemd Context
  property_count: 0
  slug: systemd-context
layout: provider
modified: '2026-05-23'
name: systemd
nav: Providers
network: true
overview: 'systemd publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Boot API, Cache API, Cgroups API, and 22 more. Tagged areas include Boot, Cgroups, Container, D-Bus, and Init.


  The systemd catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  systemd''s developer surface includes documentation, release notes, changelog, tooling, and 35 more developer resources.'
random_paper: 57
rules:
- name: systemd API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: systemd-jsonschema-spectral-rules
- name: systemd API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 4
  slug: systemd-rules
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.7
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/systemd/refs/heads/main/screenshots/systemd-2026-06-20T194839.png
security:
- kind: domain-security
  name: Systemd Domain Security
  slug: systemd-domain-security
  summary_line: TLSv1.3 · DMARC
slug: systemd
tags:
- Boot
- Cgroups
- Container
- D-Bus
- Init
- IPC
- Journal
- Linux
- Logging
- Network
- Open Source
- PID 1
- Service Manager
- System
- Systemd
- Varlink
website: https://systemd.io
---
