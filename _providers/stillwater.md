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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stillwater/refs/heads/main/hosts/stillwater-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stillwater-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/stillwater/refs/heads/main/vendors/stillwater-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stillwater-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stillwater/refs/heads/main/packages/stillwater-packages.yml
  title: ''
  type: SDKs
  url: packages/stillwater-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/stillwater/refs/heads/main/packages/stillwater-packages.yml
  title: ''
  type: Packages
  url: packages/stillwater-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StillwaterInsurance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/stillwater/refs/heads/main/security/stillwater-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stillwater-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stillwaterinsurance.com
coverage:
  checked: '2026-10-12'
  detail: Home page returns a JavaScript shell with no machine-readable API documentation.
  evidence:
  - status: 200
    url: https://stillwaterinsurance.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Stillwater is an insurance provider offering home, auto, renters, condo, and business insurance solutions. Founded in 2000 as part of Fidelity National Property and Casualty Insurance Group, it has grown to serve customers nationwide with a focus on personalized service and comprehensive coverage options. The company emphasizes a smooth quoting process, leveraging technology to provide quick estimates and easy policy management for individuals and businesses alike.
layout: provider
modified: '2026-10-12'
name: Stillwater
nav: Providers
network: true
overview: Stillwater is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Homes, Auto, Business, and Technology.
random_paper: 21
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stillwater Domain Security
  slug: stillwater-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stillwater
tags:
- Insurance
- Homes
- Auto
- Business
- Technology
website: https://stillwaterinsurance.com
---
