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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Polygen Studio provides a platform for AI‑generated content and workflow automation.
  name: Polygen Studio API
  slug: polygen-studio-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/polygen/hosts/polygen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polygen-hosts.yml
- group: other
  href: https://artifacts.apis.io/polygen/vendors/polygen-vendors.yml
  title: ''
  type: Vendors
  url: vendors/polygen-vendors.yml
- group: auth
  href: https://artifacts.apis.io/polygen/security/polygen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polygen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polygen.studio/
coverage:
  checked: '2026-10-18'
  detail: Home page returns a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.polygen.studio/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: 'Polygen Studio is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://polgen-studio-2u39aztgv-ben-karsts-projects.vercel.app/opengraph-image.png?49c2c3ea917a06c7
layout: provider
modified: '2026-10-18'
name: Polygen Studio
nav: Providers
network: true
overview: Polygen Studio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 22
score:
  band: minimal
  composite: 2.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Polygen Domain Security
  slug: polygen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: polygen
tags:
- Company
website: https://polygen.studio/
---
