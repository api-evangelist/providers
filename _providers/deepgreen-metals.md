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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/deepgreen-metals/hosts/deepgreen-metals-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deepgreen-metals-hosts.yml
- group: other
  href: https://artifacts.apis.io/deepgreen-metals/vendors/deepgreen-metals-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deepgreen-metals-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deepgreen-metals/security/deepgreen-metals-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deepgreen-metals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/deepgreen-metals_stock/
created: '2026-10-22'
description: DeepGreen Metals is a company identified in the secondary-market harvest backlog and added as a stub for full-pipeline profiling. The company focuses on sustainable metal extraction and investment, aiming to provide transparent data and APIs related to metal markets, ESG metrics, and resource management. Further details about its services, documentation, and API endpoints are pending discovery and verification.
layout: provider
modified: '2026-10-22'
name: DeepGreen Metals
nav: Providers
network: true
overview: DeepGreen Metals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 2
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
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
  name: Deepgreen Metals Domain Security
  slug: deepgreen-metals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: deepgreen-metals
tags:
- Company
website: https://forgeglobal.com/deepgreen-metals_stock/
---
