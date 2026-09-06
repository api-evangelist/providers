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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 12
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bootc-dev/bootc/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/bootc-dev/bootc/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bootc-dev/bootc/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bootc-dev/bootc/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bootc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bootc.dev
- group: docs
  title: ''
  type: Documentation
  url: https://bootc.dev/bootc/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bootc-dev/bootc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/containers/bootc
- group: operate
  title: ''
  type: Community
  url: https://github.com/bootc-dev/bootc/discussions
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/bootc-dev/bootc/releases
- group: company
  title: ''
  type: Blog
  url: https://bootc.dev/rss.xml
created: '2024-01-01'
description: Bootc is an open source tool that enables transactional, in-place operating system updates using OCI/Docker container images as the source for OS updates. It applies the container layering model to bootable host systems, using standard OCI containers as a transport and delivery format for base operating system updates. The container image includes a Linux kernel, and when deployed the base userspace runs normally with systemd as PID 1. Bootc is a CNCF Sandbox project with a stable CLI and API.
features:
- features:
  - Pull Latest OCI Image
  - Stage New Deployment
  - Auto-Apply on Reboot
  - Download-Only Mode
  - Update Checking
  name: bootc upgrade
  url: https://bootc.dev/bootc/
- features:
  - Change Container Image Reference
  - Switch OS Distribution
  - Change Registry Source
  - Seamless Image Tracking
  name: bootc switch
  url: https://bootc.dev/bootc/
- features:
  - Current Booted Image Display
  - Staged Changes Status
  - JSON Output
  - YAML Output
  name: bootc status
  url: https://bootc.dev/bootc/
- features:
  - Revert to Previous Boot
  - Boot Loader Entry Reordering
  - Safe Rollback
  name: bootc rollback
  url: https://bootc.dev/bootc/
- features:
  - Install to Disk
  - Install to Filesystem
  - Offline Installation
  - Air-Gapped Deployment
  name: bootc install
  url: https://bootc.dev/bootc/bootc-install.html
- features:
  - OCI Image Format
  - Docker Image Compatibility
  - Container Registry Support
  - Layered Image Model
  - Linux Kernel in Image
  name: OCI/Docker Compatibility
  url: https://bootc.dev/bootc/
- features:
  - ostree Backend
  - Atomic Updates
  - Content-Addressed Storage
  - Deployment Management
  name: ostree Integration
  url: https://bootc.dev/bootc/
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bootc.png
layout: provider
modified: '2026-04-19'
name: Bootc
nav: Providers
network: true
overview: 'Bootc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CNCF, Container Images, Infrastructure, OCI, and Open-Source.


  Bootc''s developer surface includes documentation, release notes, engineering blog, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 11.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bootc/refs/heads/main/screenshots/bootc-2026-06-20T173605.png
security:
- kind: domain-security
  name: Bootc Domain Security
  slug: bootc-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bootc
tags:
- CNCF
- Container Images
- Infrastructure
- OCI
- Open-Source
- Operating Systems
- System Updates
use_cases:
- features:
  - Transactional Updates
  - In-Place OS Updates
  - Atomic Upgrades
  - Rollback Support
  - Container-Based Updates
  - OCI Image Updates
  name: OS Image Updates
  url: https://bootc.dev/bootc/upgrades.html
- features:
  - Disk Installation
  - Filesystem Installation
  - Container to Disk
  - Day 2 OS Setup
  name: OS Image Installation
  url: https://bootc.dev/bootc/bootc-install.html
- features:
  - Image Reference Switching
  - Distribution Switching
  - Container Registry Tracking
  name: Container Image Switching
  url: https://bootc.dev/bootc/
- features:
  - Immutable OS
  - Reproducible Systems
  - GitOps for OS
  - Infrastructure as Code
  - Container Native OS
  name: Immutable Infrastructure
  url: https://bootc.dev/bootc/
website: https://bootc.dev
---
