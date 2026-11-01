---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skypilot.ai/en/latest/reference/tpu.html
- group: operate
  href: https://artifacts.apis.io/skypilot/changelog/skypilot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/skypilot-changelog.yml
- group: auth
  href: https://artifacts.apis.io/skypilot/authentication/skypilot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skypilot-authentication.yml
- group: agent
  href: https://artifacts.apis.io/skypilot/llms/skypilot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skypilot-llms.txt
- group: other
  href: https://artifacts.apis.io/skypilot/hosts/skypilot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skypilot-hosts.yml
- group: other
  href: https://artifacts.apis.io/skypilot/vendors/skypilot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skypilot-vendors.yml
- group: build
  href: https://artifacts.apis.io/skypilot/packages/skypilot-packages.yml
  title: ''
  type: SDKs
  url: packages/skypilot-packages.yml
- group: build
  href: https://artifacts.apis.io/skypilot/packages/skypilot-packages.yml
  title: ''
  type: Packages
  url: packages/skypilot-packages.yml
- group: auth
  href: https://artifacts.apis.io/skypilot/security/skypilot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skypilot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.skypilot.co/en/latest/docs/index.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://skypilot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skypilot.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skypilot.ai/en/latest/getting-started/quickstart.html
- group: company
  title: ''
  type: Blog
  url: https://skypilot.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skypilot-org
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skypilot.ai/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://docs.skypilot.co/en/latest/docs/index.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: SkyPilot is an open-source AI compute orchestration platform that enables developers to run large‑scale machine‑learning workloads across multiple clouds, on‑premise clusters, and HPC schedulers. It provides a unified interface for launching, managing, and scaling jobs on Kubernetes, Slurm, and over 20 cloud providers, supporting popular frameworks such as PyTorch, TensorFlow, and DeepSpeed. The project is backed by a vibrant community and recent $20M seed funding, aiming to simplify AI infrastructure for enterprises and researchers alike.
layout: provider
modified: '2026-10-22'
name: SkyPilot
nav: Providers
network: true
overview: 'SkyPilot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, OpenSource, Compute, and Orchestration.


  SkyPilot''s developer surface includes API reference, changelog, authentication, documentation, getting-started guide, engineering blog, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 44.6
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Skypilot Authentication
  slug: skypilot-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Skypilot Domain Security
  slug: skypilot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: skypilot
tags:
- Company
- AI
- OpenSource
- Compute
- Orchestration
website: https://docs.skypilot.co/en/latest/docs/index.html
---
