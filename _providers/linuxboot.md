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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The LinuxBoot project's build system and tooling for replacing UEFI DXE with a Linux kernel-based boot environment. Includes integrations with coreboot/LinuxBoot and UEFI PEI/LinuxBoot configurations.
  name: LinuxBoot Build System
  slug: linuxboot-build-system
- description: u-root is a Go-based universal root filesystem and ramfs builder used by LinuxBoot to assemble a minimal initramfs containing the userspace tools needed for booting.
  name: u-root
  slug: u-root
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/linuxboot/linuxboot/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/linuxboot/linuxboot/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/linuxboot/linuxboot/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linuxboot-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://book.linuxboot.org
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/linuxboot
- group: company
  title: ''
  type: Website
  url: https://www.linuxboot.org/
created: '2026-03-16'
description: LinuxBoot is a Linux Foundation firmware project that uses a Linux kernel and initramfs as a bootloader, replacing specific firmware functionality such as UEFI DXE. It provides faster, more reliable, and more secure boot processes by leveraging the well-tested Linux kernel for hardware initialization. Core components include u-root (the ramfs builder), the LinuxBoot build system, and the NERF (Non-Extensible Reduced Firmware) heritage from Google.
finops:
- name: Linuxboot Finops
  service_category: API
  slug: linuxboot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linuxboot.png
layout: provider
modified: '2026-04-28'
name: LinuxBoot
nav: Providers
network: true
overview: 'LinuxBoot publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Boot, Firmware, Hardware, Linux Foundation, and u-root.


  LinuxBoot''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Linuxboot Plans Pricing
  plan_count: 3
  slug: linuxboot-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Linuxboot Rate Limits
  slug: linuxboot-rate-limits
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  open_source:
    applies: true
    score: 25.0
  previous_composite: 13.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linuxboot/refs/heads/main/screenshots/linuxboot-2026-06-20T184553.png
security:
- kind: domain-security
  name: Linuxboot Domain Security
  slug: linuxboot-domain-security
  summary_line: TLSv1.3
slug: linuxboot
tags:
- Boot
- Firmware
- Hardware
- Linux Foundation
- u-root
- UEFI
website: https://www.linuxboot.org/
---
