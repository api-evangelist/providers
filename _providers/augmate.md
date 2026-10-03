---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augmate/refs/heads/main/hosts/augmate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augmate-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/augmate/refs/heads/main/packages/augmate-packages.yml
  title: ''
  type: SDKs
  url: packages/augmate-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/augmate/refs/heads/main/packages/augmate-packages.yml
  title: ''
  type: Packages
  url: packages/augmate-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/augmate
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augmate/refs/heads/main/security/augmate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augmate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augmate.io
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/augmate
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Augmate provides a mission‑driven IoT and wearable device management platform that connects employees, customers, devices and data. Their solutions enable enterprises to deploy and manage head‑mounted displays, smart glasses, and other wearables at scale across industries such as smart medicine, energy, agriculture, retail, and automotive. Augmate’s platform offers device provisioning, app distribution, data analytics, and integration via robust APIs, supporting blockchain‑enabled, protocol‑agnostic, tokenized architectures for secure IoT deployments.
layout: provider
modified: '2026-09-26'
name: Augmate
nav: Providers
network: true
overview: Augmate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Wearables, Device Management, and Enterprise.
random_paper: 14
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 44.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Augmate Domain Security
  slug: augmate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: augmate
tags:
- Company
- IoT
- Wearables
- Device Management
- Enterprise
website: https://augmate.io
---
